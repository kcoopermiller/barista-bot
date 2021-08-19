import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, command=None):
        commands = '''
**Available Commands:**
.fact
.help
.ill
.pain
.report

Type `.help [command]` for more information
        '''
        if command is not None:
            if command == 'fact':
                description = '''
.fact 
- display random coffee fact
.fact [new fact] 
- submit new fact for approval. if approved, the fact will be added to the list
                '''
                embed = discord.Embed(title='**Fact Command**', description=description, color=0x36393f)
                await ctx.send(embed=embed)
            elif command == 'help':
                embed = discord.Embed(title='**Help Command**', description=commands, color=0x36393f)
                await ctx.send(embed=embed)
            elif command =='ill':
                embed = discord.Embed(title='**Illini Command**', description=".ill\n- ni!", color=0x36393f)
                await ctx.send(embed=embed)
            elif command == 'pain':
                embed = discord.Embed(title='**Pain Command**', description="pain peko", color=0x36393f)
                await ctx.send(embed=embed)
            elif command == 'report':
                description = '''
.report [channel to look at] [message explaining incident]
- reports will be automatically deleted and sent anonymously to a mod
                '''
                embed = discord.Embed(title='**Report Command**', description=description, color=0x36393f)
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title='**Help**', description=commands, color=0x36393f)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
