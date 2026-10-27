import idconfig

async def giveGuestRole(member):
  guestRole = member.guild.get_role(idconfig.GUEST_ROLE)
  memberRoles = member.roles
  if guestRole not in memberRoles :
    await member.add_roles(guestRole)