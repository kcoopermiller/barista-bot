import discord
from discord.ext import commands
import os
from pathlib import Path


class Rules(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rules(self, channel):
        channel = self.bot.get_channel(849147102252761118)

        rules = '''
1️⃣ Be kind
2️⃣ Uphold [UIUC's non-discrimination policies](https://cam.illinois.edu/policies/hr-48)
3️⃣ Limit NSFW content to marked channels (#shitposts, #gaming and #weebs)
4️⃣ Don't spam
5️⃣ Don't ask for mod privileges
6️⃣ Advertisements are prohibited, unless otherwise approved by a mod
        '''
        rules_img_path = f"{os.path.dirname(os.path.dirname(__file__))}/images/rules.png"
        violations = '''
Please report rule violations by typing:
``` /report [channel to look at] [message explaining incident] ```
into any channel. Your message will be automatically deleted and an anonymous report will be sent to a @moderator
        '''

        embed = discord.Embed(
            title='**Welcome to the UIUC Coffee Club!**', color=0x36393f)
        # embed.add_thumbnail(url='')
        # embed.set_image(url='')

        embed_rules = discord.Embed(description=rules, color=0x36393f)
        embed_rules.set_author(name="Rules")
        embed_rules.add_field(name=' **Reporting Rule Violations**',
                              value=violations, inline=False)

        invite_link = 'https://discord.gg/RcZKvUMDdt'

        await channel.send(embed=embed)
        await channel.send(embed=embed_rules)
        await channel.send(invite_link)


def setup(bot):
    bot.add_cog(Rules(bot))
