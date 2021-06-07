import discord
from discord.ext import commands


class Clear(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    # @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        amount += 1
        await ctx.channel.purge(limit=amount)

    # doesn't work
    @clear.error
    async def clear_error(error, ctx):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have permission to do that!")


def setup(bot):
    bot.add_cog(Clear(bot))
