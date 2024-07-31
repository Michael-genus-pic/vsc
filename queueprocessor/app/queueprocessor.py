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

logCollection = mongoClient.testDB.logs


def runQueueMessage() -> None:
    print ('nnnnnnnnnnnnnew')
    result = {"processed": 0, "success": 0, "reQueued": 0, "stopped": 0}
    channels = {'apiFunction': apiFunctionProcessor}
    for channel, runFunc in channels.items():
        job =  queue.next(channel=channel)
        while job is not None :
            print (str(job.__dict__['_data']['_id']))
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
            
            print ('be3fore', result)
            # result[runResult].append(str(job.__dict__['_data']['_id']))
            result[runResult] = result[runResult] +1 
            print ('after', result)
            job =  queue.next()
            print (3333333333, str(job.__dict__['_data']['_id']))
        if result['processed']:
            result['run_at'] = datetime.datetime.now()
            result['channel'] = channel
            logCollection.insert_one(result)


def apiFunctionProcessor(payload):
    action = getattr(getattr(apiFunctions, payload['destination']), payload['function'])
    response = action(**payload['params'])
    

schedule.every(10).seconds.do(runQueueMessage)
print ('Starting')
while True:
    schedule.run_pending()
    time.sleep(1)
