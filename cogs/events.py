import discord
from discord.ext import commands


class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        # this doesn't work
        await self.bot.change_presence(activity=discord.CustomActivity(name='Brewing...'))
        print('Bot activated')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == 822935001082757131:
            guild_id = payload.guild_id
            guild = discord.utils.find(
                lambda g: g.id == guild_id, self.bot.guilds)
            role = None

            if payload.emoji.name == '🟨':
                role = discord.utils.get(guild.roles, name='freshman')
            elif payload.emoji.name == '🟩':
                role = discord.utils.get(guild.roles, name='sophomore')
            elif payload.emoji.name == '🟦':
                role = discord.utils.get(guild.roles, name='junior')
            elif payload.emoji.name == '🟪':
                role = discord.utils.get(guild.roles, name='senior')
            elif payload.emoji.name == '🟥':
                role = discord.utils.get(guild.roles, name='grad student')

            if role is not None:
                member = payload.member
                if member:
                    await member.add_roles(role)

        if message_id == 823064650233020427:
            guild_id = payload.guild_id
            guild = discord.utils.find(
                lambda g: g.id == guild_id, self.bot.guilds)
            role = None

            if payload.emoji.name == '🟨':
                role = discord.utils.get(guild.roles, name='he/him')
            elif payload.emoji.name == '🟩':
                role = discord.utils.get(guild.roles, name='she/her')
            elif payload.emoji.name == '🟦':
                role = discord.utils.get(guild.roles, name='they/them')
            elif payload.emoji.name == '🟪':
                role = discord.utils.get(guild.roles, name='genderfluid')
            elif payload.emoji.name == '🟥':
                role = discord.utils.get(guild.roles, name='multiple pronouns')

            if role is not None:
                member = payload.member
                if member:
                    await member.add_roles(role)


def setup(bot):
    bot.add_cog(Events(bot))
