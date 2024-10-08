
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson.objectid import ObjectId
from fastapi_versioning import VersionedFastAPI, version

from utils.functions import mongoToJson
from utils.enqueueFunctions import enqueueApiCall
from utils.apiTypes import Animal, Message, RawAnimal, Event
from utils.config import config
import utils.apiFunctions as apiFunctions



subApp = FastAPI(docs_url="/docs", title = 'Animal')
subApp.mongodb_client = MongoClient(config['db']['url'])
db = subApp.mongodb_client.testDB
collection = db.Animal



@subApp.get(
    "/",
    description="find all animal",
    response_model=list[Animal],
    responses={404: {"model": Message}},
)
@version(1)
def getAll() -> list[Animal]:
    animalsFound = list(collection.find({}))
    if animalsFound:
        return [mongoToJson(animal) for animal in animalsFound]
    raise HTTPException(
        status_code=404,
        detail={"msg": "No Animal Found"},
    )



@subApp.get(
    "/ident/{animalIdent}",
    description="find the single animal with litter id",
    response_model=Animal,
    responses={404: {"model": Message}},
)
@version(1)
def getAnimalById(animalIdent: int) -> Animal:
    animalFound = collection.find_one({"ident": animalIdent})
    if animalFound:
        return mongoToJson(animalFound)
    raise HTTPException(
        status_code=404,
        detail={"msg": f"Animal not found with ident {animalIdent}"},
    )


@subApp.get(
    "/litterId/{litterId}",
    description="find all the animals with litter id",
    response_model=list[Animal],
    responses={404: {"model": Message}},
)
@version(1)
def getAnimalByLitterId(litterId: int) -> list[Animal]:
    animalsFound = list(collection.find({"litterId": litterId}))
    if animalsFound:
        return [mongoToJson(animal) for animal in animalsFound]
    raise HTTPException(
        status_code=404,
        detail={"msg": f"Animals not found with litterId {litterId}"},
    )

@subApp.post(
    "/",
    description="Insert a new Animal",
    response_model=Animal,
    responses={400: {"model": Message}},
)
@version(1)
def addAnimal(animal: RawAnimal) -> Animal:
    existingAnimal = collection.find_one({"ident": animal.ident})
    if existingAnimal is not None:
        raise HTTPException(
            status_code=400,
            detail={"msg": f"Animal already exists with ident {animal.ident}"},
        )
    insertResult = collection.insert_one(animal.model_dump())
    insertedAnimal = collection.find_one({"_id": ObjectId(insertResult.inserted_id)})
    return mongoToJson(insertedAnimal)




@subApp.post(
    "/",
    description="Insert a new Animal",
    response_model=Animal,
    responses={400: {"model": Message}},
)
@version(2)
def addAnimal(animal: RawAnimal) -> Animal:
    existingAnimal = collection.find_one({"ident": animal.ident})
    if existingAnimal is not None:
        raise HTTPException(
            status_code=400,
            detail={"msg": f"Animal already exists with ident {animal.ident}"},
        )
    insertResult = collection.insert_one(animal.model_dump())
    insertedAnimal = collection.find_one({"_id": ObjectId(insertResult.inserted_id)})
    enqueueApiCall(apiFunctions.litter_v1_0.AddPigletToLitter, {"litterId":insertedAnimal['litterId'], "pigletIdent": insertedAnimal['ident']})
    return mongoToJson(insertedAnimal)



@subApp.put(
    "/addEvent/{ident}",
    description="add event to animal",
    response_model=Animal,
    responses={400: {"model": Message}},
)
@version(2)
def addEvent(ident: int, event: Event) -> Animal:
    print (ident, event)
    existingAnimal = collection.find_one({"ident": ident})
    if existingAnimal is  None:
        raise HTTPException(
            status_code=400,
            detail={"msg": f"Animal not found with ident {ident}"},
        )
    if 'events' not in existingAnimal or existingAnimal['events'] is None:
        existingAnimal['events'] = []
    existingAnimal['events'].append(event.model_dump())
    
    eventList = existingAnimal['events']
    collection.update_one({"ident": ident}, {"$set": {"events": eventList}})
    updatedAnimal = collection.find_one({"ident": ident})
    return mongoToJson(updatedAnimal)
    

subApp = VersionedFastAPI(subApp, enable_latest=True)

app= FastAPI()

app.mount('/animal', subApp)