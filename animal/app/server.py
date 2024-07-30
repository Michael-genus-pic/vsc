from typing import Union

from fastapi import FastAPI, HTTPException

from pymongo import MongoClient

from utils.functions import mongoToJson

from utils.apiTypes import Animal, Message, RawAnimal

from bson.objectid import ObjectId

from utils.config import config

from mongo_queue.queue import Queue

import utils.apiFunctions as apiFunctions

from fastapi_versioning import VersionedFastAPI, version

app = FastAPI(docs_url="/docs")
app.mongodb_client = MongoClient(config['db']['url'])
db = app.mongodb_client.testDB
collection = db.Animal

app = VersionedFastAPI(app)

queue = Queue( MongoClient(config['db']['url']).testDB.queue, consumer_id="consumer1",  timeout=300, max_attempts=len(config['retryWait']))

@app.get(
    "/ident/{animalIdent}",
    name="Get Animal By ident",
    description="find the single animal with litter id",
    response_model=Animal,
    responses={404: {"model": Message}},
)
def getAnimalById(animalIdent: int) -> Animal:
    animalFound = collection.find_one({"ident": animalIdent})
    if animalFound:
        return mongoToJson(animalFound)
    raise HTTPException(
        status_code=404,
        detail={"msg": f"Animal not found with ident {animalIdent}"},
    )


@app.get(
    "/litterId/{litterId}",
    description="find all the animals with litter id",
    response_model=list[Animal],
    responses={404: {"model": Message}},
)
def getAnimalByLitterId(litterId: int) -> list[Animal]:
    animalsFound = list(collection.find({"litterId": litterId}))
    if animalsFound:
        return [mongoToJson(animal) for animal in animalsFound]
    raise HTTPException(
        status_code=404,
        detail={"msg": f"Animals not found with litterId {litterId}"},
    )


@app.post(
    "/",
    name="New Animal",
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
    payload = {
        "destination": 'litter', 
        "function": "AddPigletToLitter",
        "params":{"litterId":insertedAnimal['litterId'], "pigletIdent": insertedAnimal['ident']},
        }
    queue.put(payload)  
    return mongoToJson(insertedAnimal)
