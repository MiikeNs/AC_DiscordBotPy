import json
import os
from dotenv import load_dotenv

with open('ids.json') as f:
  _config = json.load(f)


#CHANNELS-----------------------------------------------------------------
WELCOME_CHANNEL = _config['channels']['welcome_channel_id']


#ROLES-----------------------------------------------------------------

GUEST_ROLE = _config['roles']['guest_role_id']

#SPECIFIC-----------------------------------------------------------------
DEFAULT_MESSAGE = _config['specific']['default_message_id']
GUILD = _config['specific']['guild_id']

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')