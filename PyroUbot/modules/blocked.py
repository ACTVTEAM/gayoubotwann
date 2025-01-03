from PyroUbot import *
from pyrogram.raw.functions.contacts import GetBlocked

__MODULE__ = "ʙʟᴏᴄᴋᴇᴅ"
__HELP__ = """
<b>-- 📦 Folder Untuk Blocked --</b>

<blockquote><b>🚀 Perintah : <code>{0}unblockall</code>
📝 Penjelasan : mengunblock semua user di daftar contact</b></blockquote>
<blockquote><b>🚀 Perintah : <code>{0}getblock</code>
📝 Penjelasan : melihat jumlah yang di blockir di contact</b></blockquote>
"""

@WANN.UBOT("unblockall")
async def _(user, message):
    sks = await EMO.BERHASIL(user)
    prs = await EMO.PROSES(user)
    _prs = await message.reply(f"{prs}sedang melakukan unblockall...")
    mecha = await user.invoke(GetBlocked(offset=0, limit=100))
    user_ids = [entry.peer_id.user_id for entry in mecha.blocked]
    for x in user_ids:
        try:
            await user.unblock_user(x)
        except:
            pass
    await _prs.edit(f"<blockquote><b>{sks}berhasil melakukan unblockall users</b></blockquote>")

@WANN.UBOT("getblock")
async def _(user, message):
    prs = await EMO.PROSES(user)
    _prs = await message.reply(f"<b>{prs}sedang mengecek...</b>")
    mecha = await user.invoke(GetBlocked(offset=0, limit=100))
    user_ids = [entry.peer_id.user_id for entry in mecha.blocked]
    teko = len(user_ids)
    if user_ids:
        try:
            await _prs.edit(f"<blockquote>kamu memblockir : {teko} users</blockquote>")
        except Exception as i:
            await _prs.edit(f"{i}")
    else:
        await _prs.edit(f"tidak ada yang di blockir")
