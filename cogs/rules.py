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
            title='**Welcome to the UIUC Coffee Club!**', color=0xfff8e7)
        # embed.set_thumbnail(url=thumbnail)
        embed.add_field(name=('**Rules**'),
                        value=rules, inline=False)
        embed.add_field(name='**Reporting Rule Violations**',
                        value=violations, inline=False)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Rules(bot))
