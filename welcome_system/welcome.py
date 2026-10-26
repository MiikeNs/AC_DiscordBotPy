import idconfig

async def on_join(member):
  welcomeChannel = member.guild.get_channel.WELCOME_CHANNEL
  await welcomeChannel.send("Welcome to Athena Comapny Discord Server, feel free to look around the server, get to know our unit through videos.")