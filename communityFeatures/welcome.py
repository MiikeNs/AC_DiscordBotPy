import idconfig
import discord

async def welcomeMessage(member):
  welcomeChannel = member.guild.get_channel(idconfig.WELCOME_CHANNEL)
  await welcomeChannel.send(f"Welcome to Athena Company {member.mention} Discord Server, feel free to look around the server, get to know our unit through videos.")

async def giveGuestRole(member):
  guestRole = member.guild.get_role(idconfig.GUEST_ROLE)
  memberRoles = member.roles
  if guestRole not in memberRoles :
    await member.add_roles(guestRole)

async def welcomeReaction(member):
  welcomeChannel = member.guild.get_channel(idconfig.WELCOME_CHANNEL)

  try:
    defaultMessage = await welcomeChannel.fetch_message(idconfig.DEFAULT_MESSAGE)
    await welcomeChannel.send("Found the message!")
  except discord.NotFound:
    await welcomeChannel.send("No dice!")
 