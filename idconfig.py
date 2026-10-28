import json
import os
from dotenv import load_dotenv
import discord
from discord import ui

with open('ids.json') as f:
  _config = json.load(f)


#CHANNELS-----------------------------------------------------------------
WELCOME_CHANNEL = _config['channels']['welcome_channel_id']


#ROLES-----------------------------------------------------------------

GUEST_ROLE = _config['roles']['guest_role_id']
APPLICANT_ROLE = _config['roles']['applicant_role_id']

#SPECIFIC-----------------------------------------------------------------
DEFAULT_MESSAGE = _config['specific']['default_message_id']
GUILD = _config['specific']['guild_id']


#modals--------------------------------------------------------------------
class signupModal(ui.Modal, title="Signup Form"):
  ign = ui.Label(text='In Game Name', component=ui.TextInput())
  age = ui.Label(text= 'Age', component=ui.TextInput())
  country = ui.Label(text= 'Country', component=ui.TextInput())
  hours = ui.Label(text= 'Hours of Experience', component=ui.TextInput())

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')