from PyroUbot import *

__MODULE__ = "ᴀɴɪᴍᴇ"
__HELP__ = """
<b>-- 📦 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀɴɪᴍᴇ --</b>

<blockquote><b>🚀 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}wall</code></blockquote>
<blockquote><b>🚀 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}waifu</code></blockquote>
<blockquote><b>📝 ᴘᴇɴᴊᴇʟᴀsᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘʜᴏᴛᴏ ᴀɴɪᴍᴇ ʀᴀɴᴅᴏᴍ</b></blockquote>
"""


@WANN.UBOT("wall|waifu")
async def anime_cmd(client, message):
    msg = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ</b>", quote=True)
    if message.command[0] == "wall":
        photo = await API.wall(client)
        try:
            await photo.copy(message.chat.id, reply_to_message_id=message.id)
            return await msg.delete()
        except Exception as error:
            return await msg.edit(error)
    elif message.command[0] == "waifu":
        photo = API.waifu()
        try:
            await message.reply_photo(photo, quote=True)
            return await msg.delete()
        except Exception as error:
            return await msg.edit(error)
