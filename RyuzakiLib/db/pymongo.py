from pymongo import MongoClient


class MongoConnect:
    def __init__(self, mongo_url=None, client=None, database=None):
        self.mongo_url = mongo_url
        self.client = client
        self.database = database

    def get_collection(self, mongodb_dev: bool = None):
        if mongodb_dev:
            client_mongo = MongoClient(self.mongo_url)
            db = client_mongo[self.client][self.database]
            return db[self.collection_name]
        else:
            client_mongo = MongoClient(self.mongo_url)
            db = client_mongo["tiktokbot"]["ryuzakilib"]
            return db[self.collection_name]
