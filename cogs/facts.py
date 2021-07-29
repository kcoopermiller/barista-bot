import discord
from discord.ext import commands
import os
import random


class Facts(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fact(self, ctx, *, args=None):
        if args is not None:
            mod_channel = self.bot.get_channel(863552129163591680)
            embed = discord.Embed(title='New Fact Submission',
                              description=args, color=0xedb76c)
            embed.set_author(name=f'{ctx.message.author}')

            await ctx.channel.purge(limit=1)
            await ctx.author.send('fact sent to mods')
            await mod_channel.send(embed=embed)
            await mod_channel.send('<@&806006810200244224>')
        else: 
            facts = os.listdir(os.path.join(os.path.dirname(os.path.dirname(__file__)), "images/facts"))
            fact = [fact for fact in facts if fact.endswith('.png')]
            await ctx.send(file=discord.File(os.path.join(os.path.dirname(os.path.dirname(__file__)), "images/facts/") + random.choice(fact)))

def setup(bot):
    bot.add_cog(Facts(bot))
