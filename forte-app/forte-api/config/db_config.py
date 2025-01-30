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
    S3_DEV_NAME = os.environ.get('S3_DEV_NAME')
    
    S3_LOCAL_NAME = 'man-local-bucket'
    B3_LOCAL_ACC: 'S3RVER'
    B3_LOCAL_SEC: 'S3RVER'
