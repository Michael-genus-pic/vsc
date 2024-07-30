config = {
    "retryWait": [5, 10, 30, 60, 120, 300, 600, 1800],
    "db": {"url": "mongodb://127.0.0.1:27017/"},
    "apis":{
        "animal": {"url":"http://127.0.0.1:3000"},
        "litter": {"url":"http://127.0.0.1:3001"},
        "notification": {"url":"http://127.0.0.1:3002"},
        "versionv1": {"url":"http://127.0.0.1:3003","version":"v1_0"},
        "versionv2": {"url":"http://127.0.0.1:3003","version":"v2_0"}
    }
}
