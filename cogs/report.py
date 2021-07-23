import discord
from discord.ext import commands


class Report(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def report(self, ctx, channel, *, args):
        mod_channel = self.bot.get_channel(863552129163591680)
        embed = discord.Embed(title='Rule Violation Report',
                              description=args, color=0xac545b)
        embed.set_author(name=f'#{channel}')

        await ctx.channel.purge(limit=1)
        await ctx.author.send('anonymous report sent to mods')
        await mod_channel.send(embed=embed)
        await mod_channel.send('<@&806006810200244224>')


def setup(bot):
    bot.add_cog(Report(bot))
