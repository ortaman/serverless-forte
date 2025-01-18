import os

class MongoConfig:

    MONGO_NAME = os.environ['MONGO_NAME']

    MONGO_USER = os.environ['MONGO_USER']
    MONGO_PASS = os.environ['MONGO_PASS']
    MONGO_HOST = os.environ['MONGO_HOST']

    MONGO_COLLECT_NAME = os.environ['MONGO_COLLECT_NAME']

    URL = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:27017"
