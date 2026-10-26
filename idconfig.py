import json
import os
from dotenv import load_dotenv

with open('ids.json') as f:
  _config = json.load(f)

WELCOME_CHANNEL = _config['channels']['welcome_channel_id']


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')