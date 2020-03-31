
import os
from flask import Flask, request, current_app
from app.models import Configuration


appFlask = Flask(__name__)

conf = Configuration.Configuration( {
    "uri": os.environ['STORE_URI_NAME'],
    "db": os.environ['STORE_DATABASE_NAME'],
    "table":os.environ['STORE_TABLE_NAME']
    
})
appFlask.config['PUBSUB_VERIFICATION_TOKEN'] = conf.get_config('PUBSUB_VERIFICATION_TOKEN')
appFlask.config['DATABASE_ENTRIES_PARAMETERS'] =  {
            "uri":conf.get_config('DATABASE_URI'),
            "db":conf.get_config('DATABASE_NAME'),
            "table":conf.get_config('DATABASE_TABLE')
        }


from app.views import  push

