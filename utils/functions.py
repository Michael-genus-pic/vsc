import requests

def mongoToJson(object):
    object["id"] = str(object["_id"])
    del object["_id"]
    return object


def getApiResponse(url, default=None):
    result = default
    try:
        response = requests.get(url)
        if response.status_code  != 200:
            return result
        result = response.json()
    except requests.exceptions.RequestException:
        pass
    return result
