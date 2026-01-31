import asyncio
import importlib
from pyrogram import idle

import config
from config import BANNED_USERS
from ISTKHAR_MUSIC import LOGGER, app, userbot
from ISTKHAR_MUSIC.misc import sudo
from ISTKHAR_MUSIC.plugins import ALL_MODULES
from ISTKHAR_MUSIC.utils.database import get_banned_users, get_gbanned


async def init():
    if not any([
        config.STRING1,
        config.STRING2,
        config.STRING3,
        config.STRING4,
        config.STRING5,
    ]):
        LOGGER(__name__).error("Assistant vars missing, exiting")
        return

    await sudo()

    try:
        for i in await get_gbanned():
            BANNED_USERS.add(i)
        for i in await get_banned_users():
            BANNED_USERS.add(i)
    except:
        pass

    await app.start()

    for module in ALL_MODULES:
        importlib.import_module(f"ISTKHAR_MUSIC.plugins{module}")

    LOGGER("ISTKHAR_MUSIC.plugins").info("Modules Imported")

    await userbot.start()

    LOGGER("ISTKHAR_MUSIC").info("Bot Started Successfully")

    await idle()

    await app.stop()
    await userbot.stop()


if __name__ == "__main__":
    asyncio.run(init())