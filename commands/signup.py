import idconfig
import discord

class SignupModal(idconfig.signupModal):        # 1, 3: top level, distinct name
    async def on_submit(self, interaction):
        
        embed = discord.Embed(title = f"Application form of {interaction.user.global_name}", colour= discord.Colour.from_str("#FFFF00"))
        embed.add_field(name="Name & Age: ", value= self.name_age.component.value, inline=False)
        embed.add_field(name="Country: ", value=self.country.component.value, inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name="Hours of Experience: ", value=self.hours.component.value, inline=True)
        if "mic" in self.micEnglish.component.values:
            embed.add_field(name="Microphone: ", value="Yes", inline=True)

        if "english" in self.micEnglish.component.values:
            embed.add_field(name="English speaker: ", value="Yes", inline=True)
        embed.add_field(name="Where they found the Unit: ", value=self.howFound.component.value, inline=False)

        recruitmentChannel = interaction.user.guild.get_channel(idconfig.RECRUITMENT_CHANNEL)
        await recruitmentChannel.send(embed= embed)
        await interaction.response.send_message(f'Signup form submitted, {interaction.user.global_name} a recruiter will get in touch soon.', ephemeral=True)

async def unitSignup(interaction):
    guestRole = interaction.user.guild.get_role(idconfig.GUEST_ROLE)
    if guestRole in interaction.user.roles:
        modal = SignupModal()                            # 2: the feature version
        await interaction.response.send_modal(modal)     # 4: the one response
    else:
        await interaction.response.send_message(          # 5: the other path's response
            "You need the Guest role to sign up.", ephemeral=True
        )