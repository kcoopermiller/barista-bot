from discord.ext import commands
import os
from dotenv import load_dotenv
import discord

intents = discord.Intents.all()


bot = commands.Bot(command_prefix='.', help_command=None, intents=intents)

client = discord.Client(intents=intents)

for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)
