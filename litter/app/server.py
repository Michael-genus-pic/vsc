from fastapi import FastAPI, HTTPException

from fastapi_versioning import VersionedFastAPI, version

from pymongo import MongoClient


from bson.objectid import ObjectId

from utils.functions import mongoToJson
from utils.config import config
from utils.apiTypes import Litter, LitterWithLitterMates, Message, RawLitter
import utils.apiFunctions as apiFunctions



subApp = FastAPI(docs_url="/docs", title = 'Litter')
subApp.mongodb_client = MongoClient(config['db']['url'])
db = subApp.mongodb_client.testDB
collection = db.Litter


@subApp.get("/", response_model=list[Litter], responses={404: {"model": Message}})
@version(1)
def getAll() -> list[Litter]:
    littersFound = collection.find({})
    if littersFound:
        return [mongoToJson(litter) for litter in littersFound]
    raise HTTPException(
        status_code=404,
        detail={"msg": f"No Litter Found"},
    )


@subApp.get(
    "/litterId/{litterId}", response_model=Litter, responses={404: {"model": Message}}
)
@version(1)
def getLitterById(litterId: int) -> Litter:
    litterFound = collection.find_one({"litterId": litterId})
    if litterFound:
        return mongoToJson(litterFound)
    raise HTTPException(
        status_code=404,
        detail={"msg": f"Litter not found with litterId {litterId}"},
    )


@subApp.get(
    "/sire/{sire}/dam/{dam}",
    response_model=list[Litter],
    responses={404: {"model": Message}},
)
@version(1)
def getLitterBySireDam(sire: int, dam: int) -> list[Litter]:
    littersFound = list(collection.find({"sire": sire, "dam": dam}))
    if littersFound:
        return [mongoToJson(animal) for animal in littersFound]
    raise HTTPException(
        status_code=404,
        detail={"msg": f"Litter not found with sire {sire} and dam {dam}"},
    )


@subApp.get(
    "/litterMates/litterId/{litterId}",
    response_model=LitterWithLitterMates,
    responses={404: {"model": Message}},
)
@version(1)
def getLitterMatesbyLitterId(litterId: int) -> LitterWithLitterMates:
    try:
        litter = getLitterById(litterId)
        litter["litterMates"] = []
        litter["litterMates"] = apiFunctions.animal_v2_0.Getanimalbylitterid(litterId)
    except Exception as e:
        pass
    return litter


@subApp.post(
    "/",
    name="Add a new Litter",
    description="add a new Litter",
    response_model=Litter,
    responses={400: {"model": Message}, 404: {"model": Message}},
)
@version(1)
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

@subApp.put(
    "/litterId/{litterId}/pigletIdent/{pigletIdent}",
    name="Add piglet to Litter",
    description="add an piglet ident to litter",
    response_model=Litter,
    responses={400: {"model": Message}, 404: {"model": Message}},
)
@version(1)
def addPigletToLitter(litterId: int, pigletIdent: int) -> Litter:
    litter = collection.find_one({"litterId": litterId})
    if litter is None:
        raise HTTPException(
            status_code=404,
            detail={"msg": f"Litter not found with litterId {litterId}"},
        )

    try:
        apiFunctions.animal_latest.Getanimalbyid(pigletIdent)
    except:
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



subApp = VersionedFastAPI(subApp, enable_latest=True)

app= FastAPI()

app.mount('/litter', subApp)