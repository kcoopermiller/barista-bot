import discord
from discord.ext import commands
import os
import random


class Facts(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fact(self, ctx):
        facts = os.listdir(os.path.join(os.path.dirname(os.path.dirname(__file__)), "images/facts"))
        fact = [fact for fact in facts if fact.endswith('.png')]
        await ctx.send(file=discord.File(os.path.join(os.path.dirname(os.path.dirname(__file__)), "images/facts/") + random.choice(fact)))

def setup(bot):
    bot.add_cog(Facts(bot))
