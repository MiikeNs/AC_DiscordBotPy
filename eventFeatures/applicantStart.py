import idconfig

async def applicantRoleAdd(payload):
  if not payload.member.bot:
    if payload.message_id == idconfig.DEFAULT_MESSAGE :
      if payload.emoji.name == '✅':
        applicantRole = payload.member.guild.get_role(idconfig.APPLICANT_ROLE)
        await payload.member.add_roles(applicantRole)
        channel = payload.member.guild.get_channel(payload.channel_id)
        message = channel.get_partial_message(payload.message_id)
        await message.remove_reaction('✅', payload.member)