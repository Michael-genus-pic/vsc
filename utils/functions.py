
def mongoToJson(object: object)-> object:
    object["id"] = str(object["_id"])
    del object["_id"]
    return object


