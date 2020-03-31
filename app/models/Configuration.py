from app.models  import DBFirestore

class Configuration():
    def __init__(self, params):
        self.dbobj=DBFirestore.DBFirestore(params)
        
    def get_config(self, query):
        return self.dbobj.get_config(query)