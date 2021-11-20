from telethon import events, TelegramClient

import re, os, random, asyncio, logging, html

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(name)

APP_ID = os.environ.get("APP_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = TelegramClient("bot", APP_ID, API_HASH).start(bot_token=BOT_TOKEN)

print("Bot started!!")
bot.run_until_disconnected()
