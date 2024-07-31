from types import FunctionType
from mongo_queue.queue import Queue
from pymongo import MongoClient

from utils.config import config


queue = Queue( MongoClient(config['db']['url']).testDB.queue, consumer_id="consumer1",  timeout=300, max_attempts=len(config['retryWait']))

def enqueueApiCall(apiFuncton: FunctionType, params: dict = {}, delay: int = 0)->dict:
    destination, apiFunction = apiFuncton.__qualname__.split('.')
    payload = {
        "destination": destination,
        "function": apiFunction,
        "params":params,
        }
    queue.put(payload, delay = delay, channel="apiFunction")  

    return {}