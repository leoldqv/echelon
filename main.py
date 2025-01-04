import discord
import asyncio
import shutil
import sys
import os

from discord.ext import commands
from colorama import Fore
from useful import load_data, save_data

settings = load_data("../settings")

intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix=settings.get("prefixes"))

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def print_centered(s: str):
    print(s.center(shutil.get_terminal_size().columns))

@bot.event
async def on_ready():
    clear_console()
    #print_centered()

if __name__ == "__main__":
    bot.run(settings.get("token"))