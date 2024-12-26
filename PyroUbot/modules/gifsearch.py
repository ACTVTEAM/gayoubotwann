import random
from PyroUbot import *
from pyrogram.types import InputMediaPhoto

__MODULE__ = "ɢɪғsᴇᴀʀᴄʜ"
__HELP__ = """
<b>-- 📦 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢɪғsᴇᴀʀᴄʜ --</b>

<blockquote><b>🚀 ᴘᴇʀɪɴᴛᴀʜ :<code>{0}gif</code> [ǫᴜᴇʀʏ]
📝 ᴘᴇɴᴊᴇʟᴀsᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ɢɪꜰᴛ/ᴀɴɪᴍᴀᴛɪᴏɴ ʀᴀɴᴅᴏᴍ ᴅᴀʀɪ ɢᴏᴏɢʟᴇ</b></blockquote>
"""

@WANN.UBOT("gif")
async def gif_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply(f"<code>{message.text}</code> [ǫᴜᴇʀʏ]")
    TM = await message.reply("<b>ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    try:
        x = await client.get_inline_bot_results(
            message.command[0], message.text.split(None, 1)[1]
        )
        saved = await client.send_inline_bot_result(
            client.me.id, x.query_id, x.results[random.randrange(len(x.results))].id
        )
    except:
        await message.reply("<b>❌ ɢɪꜰ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")
        return await TM.delete()
    saved = await client.get_messages(client.me.id, int(saved.updates[1].message.id))
    await client.send_animation(
        message.chat.id, saved.animation.file_id, reply_to_message_id=message.id
    )
    await TM.delete()
    return await saved.delete()
