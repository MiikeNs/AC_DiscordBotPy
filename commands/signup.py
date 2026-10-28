import idconfig


class SignupModal(idconfig.signupModal):        # 1, 3: top level, distinct name
    async def on_submit(self, interaction):
        await interaction.response.send_message(f'The name is {self.ign.component.value}, age {self.age.component.value}, from {self.country.component.value} and I have {self.hours.component.value} hours.')

async def unitSignup(interaction):
    guestRole = interaction.user.guild.get_role(idconfig.GUEST_ROLE)
    if guestRole in interaction.user.roles:
        modal = SignupModal()                            # 2: the feature version
        await interaction.response.send_modal(modal)     # 4: the one response
    else:
        await interaction.response.send_message(          # 5: the other path's response
            "You need the Guest role to sign up.", ephemeral=True
        )