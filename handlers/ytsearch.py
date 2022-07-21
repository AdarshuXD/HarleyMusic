# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚

# the logging things
import logging

from pyrogram.types import Message
from search_engine_parser import GoogleSearch
from youtube_search import YoutubeSearch

from pyrogram import Client as app, filters

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

import pyrogram

logging.getLogger("pyrogram").setLevel(logging.WARNING)

@app.on_message(pyrogram.filters.command(["search"]))
async def ytsearch(_, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("/search ǫᴜᴇʀʏ!")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("𝐇𝐚𝐫𝐥𝐞𝐲 𝐬𝐞𝐚𝐫𝐜𝐡𝐢𝐧𝐠 𝐟𝐫𝐨𝐦 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞....")
        results = YoutubeSearch(query, max_results=4).to_dict()
        i = 0
        text = ""
        while i < 4:
            text += f"🥀𝗧𝗶𝘁𝗹𝗲 - {results[i]['title']}\n"
            text += f"👩‍💻𝗗𝘂𝗿𝗮𝘁𝗶𝗼𝗻 - {results[i]['duration']}\n"
            text += f"💬𝗩𝗶𝗲𝘄𝘀- {results[i]['views']}\n"
            text += f"💥𝗖𝗵𝗮𝗻𝗻𝗲𝗹 - {results[i]['channel']}\n"
            text += f"https://youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(str(e))
