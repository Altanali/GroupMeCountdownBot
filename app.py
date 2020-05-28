import os
import json

from urllib.parse import urlencode
from urllib.request import  Request, urlopen

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()

  # We don't want to reply to ourselves!
  if data['name'] != 'apnorton-test-bot':
    msg = '{}, you sent "{}".'.format(data['name'], data['text'])
    send_message(msg)

  return "ok", 200

# {
#   "attachments": [],
#   "avatar_url": "https://i.groupme.com/750x1000.jpeg.a6bd93ffed43420493af7116ab1515c8",
#   "created_at": 1302623328,
#   "group_id": "59969540",
#   "id": "1234567890",
#   "name": "John",
#   "sender_id": "12345",
#   "sender_type": "user",
#   "source_guid": "GUID",
#   "system": False,
#   "text": "Hello world ☃☃",
#   "user_id": "1234567890"
# }

def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id' : os.getenv('GROUPME_BOT_ID'),
        'text' : msg,
        }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read.decode()
