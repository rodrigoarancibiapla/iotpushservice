import base64
import json
import sys
import google.cloud.logging
client = google.cloud.logging.Client()
client.setup_logging()
import logging
from app import appFlask as myapp

from app import request, current_app
from app.models import DBEntries

@myapp.route('/pubsub/push', methods=['POST'])
def pubsub_push():
      
    if (request.args.get('token', '') ==None):
       return 'Invalid request, token not exists', 400
    if (request.args.get('token', '')!=current_app.config['PUBSUB_VERIFICATION_TOKEN']):
       return 'Invalid request, toekn invalid', 400

    dbparams=current_app.config['DATABASE_ENTRIES_PARAMETERS']
    envelope = json.loads(request.data.decode('utf-8'))
    print(envelope)
    payload = base64.b64decode(envelope['message']['data'])
    print((payload))
    logging.info("storing " + payload.decode("utf-8") + " in " + json.dumps(dbparams))

    entryObj = DBEntries.DBEntries(dbparams)

    try:
       entryObj.put_entry(json.loads(payload))
       return 'OK', 200
    except:
       logging.error("ERR" + str(sys.exc_info()[1]))
       return "ERR  " + str(sys.exc_info()[1]),500
    