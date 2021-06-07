import discord
from discord.ext import commands


class Illini(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ill(self, ctx):
        await ctx.send('ini!')


def setup(bot):
    bot.add_cog(Illini(bot))
