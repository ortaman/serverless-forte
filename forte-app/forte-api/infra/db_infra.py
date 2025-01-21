import os

class MongoConfig:

    MONGO_NAME = os.environ['MONGO_NAME']

    MONGO_USER = os.environ['MONGO_USER']
    MONGO_PASS = os.environ['MONGO_PASS']
    MONGO_HOST = os.environ['MONGO_HOST']

    MONGO_DEFAULT_COLLECTION = os.environ['MONGO_DEFAULT_COLLECTION']

    URL = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:27017"
    
    ATLAS_URI = f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@forte-db.i98y0.mongodb.net/?retryWrites=true&w=majority&appName=forte-db"


class BotoSettings:
    S3_NAME = os.environ.get('S3_NAME')
    ACC = os.environ.get('B3_ACC')
    SEC = os.environ.get('B3_SEC')
