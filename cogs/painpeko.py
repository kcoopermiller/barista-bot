import discord
from discord.ext import commands
import os


class PainPeko(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pain(self, ctx):
        await ctx.send(file=discord.File(os.path.dirname(os.path.dirname(__file__)) + '/images/painpeko.jpeg'))


def setup(bot):
    bot.add_cog(PainPeko(bot))
