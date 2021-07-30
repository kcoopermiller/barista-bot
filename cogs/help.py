import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, command=None):
        if command is not None:
            match command:
                case 'fact':
                    embed = discord.Embed(title='**Fact Command**', description="Fact", color=0x36393f)
                    await ctx.send(embed=embed)
                case 'help':
                    embed = discord.Embed(title='**Help Command**', description="bruh", color=0x36393f)
                    await ctx.send(embed=embed)
                case 'ill':
                    embed = discord.Embed(title='**Illini Command**', description="ILL\nNI!", color=0x36393f)
                    await ctx.send(embed=embed)
                case 'pain':
                    embed = discord.Embed(title='**Pain Command**', description="pain peko", color=0x36393f)
                    await ctx.send(embed=embed)
                case 'report':
                    embed = discord.Embed(title='**Report Command**', description="report", color=0x36393f)
                    await ctx.send(embed=embed)
        else:
            commands = '''
**Available Commands:**
.fact
.help
.ill
.pain
.report

Type `.help [command]` for more information
            '''
            embed = discord.Embed(title='**Help**', description=commands, color=0x36393f)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
