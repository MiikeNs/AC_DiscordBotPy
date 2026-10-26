# This example requires the 'message_content' intent.
import discord
import os
import logging
from datetime import datetime
from communityFeatures import welcome
import idconfig

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)


os.makedirs('logs', exist_ok=True)


filename = f"logs/discord_{datetime.now():%Y-%m-%d_%H-%M}.log"
handler = logging.FileHandler(filename=filename, encoding='utf-8', mode='w')




@client.event
async def on_ready():
    guild = client.get_guild(idconfig.GUILD)
    await welcome.welcomeReaction(guild)
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_member_join(member):
    await welcome.welcomeMessage(member)
    await welcome.giveGuestRole(member)
    await welcome.welcomeReaction(member)


client.run(idconfig.TOKEN, log_handler=handler, log_level=logging.INFO)
