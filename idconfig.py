import json

with open('ids.json') as f:
  _config = json.load(f)

welcomeChannel = _config['welcome_channel_id']
TOKEN = _config['tokenID']