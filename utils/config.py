
hostName = "192.168.0.233"
config = {
    # "retryWait": [5, 10, 30, 60, 120, 300, 600, 1800],
    "retryWait": [5, 5,5,5,5,5,5,5,5],
    "db": {"url": f"mongodb://{hostName}:27017/"},
    "apis":{
        "animal": {"url":f"http://{hostName}/animal"},
        "litter": {"url":f"http://{hostName}/litter"},
        "notification": {"url":f"http://{hostName}/notification"},
        "versioning": {"url":f"http://{hostName}/versioning"}
    }
}
