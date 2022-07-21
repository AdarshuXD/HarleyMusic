# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚

# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚

import os
from os import path
from pyrogram import Client, filters
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserAlreadyParticipant
from callsmusic import callsmusic, queues
from callsmusic.callsmusic import client as USER
from helpers.admins import get_administrators
import requests
import aiohttp
from youtube_search import YoutubeSearch
import converter
from downloaders import youtube
from config import DURATION_LIMIT
from helpers.filters import command
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
import aiofiles
import ffmpeg
from PIL import Image, ImageFont, ImageDraw
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream


def transcode(filename):
    ffmpeg.input(filename).output("input.raw", format='s16le', acodec='pcm_s16le', ac=2, ar='48k').overwrite_output().run() 
    os.remove(filename)

# Convert seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


# Change image size
def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

async def generate_cover(requested_by, title, views, duration, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    
    image1 = Image.open("./background.png")
    image2 = Image.open("etc/hypermusic.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("temp.png")
    img = Image.open("temp.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("etc/hyper2.otf", 30)
    draw.text((190, 550), f"Title: {title}", (255, 255, 255), font=font)
    draw.text(
(190, 590), f"Duration: {duration}", (255, 255, 255), font=font
    )
    draw.text((190, 630), f"Views: {views}", (255, 255, 255), font=font)
    draw.text((190, 670),
 f"Added By: {requested_by}",
 (255, 255, 255),
 font=font,
    )
    img.save("final.png")
    os.remove("temp.png")
    os.remove("background.png")

@Client.on_callback_query()
def close(Client, callback: CallbackQuery):
    if callback.data == "Close":
        callback.message.delete()

@Client.on_message(
    command(["ytp", "play"])
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def play(_, message: Message):
    global que
    global useer
    await message.delete()
    usrid = message.from_user.mention

    lel = await message.reply("🕺")

    administrators = await get_administrators(message.chat)
    chid = message.chat.id

    try:
        user = await USER.get_me()
    except:
        user.first_name = "HarleyXAssistant"
    usar = user
    wew = usar.id
    try:
        await _.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message.from_user.id:
                try:
                    invitelink = await _.export_chat_invite_link(chid)
                except:
                    await lel.edit(
                        "<b><i>𝐁𝐚𝐛𝐲 𝐦𝐚𝐤𝐞 𝐦𝐞 𝐀𝐝𝐦𝐢𝐧 𝐟𝐢𝐫𝐬𝐭 𝐟𝐨𝐫 𝐩𝐥𝐚𝐲 𝐦𝐮𝐬𝐢𝐜 🙋‍♀️🥀</i></b>")
                    return

                try:
                    await USER.join_chat(invitelink)
                    await USER.send_message(
                        message.chat.id, "𝐇𝐚𝐫𝐥𝐞𝐲 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐢𝐬 𝐣𝐨𝐢𝐧 𝐢𝐧 𝐭𝐡𝐢𝐬 𝐛𝐚𝐛𝐲🧚‍♀️🥀")

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    await lel.edit(
                        f"<b><i>𝐔𝐧𝐚𝐛𝐥𝐞 𝐭𝐨 𝐩𝐥𝐚𝐲 𝐛𝐚𝐛𝐲😕, 𝐌𝐚𝐤𝐞 𝐬𝐮𝐫𝐞 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐢𝐬 𝐧𝐨𝐭 𝐛𝐚𝐧 𝐢𝐧 𝐭𝐡𝐢𝐬 𝐠𝐫𝐨𝐮𝐩🤷‍♀️</i></b>")
    
    try:
        await USER.get_chat(chid)
    except:
        await lel.edit(
            f"<i><b>ᴏᴏᴘs sᴏʀʀʏ {user.first_name}, ᴀssɪsᴛᴀɴᴛ ɪᴢ ɴᴏᴛ ɪɴ ᴛʜɪs ᴄʜᴀᴛ ᴘʟɪsʜ ᴛᴇʟʟ ʏᴏᴜʀ ᴀᴅᴍɪɴs ᴜsᴇ /joinub ᴄᴏᴍᴀɴᴅ ʙᴇғᴏʀᴇ ᴘʟᴀʏ sᴏɴɢs💁‍♂️</b></i>")
        return
    
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)
    
    if audio:
        if round(audio.duration / 360) > DURATION_LIMIT:
            raise DurationLimitError(
                f"**𝐒𝐨𝐫𝐫𝐲 𝐆𝐢𝐯𝐞𝐧 𝐐𝐮𝐞𝐫𝐲 𝐢𝐬 𝐧𝐨 𝐥𝐨𝐧𝐠𝐞𝐫 𝐭𝐡𝐚𝐧 {DURATION_LIMIT} 𝐒𝐨 𝐀𝐫𝐞𝐧'𝐭 𝐚𝐥𝐥𝐨𝐰 𝐭𝐨 𝐩𝐥𝐚𝐲 𝐝𝐮𝐞 𝐭𝐨 𝐡𝐞𝐚𝐯𝐲 𝐮𝐬𝐚𝐠𝐞😕🤷‍♀️**"
            )

        file_name = get_file_name(audio)
        title = file_name
        thumb_name = "https://te.legra.ph/file/3f22c82379ea73b4a7967.jpg"
        thumbnail = thumb_name
        duration = round(audio.duration / 60)
        views = "Locally added"

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                            text="Enjoy🥀",
                            url=f"https://t.me/"),
                    InlineKeyboardButton(
                            text="Update👾",
                            url=f"https://t.me/"),
               ],
               [
                   InlineKeyboardButton(text="Close Menu", callback_data="close_"),                   
               ],
            ]
        )
    
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name))
            else file_name
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

            keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                            text="Enjoy🥀",
                            url=f"https://t.me/SILENT_DEVS"),
                    InlineKeyboardButton(
                            text="Update👾",
                            url=f"https://t.me/"),
               ],
               [
                   InlineKeyboardButton(text="Close Menu", callback_data="close_"),                   
               ],
            ]
        )
    
        except Exception as e:
            title = "NaN"
            thumb_name = "https://te.legra.ph/file/3f22c82379ea73b4a7967.jpg"
            duration = "NaN"
            views = "NaN"
            keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                            text="Enjoy🥀",
                            url=f"https://t.me/"),
                    InlineKeyboardButton(
                            text="Update👾",
                            url=f"https://t.me/"),
               ],
               [
                   InlineKeyboardButton(text="Close Menu", callback_data="close_"),                   
               ],
            ]
        )
    
        if (dur / 360) > DURATION_LIMIT:
            await lel.edit(
                f"**𝐒𝐨𝐫𝐫𝐲 𝐆𝐢𝐯𝐞𝐧 𝐐𝐮𝐞𝐫𝐲 𝐢𝐬 𝐧𝐨 𝐥𝐨𝐧𝐠𝐞𝐫 𝐭𝐡𝐚𝐧 {DURATION_LIMIT} 𝐒𝐨 𝐀𝐫𝐞𝐧'𝐭 𝐚𝐥𝐥𝐨𝐰 𝐭𝐨 𝐩𝐥𝐚𝐲 𝐝𝐮𝐞 𝐭𝐨 𝐡𝐞𝐚𝐯𝐲 𝐮𝐬𝐚𝐠𝐞😕🤷‍♀️**"
            )
            return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
            return await lel.edit(
                "𝐔𝐬𝐚𝐠𝐞:-\n `/ytp` ᴏʀ `/play` 𝐒𝐨𝐧𝐠 𝐍𝐚𝐦𝐞 | 𝐘𝐓 𝐥𝐢𝐧𝐤 | 𝐓𝐆 𝐀𝐮𝐝𝐢𝐨 𝐟𝐢𝐥𝐞 🙋‍♀️"
            )
        await lel.edit("Processing Your Query....")
        query = message.text.split(None, 1)[1]
        # print(query)
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            await lel.edit(
                "**🤷𝐧𝐭𝐠 𝐈 𝐠𝐨𝐭 𝐩𝐥𝐳 𝐜𝐡𝐞𝐜𝐤 𝐲𝐨𝐮𝐫 𝐪𝐮𝐞𝐫𝐲 𝐭𝐡𝐞𝐧 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧🧚‍♀️.**"
            )
            print(str(e))
            return

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                            text="Enjoy🥀",
                            url=f"https://t.me/"),
                    InlineKeyboardButton(
                            text="Update👾",
                            url=f"https://t.me/"),
               ],
               [
                   InlineKeyboardButton(text="Close Menu", callback_data="close_"),                   
               ],               
            ]
        )
    
        if (dur / 60) > DURATION_LIMIT:
            await lel.edit(
                f"**𝐒𝐨𝐫𝐫𝐲 𝐆𝐢𝐯𝐞𝐧 𝐐𝐮𝐞𝐫𝐲 𝐢𝐬 𝐧𝐨 𝐥𝐨𝐧𝐠𝐞𝐫 𝐭𝐡𝐚𝐧 {DURATION_LIMIT} 𝐒𝐨 𝐀𝐫𝐞𝐧'𝐭 𝐚𝐥𝐥𝐨𝐰 𝐭𝐨 𝐩𝐥𝐚𝐲 𝐝𝐮𝐞 𝐭𝐨 𝐡𝐞𝐚𝐯𝐲 𝐮𝐬𝐚𝐠𝐞😕🤷‍♀️**"
            )
            return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(youtube.download(url))
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) in ACTV_CALLS:
        position = await queues.put(chat_id, file=file_path)      
        await message.reply_photo(
            photo="final.png",
            caption="****𝐍𝐨𝐰, 𝐘𝐨𝐮𝐫 𝐒𝐨𝐧𝐠 𝐢𝐬 𝐪𝐮𝐞𝐮𝐞𝐝 𝐢𝐧 𝐥𝐢𝐬𝐭🥀💖 \n\n𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐝 𝐛𝐲: {}𝐁𝐚𝐛𝐲 🥀 \n𝐏𝐨𝐬𝐢𝐭𝐢𝐨𝐧:-** {}**".format(usrid, position),
            reply_markup=keyboard,
        )
        await message.delete()
    
    else:
        await callsmusic.pytgcalls.join_group_call(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )

        await message.reply_photo(
            photo="final.png",
            reply_markup=keyboard,
            caption="**𝐍𝐨𝐰, 𝐈'𝐦 𝐩𝐥𝐚𝐲𝐢𝐧𝐠 𝐲𝐨𝐮𝐫 𝐐𝐮𝐞𝐮𝐞𝐝 𝐒𝐨𝐧𝐠💖🧚‍♀️.\n\n𝐏𝐥𝐚𝐲𝐢𝐧𝐠 𝐚𝐭🧚‍♀️ :- `{}`...**\n𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐝 𝐛𝐲 : {}𝐁𝐚𝐛𝐲🥀".format(
        message.chat.title, usrid
        ), )
        
    
    os.remove("final.png")
    return await lel.delete()
