from fastapi import FastAPI, HTTPException

from fastapi_versioning import VersionedFastAPI, version

from pymongo import MongoClient


from bson.objectid import ObjectId

from utils.functions import mongoToJson
from utils.config import config
from utils.apiTypes import Litter, LitterWithLitterMates, Message, RawLitter
import utils.apiFunctions as apiFunctions



app = FastAPI(docs_url="/docs", title = 'Litter')
app.mongodb_client = MongoClient(config['db']['url'])
db = app.mongodb_client.testDB
collection = db.Litter


@app.get(
    "/litterId/{litterId}", response_model=Litter, responses={404: {"model": Message}}
)
def getLitterById(litterId: int) -> Litter:
    litterFound = collection.find_one({"litterId": litterId})
    if litterFound:
        return mongoToJson(litterFound)
    raise HTTPException(
        status_code=404,
        detail={"msg": f"Litter not found with litterId {litterId}"},
    )


@app.get(
    "/sire/{sire}/dam/{dam}",
    response_model=list[Litter],
    responses={404: {"model": Message}},
)
def getLitterBySireDam(sire: int, dam: int) -> list[Litter]:
    littersFound = list(collection.find({"sire": sire, "dam": dam}))
    if littersFound:
        return [mongoToJson(animal) for animal in littersFound]
    raise HTTPException(
        status_code=404,
        detail={"msg": f"Litter not found with sire {sire} and dam {dam}"},
    )


@app.get(
    "/litterMates/litterId/{litterId}",
    response_model=LitterWithLitterMates,
    responses={404: {"model": Message}},
)
def getLitterMatesbyLitterId(litterId: int) -> LitterWithLitterMates:
    try:
        litter = getLitterById(litterId)
        litter["litterMates"] = apiFunctions.animal.Getanimalbylitterid(litterId)
        return litter
    except Exception as e:
        raise e


@app.post(
    "/",
    name="Add a new Litter",
    description="add a new Litter",
    response_model=Litter,
    responses={400: {"model": Message}, 404: {"model": Message}},
)
def addLitter(litter: RawLitter) -> Litter:
    existingLitter = collection.find_one({"litterId": litter.litterId})
    if existingLitter is not None:
        raise HTTPException(
            status_code=404,
            detail={"msg": f"Litter already exists with litterId {litter.litterId}"},
        )
    insertResult = collection.insert_one(litter.model_dump())
    insertedLitter = collection.find_one({"_id": ObjectId(insertResult.inserted_id)})
    return mongoToJson(insertedLitter)

@app.put(
    "/litterId/{litterId}/pigletIdent/{pigletIdent}",
    name="Add piglet to Litter",
    description="add an piglet ident to litter",
    response_model=Litter,
    responses={400: {"model": Message}, 404: {"model": Message}},
)
def addAnimal(litterId: int, pigletIdent: int) -> Litter:
    litter = collection.find_one({"litterId": litterId})
    if litter is None:
        raise HTTPException(
            status_code=404,
            detail={"msg": f"Litter not found with litterId {litterId}"},
        )

    animal = apiFunctions.animal.Getanimalbyid(pigletIdent)
    if animal is None:
        raise HTTPException(
            status_code=400,
            detail={"msg": f"piglet {pigletIdent} not found "},
        )
    if "piglets" not in litter or litter["piglets"] is None:
        litter["piglets"] = []
    if pigletIdent in litter["piglets"]:
        raise HTTPException(
            status_code=400,
            detail={"msg": f"piglet {pigletIdent} already in {litterId}"},
        )
    litter["piglets"].append(pigletIdent)
    collection.update_one(
        {"litterId": litterId}, {"$set": {"piglets": litter["piglets"]}}
    )

    return mongoToJson(litter)
