import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('ODA2MDAxMTkyMjk5NTI4MTky.YBjFGw.aLvLAgQtNb1h98eDstiJ68rzGHA')
# will not run without token
