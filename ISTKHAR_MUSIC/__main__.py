import asyncio
import importlib
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from ISTKHAR_MUSIC import LOGGER, app, userbot
from ISTKHAR_MUSIC.core.call import Call
from ISTKHAR_MUSIC.misc import sudo
from ISTKHAR_MUSIC.plugins import ALL_MODULES
from ISTKHAR_MUSIC.utils.database import get_banned_users, get_gbanned


noor = Call()


async def init():
    if not any(
        [
            config.STRING1,
            config.STRING2,
            config.STRING3,
            config.STRING4,
            config.STRING5,
        ]
    ):
        LOGGER(__name__).error(
            "Assistant client variables not defined, exiting..."
        )
        return

    await sudo()

    try:
        for user_id in await get_gbanned():
            BANNED_USERS.add(user_id)
        for user_id in await get_banned_users():
            BANNED_USERS.add(user_id)
    except Exception as e:
        LOGGER(__name__).warning(e)

    await app.start()

    for module in ALL_MODULES:
        importlib.import_module(f"ISTKHAR_MUSIC.plugins{module}")

    LOGGER("ISTKHAR_MUSIC.plugins").info("Successfully Imported Modules...")

    await userbot.start()
    await noor.start()

    try:
        await noor.stream_call(
            "https://graph.org/file/e999c40cb700e7c684b75.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("ISTKHAR_MUSIC").error(
            "Please turn on the videochat of your log group/channel.\nStopping Bot..."
        )
        return
    except Exception:
        pass

    await noor.decorators()

    LOGGER("ISTKHAR_MUSIC").info("Istkhar Music Bot Started Successfully")

    await idle()

    await app.stop()
    await userbot.stop()
    LOGGER("ISTKHAR_MUSIC").info("Stopping Istkhar Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())