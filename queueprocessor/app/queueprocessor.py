import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mongo_queue.queue import Queue
from pymongo import MongoClient
import schedule
from types import ModuleType

from utils.config import config
import time
import datetime
import utils.apiFunctions as apiFunctions


mongoClient = MongoClient(config['db']['url'])

queue = Queue( mongoClient.testDB.queue, consumer_id="consumer1",  timeout=300, max_attempts=len(config['retryWait']))

queueLogCollection = mongoClient.testDB.queueLogs


def runQueueMessage() -> None:
    result = {"processed": 0, "success": [], "reQueued": [], "stopped": []}
    channels = {'apiFunction': apiFunctionProcessor, 'scheduled': scheduled}
    for channel, runFunc in channels.items():
        job =  queue.next(channel=channel)
        while job is not None :
            result['processed'] = result["processed"] + 1
            runResult = 'success'
            try:
                runFunc(job.payload)
                job.complete()
            except Exception as e:
                state = job.state
                if state is None:
                    state = {}
                if "errorHistory" not in state:
                    state['errorHistory'] = []
                state['errorHistory'].append({"Error": str(e), "errorTime": datetime.datetime.now()})
                runResult = 'reQueued' if job.attempts < len(config['retryWait'])-1 else "stopped"
                job.release(sleep=config['retryWait'][job.attempts], state=state) 
            result[runResult].append(str(job.__dict__['_data']['_id']))
            job =  queue.next(channel=channel)
        if result['processed']:
            result['run_at'] = datetime.datetime.now()
            result['channel'] = channel
            queueLogCollection.insert_one(result)


def apiFunctionProcessor(payload):
    action = getattr(getattr(apiFunctions, payload['destination']), payload['function'])
    response = action(**payload['params'])
    
def scheduled(payload):
    queue.put({"payload":payload}, delay=120, channel="scheduled")
    
    mongodb_client = MongoClient(config['db']['url'])
    db = mongodb_client.testDB
    collection = db.scheduledRun
    currentDate = datetime.datetime.now()
    collection.insert_one({'executed': currentDate, "payload":payload})
    
    

schedule.every(5).seconds.do(runQueueMessage)
print ('Starting')
while True:
    schedule.run_pending()
    time.sleep(1)
