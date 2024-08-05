from fastapi import FastAPI, HTTPException
from mongo_queue.queue import Queue
from pymongo import MongoClient
import schedule

from utils.apiTypes import Message, QueueData
from utils.config import config
import json
import time
import datetime

from fastapi_versioning import VersionedFastAPI, version

subApp = FastAPI(docs_url="/docs", title = 'Versioning Test')



queue = Queue( MongoClient(config['db']['url']).testDB.queue, consumer_id="consumer1",  timeout=300, max_attempts=len(config['retryWait']))



@subApp.get("/ep")
@version(1)
async def apiMessage() -> Message:
    return {"msg": "V1"}

@subApp.get("/ep")
@version(2)
async def apiMessage() -> Message:
    return {"msg": "V2"}



subApp = VersionedFastAPI(subApp, enable_latest=True)


app= FastAPI()

app.mount('/versioning', subApp)