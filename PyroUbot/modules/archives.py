from PyroUbot.core.helpers.tools import get_data_id
from PyroUbot import *
__MODULE__ = "ᴀʀᴄʜɪᴠᴇ"
__HELP__ = """
<b>-- 📦 Folder Untuk Archive --</b>

<blockquote><b>🚀 Perintah : <code>{0}arch</code>
📝 Penjelasan : mengarchivekan group chat pribadi maupun channel</b></blockquote>
<blockquote><b> 🚀 Perintah : <code>{0}unarch</code>
📝 Penjelasan : mengunarchivekan group chat pribadi maupun channel</b></blockquote>
"""
@WANN.UBOT("arch")
@WANN.TOP_CMD
async def archive_user(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if len(message.command) <2:
        return await message.reply(f"<blockquote><b>{ggl}mohon gunakan arch all, users, group</b></blockquote>")
    anjai = await message.reply(f"{prs}proccesing...")
    anjir = message.command[1]
    xx = await get_data_id(client, anjir)
    for anu in xx:
        await client.archive_chats(anu)
    
    await anjai.edit(f"<b>{brhsl}berhasil mengarchivekan semua {anjir}</b>")

@WANN.UBOT("unarch")
@WANN.TOP_CMD
async def unarchive_user(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if len(message.command) <2:
        return await message.reply(f"{ggl}mohon gunakan arch all, users, group")
    anjai = await message.reply(f"{prs}proccesing...")
    anjir = message.command[1]
    xx = await get_data_id(client, anjir)
    for anu in xx:
        await client.unarchive_chats(anu)
    await anjai.edit(f"<blockquote><b>{brhsl}berhasil mengunarchivekan semua {anjir}</b></blockquote>")
