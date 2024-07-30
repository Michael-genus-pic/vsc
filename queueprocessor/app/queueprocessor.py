import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mongo_queue.queue import Queue
from pymongo import MongoClient
import schedule

from utils.config import config
import time
import datetime
import utils.apiFunctions as apiFunctions


mongoClient = MongoClient(config['db']['url'])

queue = Queue( mongoClient.testDB.queue, consumer_id="consumer1",  timeout=300, max_attempts=len(config['retryWait']))

logCollection = mongoClient.testDB.logs


def runQueueMessage() -> None:
    result = {"processed": 0, "success": 0, "reQueued": 0, "stopped": 0}
    job =  queue.next()
    while job is not None :
        result['processed'] = result["processed"] + 1
        runResult = 'success'
        try:
            runQueue(job.payload)
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
        result[runResult] = result[runResult] +1
        job =  queue.next()
    if result['processed']:
        result['run_at'] = datetime.datetime.now()
        logCollection.insert_one(result)


def runQueue(payload):
    print ("payload", payload)
    action = getattr(getattr(apiFunctions, payload['destination']), payload['function'])
    response = action(**payload['params'])
    print ("response", response)
    

schedule.every(5).seconds.do(runQueueMessage)
print ('Starting')
while True:
    schedule.run_pending()
    time.sleep(1)
