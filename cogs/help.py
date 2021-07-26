import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        commands = '''
        **Available Commands:**
        .facts
        .help
        .ill
        .pain
        .report
        '''
        embed = discord.Embed(title='**Help**', description=commands, color=0x36393f)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
