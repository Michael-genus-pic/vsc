from fastapi import FastAPI, HTTPException
from mongo_queue.queue import Queue
from pymongo import MongoClient
import schedule

from utils.apiTypes import Message, ApiQueueData, ScheduleQueueData
from utils.config import config
import json
import time
import datetime

from fastapi_versioning import VersionedFastAPI, version

subApp = FastAPI(docs_url="/docs", title = 'Notification')



queue = Queue( MongoClient(config['db']['url']).testDB.queue, consumer_id="consumer1",  timeout=300, max_attempts=len(config['retryWait']))



@subApp.post("/apiFunction")
@version(1)
async def queueApiFunction(info: ApiQueueData) -> Message:
    job = queue.put(info.model_dump(),delay = 0, channel="apiFunction")
    return {"msg": str(job)}

@subApp.post("/scheduled")
@version(1)
async def queueScheduled(info: ScheduleQueueData) -> Message:
    job = queue.put(info.model_dump(), delay = info.delay, channel="scheduled")  
    return {"msg": str(job)}



subApp = VersionedFastAPI(subApp, enable_latest=True)

app= FastAPI()

app.mount('/notification', subApp)