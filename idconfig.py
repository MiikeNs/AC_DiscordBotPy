import json
import os
from dotenv import load_dotenv
import discord
from discord import ui

with open('ids.json') as f:
  _config = json.load(f)


#CHANNELS-----------------------------------------------------------------
WELCOME_CHANNEL = _config['channels']['welcome_channel_id']
RECRUITMENT_CHANNEL = _config['channels']['recruitment_channel_id']

#ROLES-----------------------------------------------------------------

GUEST_ROLE = _config['roles']['guest_role_id']
APPLICANT_ROLE = _config['roles']['applicant_role_id']

#SPECIFIC-----------------------------------------------------------------
DEFAULT_MESSAGE = _config['specific']['default_message_id']
GUILD = _config['specific']['guild_id']


#modals--------------------------------------------------------------------
class signupModal(ui.Modal, title="Signup Form"):
  name_age = ui.Label(text='Username', component=ui.TextInput(placeholder="Username, age"))
  country = ui.Label(text= 'Country', component=ui.TextInput(placeholder="Country where you live."))
  hours = ui.Label(text= 'Hours of Experience', component=ui.TextInput(placeholder="How many hours (aproximately) you have in experience."))
  micEnglish = ui.Label(text="Requirements", component=ui.CheckboxGroup(required=True, options= [discord.CheckboxGroupOption(label="Working microphone", value="mic" ,default=False), discord.CheckboxGroupOption(label="Speak English", value="english" ,default=False)] ))
  howFound = ui.Label(text= 'How did you find Athena Company', component=ui.TextInput(placeholder="Reddit, Discord, Friend or otherwhise."))




load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')