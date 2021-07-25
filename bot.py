import discord
import os
from discord.ext import commands
import os
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='.')

for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)
