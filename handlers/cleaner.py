# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚


import os
from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.filters import command, other_filters
from helpers.decorators import sudo_users_only, errors

downloads = os.path.realpath("downloads")
raw_files = os.path.realpath("raw_files")

@Client.on_message(command("rmf") & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("`🗑️𝐇𝐚𝐫𝐥𝐞𝐲 𝐑𝐞𝐦𝐨𝐯𝐞𝐝 𝐚𝐥𝐥 𝐟𝐢𝐥𝐞 𝐟𝐫𝐨𝐦 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝`")
    else:
        await message.reply_text("`𝐍𝐨𝐨𝐛, 𝐍𝐨𝐭𝐡𝐢𝐧𝐠 𝐡𝐞𝐫𝐞 𝐟𝐨𝐫 𝐫𝐞𝐦𝐨𝐯𝐞🙄`")

        
@Client.on_message(command("rmw") & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw_files)
    if ls_dir:
        for file in os.listdir(raw_files):
            os.remove(os.path.join(raw_files, file))
        await message.reply_text("`𝐂𝐥𝐞𝐚𝐧𝐢𝐧𝐠 𝐔𝐩 𝐃𝐁🗑️`")
    else:
        await message.reply_text("`𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐃𝐨𝐧𝐞🙋‍♀️`")


@Client.on_message(command(["dclean"]) & ~filters.edited)
@errors
@sudo_users_only
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("`🧚‍♀️𝐂𝐥𝐞𝐚𝐧 𝐃𝐨𝐧𝐞`")
    else:
        await message.reply_text("`💬𝐍𝐨𝐰, 𝐀𝐥𝐥 𝐨𝐤 𝐚𝐥𝐫𝐞𝐚𝐝𝐲 😌`")
