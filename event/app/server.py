from fastapi import FastAPI, HTTPException
from mongo_queue.queue import Queue
from pymongo import MongoClient
import schedule

from bson.objectid import ObjectId
from utils.apiTypes import Message
from utils.config import config
import utils.apiFunctions as apiFunctions

from utils.enqueueFunctions import enqueueApiCall
from utils.functions import mongoToJson

from fastapi_versioning import VersionedFastAPI, version
from utils.apiTypes import OnTest, Event, OffTest

subApp = FastAPI(docs_url="/docs", title = 'Event')

subApp.mongodb_client = MongoClient(config['db']['url'])
db = subApp.mongodb_client.testDB
collection = db.Event

queue = Queue( MongoClient(config['db']['url']).testDB.queue, consumer_id="consumer1",  timeout=300, max_attempts=len(config['retryWait']))



@subApp.post("/onTest",     
    description="addOnTestEvent",
    response_model=Event,
    responses={400: {"model": Message}},)
@version(1)
async def addOnTestEvent(onTest: OnTest) -> Event:
    existingEvent = collection.find_one({"eventName": "OnTest", "eventData.ident":onTest.ident, "eventData.testDate": onTest.testDate})
    if existingEvent is not None:
        raise HTTPException(
            status_code=400,
            detail={"msg": f"Event already Exists with {onTest.ident} at {onTest.testDate}"},
        )       
    try:
        apiFunctions.animal_latest.Getanimalbyid(onTest.ident)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail={"msg": f"No Animal Found with Ident {onTest.ident}"},
        )        
    onTestData={"eventName": "OnTest", "eventData": onTest.model_dump()}
    insertResult = collection.insert_one(onTestData)
    insertedEvent = collection.find_one({"_id": ObjectId(insertResult.inserted_id)})
    eventObj = mongoToJson(insertedEvent)
    enqueueApiCall(apiFunctions.animal_latest.Addevent, {"ident": onTest.ident, "payload":eventObj })
    return eventObj


@subApp.post("/offTest",     
    description="addOffTestEvent",
    response_model=Event,
    responses={400: {"model": Message}},)
@version(1)
async def addOffTestEvent(offTest: OffTest) -> Event:
    existingEvent = collection.find_one({"eventName": "OffTest", "eventData.ident":offTest.ident, "eventData.testDate": offTest.testDate})
    if existingEvent is not None:
        raise HTTPException(
            status_code=400,
            detail={"msg": f"Event already Exists with {offTest.ident} at {offTest.testDate}"},
        )       
    try:
        apiFunctions.animal_latest.Getanimalbyid(offTest.ident)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail={"msg": f"No Animal Found with Ident {offTest.ident}"},
        )        
    offTestData={"eventName": "OffTest", "eventData": offTest.model_dump()}
    insertResult = collection.insert_one(offTestData)
    insertedEvent = collection.find_one({"_id": ObjectId(insertResult.inserted_id)})
    eventObj = mongoToJson(insertedEvent)
    enqueueApiCall(apiFunctions.animal_latest.Addevent, {"ident": offTest.ident, "payload":eventObj })
    return eventObj


@subApp.get("/ident/{ident}",     
    description="get event by ident",
    response_model=list[Event],
    responses={400: {"model": Message}},)
@version(1)
async def getEventsByIdent(ident: int) -> list[Event]:
    events = collection.find({"eventData.ident": ident})
    if events is None:
        raise HTTPException( 
            status_code=400,
            detail={"msg": f"No Event found for animal {ident}"},
        )   
    return [mongoToJson(evt) for evt in events]

subApp = VersionedFastAPI(subApp, enable_latest=True)


app= FastAPI()

app.mount('/event', subApp)