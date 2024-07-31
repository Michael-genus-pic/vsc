config = {
    # "retryWait": [5, 10, 30, 60, 120, 300, 600, 1800],
    "retryWait": [5, 5,5,5,5,5,5,5,5],
    "db": {"url": "mongodb://127.0.0.1:27017/"},
    "apis":{
        "animal": {"url":"http://127.0.0.1:3000"},
        "litter": {"url":"http://127.0.0.1:3001"},
        "notification": {"url":"http://127.0.0.1:3002"},
        "versioning": {"url":"http://127.0.0.1:3003"}
    }
}
