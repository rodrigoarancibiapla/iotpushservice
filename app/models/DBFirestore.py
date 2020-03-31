import logging
import sys
from google.cloud import firestore

class DBFirestore():
    def __init__(self, params):
        self.params = params
        self.db = firestore.Client()

    def get_config(self, query):
        dat = self.db.collection(self.params['db'])
        response = dat.document(self.params['table']).get().to_dict()[query]
        return response
		