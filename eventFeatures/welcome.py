import idconfig

async def welcomeMessage(member):
  welcomeChannel = member.guild.get_channel(idconfig.WELCOME_CHANNEL)
  await welcomeChannel.send(f"Welcome to Athena Company {member.mention} Discord Server, feel free to look around the server, get to know our unit through videos.")

