from discord.ext import commands
import time


class Clear(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx, amount=10):
        if ctx.message.author.guild_permissions.administrator:
            await ctx.channel.purge(limit=amount+1)
        else:
            ctx.send("Cannot clear due to insufficient permissions")
            time.sleep(2)
            await ctx.channel.purge(limit=1)


def setup(bot):
    bot.add_cog(Clear(bot))
