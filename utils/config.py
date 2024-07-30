config = {
    "retryWait": [5, 10, 30, 60, 120, 300, 600, 1800],
    "db": {"url": "mongodb://127.0.0.1:27017/"},
    "api_urls":{
        "animal": "http://127.0.0.1:3000",
        "litter": "http://127.0.0.1:3001",
        "notification": "http://127.0.0.1:3002"
    }
}
