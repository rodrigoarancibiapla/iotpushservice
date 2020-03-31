from app.models  import DBMongo

class DBEntries():
    def __init__(self, params):
        self.dbobj=DBMongo.DBMongo(params)
    def put_entry(self, data):
        self.dbobj.put_entry(data)