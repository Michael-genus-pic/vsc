from utils.addresses import hostAddress, mongoServerAddress

hostName = hostAddress

config = {
    "retryWait": [5, 10, 30, 60, 120, 300, 600, 1800],
    "db": {"url": f"mongodb://{mongoServerAddress}:27017/"},
    "apis":{
        "animal": {"port": 3000},
        "litter": {"port": 3001},
        "notification": {"port": 3002},
        "versioning": {"port": 3003}
    }
}
