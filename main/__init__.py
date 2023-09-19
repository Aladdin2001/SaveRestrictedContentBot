#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 20068224
API_HASH = "0b1fbb5b073d1e086a10c602cc80d913"
BOT_TOKEN = "6504019507:AAGuz-pT7E9KLifiu2FhLkmpR8W274e04cI"
SESSION = "BAEyN4AAG228SLZNUeb2rcxYRgFTzWQWUo678wVBwNga4T6udhd92W9HAgTXtPYxrIoio2mC72iVbPpmjnkYIVF4j3B0JwSB7aN55mqwJOhKjDD8NK7j3I5G2X_CF7JnIcJtl7m-fk-9lJZdoR-Fumjprdon0kfoNbNZtQbkSfgSY3Jg4OdsCXKtoScGkttS2YSvwMe3PPceMJAvuw7cMPfpCcz-PHZSyfUXtdJtAKjJjatPxHVcdEi5ZBZRoXXSZRkPsGjXr0opGEL_BxpaNgSSEQrX1Ljxx9jJWJ5ibAxsd3pTmXdIz45kwxMQ3rEbhAa6Fj54nlSNnS-40CZevGQjCAMcoAAAAAGGMevWAA"
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
