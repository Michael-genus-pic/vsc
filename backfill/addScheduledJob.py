from mongo_queue.queue import Queue
from pymongo import MongoClient
from utils.config import config


mongoClient = MongoClient(config['db']['url'])
queue = Queue( mongoClient.testDB.queue, consumer_id="consumer1",  timeout=300, max_attempts=len(config['retryWait']))

payload = {'delay': 120, "randomkey": "randomvalue"}
initialDelay = 0
queue.put(payload, delay=0, channel="scheduled")