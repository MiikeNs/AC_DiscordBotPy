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

async def welcomeReaction(guild):
  welcomeChannel = guild.get_channel(idconfig.WELCOME_CHANNEL)
  defaultMessage = await welcomeChannel.fetch_message(idconfig.DEFAULT_MESSAGE)
  botReacted = False
  for reaction in defaultMessage.reactions:
      if reaction.emoji == "✅" and reaction.me:
          botReacted = True

  if not botReacted:
      await defaultMessage.add_reaction("✅")