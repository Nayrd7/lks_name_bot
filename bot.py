import disnake
from disnake.ext import commands

import os
from dotenv import load_dotenv

from pathlib import Path

import config.config as cfg

load_dotenv(dotenv_path='config/bot_token.env')

intents = disnake.Intents.all()

bot = commands.Bot(command_prefix=cfg.bot_prefix, help_command=None, intents=intents)


@bot.event()
async def on_ready():
    print(f'Bot - {bot.user.name}#{bot.user.discriminator} - is ready to work!')

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot.run(BOT_TOKEN)
