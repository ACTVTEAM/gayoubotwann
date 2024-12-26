import asyncio
import io
import os

import cv2
import requests
from pyrogram import raw

from PyroUbot import *

__MODULE__ = "ʙʟᴜʀ"
__HELP__ = """
<b>-- 📦 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙʟᴜʀ --</b>

<blockquote><b>🚀 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}blur</code> [ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ]
📝 ᴘᴇɴᴊᴇʟᴀsᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʀɪᴋᴀ ᴇꜰᴇᴋ ʙʟᴜʀ ᴋᴇ ɢᴀᴍʙᴀʀ</b></blockquote>
"""


async def ReTrieveFile(input_file_name):
    headers = {
        "X-API-Key": RMBG_API,
    }
    files = {
        "image_file": (input_file_name, open(input_file_name, "rb")),
    }
    return requests.post(
        "https://api.remove.bg/v1.0/removebg",
        headers=headers,
        files=files,
        allow_redirects=True,
        stream=True,
    )

@WANN.UBOT("blur")
async def blur_cmd(client, message):
    ureply = message.reply_to_message
    xd = await message.reply("<i>ᴍᴇᴍᴘʀᴏsᴇs...</i>")
    if not ureply:
        return await xd.edit("ʙᴀʟᴀs ᴋᴇ ɢᴀᴍʙᴀʀ")
    yinsxd = await client.download_media(ureply, "./downloads/")
    if yinsxd.endswith(".tgs"):
        cmd = ["lottie_convert.py", yinsxd, "yin.png"]
        file = "yin.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        img = cv2.VideoCapture(yinsxd)
        heh, lol = img.read()
        cv2.imwrite("yin.png", lol)
        file = "yin.png"
    yin = cv2.imread(file)
    ayiinxd = cv2.GaussianBlur(yin, (35, 35), 0)
    cv2.imwrite("yin.jpg", ayiinxd)
    await client.send_photo(
        message.chat.id,
        "yin.jpg",
        reply_to_message_id=message.id,
    )
    await xd.delete()
    os.remove("yin.png")
    os.remove("yin.jpg")
    os.remove(yinsxd)
