import discord

from discord.ext import commands
from colorama import Fore

intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix='e!')