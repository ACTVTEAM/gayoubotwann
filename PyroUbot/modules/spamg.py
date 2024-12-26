import asyncio

from pyrogram.enums import ChatType
from pyrogram.errors import FloodWait

from .. import *
from PyroUbot import *

__MODULE__ = "ꜱᴘᴀᴍ"
__HELP__ = """
<b>-- 📦 Folder bantuan spam --</b>

<blockquote><b>🚀 Perintah : <code>{0}spam</code>
📝 Penjelasan : <code>melakukan spam pesan</code></b></blockquote>
<blockquote><b>🚀 Perintah : <code>{0}setdelay</code>
📝 Penjelasan : <code>mengatur delay setiap pesan yang di kirim</code></b></blockquote>
<blockquote><b>🚀 Perintah : <code>{0}stopspam</code>
📝 Penjelasan : <code>memberhentikan spam pesan yang sedang berjalan</code></b></blockquote>
"""

spam_progress = []

async def SpamMsg(client, message, send):
    delay = await get_vars(client.me.id, "SPAM") or 0
    await asyncio.sleep(int(delay))
    if message.reply_to_message:
        await send.copy(message.chat.id)
    else:
        await client.send_message(message.chat.id, f"{send}\n\n<b>-- Powered By @XyroOfficiall --</b>")

@WANN.UBOT("spam")
@WANN.TOP_CMD
async def _(client, message):
    global spam_progress
    spam_progress.append(client.me.id)
    sks = await EMO.BERHASIL(client)
    _msg = "<b>memproses...</b>"

    r = await message.reply(_msg)
    count, msg = extract_type_and_msg(message)

    try:
        count = int(count)
    except Exception:
        return await r.edit(f"<b><code>{message.text.split()[0]}</code> [jumlah] [text/reply_msg]</b>")

    if not msg:
        return await r.edit(
            f"<b><code>{message.text.split()[0]}</code> [jumlah] [text/reply_msg]</b>"
        )
    
    for _ in range(count):
        if client.me.id not in spam_progress:
            await r.edit(f"<blockquote><b>proses spam berhasil di batalkan !</b> {sks}</blockquote>")
            return
        await SpamMsg(client, message, msg)

    spam_progress.remove(client.me.id)    
    await r.edit("<b>spam telah selesai</b>")

@WANN.UBOT("setdelay")
@WANN.TOP_CMD
async def _(client, message):
    _msg = "<b>memproses...</b>"

    r = await message.reply(_msg)
    count, msg = extract_type_and_msg(message)

    try:
        count = int(count)
    except Exception:
        return await r.edit(f"<b><code>{message.text.split()[0]}</code> [count]</b>")

    if not count:
        return await r.edit(f"<b><code>{message.text.split()[0]}</code> [count]</b>")

    await set_vars(client.me.id, "SPAM", count)
    return await r.edit("<b>spam delay berhasil di setting</b>")

@WANN.UBOT("stopspam")
@WANN.TOP_CMD
async def _(client, message):
    global spam_progress
    if client.me.id in spam_progress:
        spam_progress.remove(client.me.id)
        await message.reply("<b>spam telah berhenti</b>")
    else:
        await message.reply("<b>tidak ada spam yang ditemukan</b>")