import discord

from discord.ext import commands
from colorama import Fore
from useful import load_data, save_data

settings = load_data("../settings")

intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix=settings.get("prefixes"))

if __name__ == "__main__":
    bot.run(settings.get("token"))