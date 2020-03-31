import sys
from pymongo import MongoClient
from app.models.IDBEntries import IDBEntries 

import logging

class DBMongo(IDBEntries):
    def __init__(self, params):
        self.params = params
    def put_entry(self, data):
        try:
            client = MongoClient(self.params['uri'])
            db = client[self.params['db']]
            collection = db[self.params['table']]
        
            collection.insert_one(data)
        except:
            print("error inseting " + str(sys.exc_info()[1]))
            raise Exception(str(sys.exc_info()[1]))
        