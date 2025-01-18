import pymongo


class MongoDb:

    def __init__(self, mongo_config):

        self.client = None
        self.db = None

        try:
            self.client = pymongo.MongoClient(mongo_config.URL)
            self.db = self.client[mongo_config.MONGO_NAME]

        except Exception as exception:
            print(f"Error: {exception}")

    def __del__(self):
        if self.client is not None:
            self.client.close()

    def set_collection(self, db_collection):
        self.collection = self.db[db_collection]

    def insert(self, data):
        try:
            txn_id = self.collection.insert_one(data).inserted_id
            print(f"Data inserted with ID: {txn_id}")

        except pymongo.errors.DuplicateKeyError as error:
            print(f"Error: {error}")
            return 0

        except Exception as exception:
            print(f"Error: {exception}")
            return -1

        return txn_id

    def fetch_one(self, query):
        data = self.collection.find_one(query)
        return data

    def fetch_all(self, query):
        data = self.collection.find(query)
        return data

    def update_one(self, filter_by, data):
        data = self.collection.update_one(filter_by, {"$set": data}, upsert=False)
        return data
