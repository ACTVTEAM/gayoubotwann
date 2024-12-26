import asyncio
import io
import os

import cv2
import requests
from pyrogram import raw

from PyroUbot import *

__MODULE__ = "ʀᴇᴍᴏᴠᴇʙɢ"
__HELP__ = """
<b>-- 📦 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʀᴇᴍᴏᴠᴇʙɢ --</b>

<blockquote><b>🚀 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}rmbg</code> [ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ]
📝 ᴘᴇɴᴊᴇʟᴀsᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ʟᴀᴛᴀʀ ʙᴇʟᴀᴋᴀɴɢ ɢᴀᴍʙᴀʀ</b></blockquote>
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

@WANN.UBOT("rmbg")
async def rbg_cmd(client, message):
    if RMBG_API is None:
        return
    if message.reply_to_message:
        reply_message = message.reply_to_message
        xx = await message.reply("<i>ᴍᴇᴍᴘʀᴏsᴇs...</i>")
        try:
            if (
                isinstance(reply_message.media, raw.types.MessageMediaPhoto)
                or reply_message.media
            ):
                downloaded_file_name = await client.download_media(
                    reply_message, "./downloads/"
                )
                await xx.edit("<i>ᴍᴇɴɢʜᴀᴘᴜs ʟᴀᴛᴀʀ ʙᴇʟᴀᴋᴀɴɢ ᴅᴀʀɪ ɢᴀᴍʙᴀʀ ɪɴɪ...</i>")
                output_file_name = await ReTrieveFile(downloaded_file_name)
                os.remove(downloaded_file_name)
            else:
                await xx.edit("<i>ʙᴀɢᴀɪᴍᴀɴᴀ ᴄᴀʀᴀ ᴍᴇɴɢʜᴀᴘᴜs ʟᴀᴛᴀʀ ʙᴇʟᴀᴋᴀɴɢ ɪɴɪ ?</i>")
        except Exception as e:
            await xx.edit(f"{(str(e))}")
            return
        contentType = output_file_name.headers.get("content-type")
        if "image" in contentType:
            with io.BytesIO(output_file_name.content) as remove_bg_image:
                remove_bg_image.name = "rbg.png"
                await client.send_document(
                    message.chat.id,
                    document=remove_bg_image,
                    force_document=True,
                    reply_to_message_id=message.id,
                )
                await xx.delete()
        else:
            await xx.edit(
                "<b>ᴋᴇsᴀʟᴀʜᴀɴ (ᴋᴜɴᴄɪ ᴀᴘɪ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ, sᴀʏᴀ ᴋɪʀᴀ ?)</b>\n<i>{}</i>".format(
                    output_file_name.content.decode("UTF-8")
                ),
            )
    else:
        return await message.reply("sɪʟᴀʜᴋᴀɴ ʙᴀʟᴀs ᴋᴇ ɢᴀᴍʙᴀʀ")