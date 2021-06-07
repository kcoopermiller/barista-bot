import discord
from discord.ext import commands
import os, random

class Facts(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fact(self, ctx):
        await ctx.send(file=discord.File(os.path.join(os.path.dirname(__file__), 
            "../images/facts/" + random.choice(os.listdir(os.path.join(os.path.dirname(__file__), "../images/facts"))))))


def setup(bot):
    bot.add_cog(Facts(bot))

    