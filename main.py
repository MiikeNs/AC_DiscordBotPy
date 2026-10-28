# This example requires the 'message_content' intent.
import discord
import os
import logging
from datetime import datetime
from discord import app_commands
from eventFeatures import welcome, giveGuestRole, welcomeReaction, applicantStart
from commands import signup
import idconfig

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = discord.Client(intents=intents)

# Slash commands: the list of commands, and the server to register them in
tree = app_commands.CommandTree(bot)
MY_GUILD = discord.Object(id=idconfig.GUILD)

os.makedirs('logs', exist_ok=True)

filename = f"logs/discord_{datetime.now():%Y-%m-%d_%H-%M}.log"
handler = logging.FileHandler(filename=filename, encoding='utf-8', mode='w')


# Runs once at startup: registers the slash commands in your server
async def setup_hook():
    tree.copy_global_to(guild=MY_GUILD)
    await tree.sync(guild=MY_GUILD)

bot.setup_hook = setup_hook


@bot.event
async def on_ready():
    guild = bot.get_guild(idconfig.GUILD)
    await welcomeReaction.welcomeReaction(guild)
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@bot.event
async def on_member_join(member):
    await welcome.welcomeMessage(member)
    await giveGuestRole.giveGuestRole(member)

@bot.event
async def on_raw_reaction_add(payload):
    await applicantStart.applicantRoleAdd(payload)


# Slash commands
@tree.command()
async def ping(interaction: discord.Interaction):
    """Check if the bot is alive."""
    await interaction.response.send_message("pong")

@tree.command(name="signup")
async def signupCommand(interaction: discord.Interaction):
    """Apply to join the unit."""
    await signup.unitSignup(interaction)


bot.run(idconfig.TOKEN, log_handler=handler, log_level=logging.INFO)