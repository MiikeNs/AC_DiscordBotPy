import idconfig

async def welcomeReaction(guild):
  welcomeChannel = guild.get_channel(idconfig.WELCOME_CHANNEL)
  defaultMessage = await welcomeChannel.fetch_message(idconfig.DEFAULT_MESSAGE)
  botReacted = False
  for reaction in defaultMessage.reactions:
      if reaction.emoji == "✅" and reaction.me:
          botReacted = True

  if not botReacted:
      await defaultMessage.add_reaction("✅")