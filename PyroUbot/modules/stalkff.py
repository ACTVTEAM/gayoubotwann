import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "ꜱᴛᴀʟᴋꜰꜰ"
__HELP__ = """
<b>-- 📦 ꜱᴛᴀʟᴋꜰꜰ --</b>

<blockquote><b>🚀 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}stalkff</code> 
<i>📝 Penjelasan : search akun ff menggunakan id</i></b></blockquote>
"""

@WANN.UBOT("stalkff")
async def stalkff(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"{prs} Processing...")
    
    if len(message.command) != 2:
        return await jalan.edit(f"{ggl} Please use the command `stalkff` id akun.")
    
    id = message.command[1]
    chat_id = message.chat.id
    url = f"https://ff.lxonfire.workers.dev/?id={id}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            Nicname = data['nickname']
            region = data['region']
            openid = data['open_id']
            photoUrl = data['img_url']
            caption = f"""
<b><emoji id=5841235769728962577>⭐</emoji>Nicname: <code>{Nicname}</code></b>
<b><emoji id=5843952899184398024>⭐</emoji>Region: <code>{region}</code></b>
<b><emoji id=5841243255856960314>⭐</emoji>OpenID: <code>{openid}</code></b>
"""
            photo_path = wget.download(photoUrl)
            await client.send_photo(chat_id, caption=caption, photo=photo_path)
            if os.path.exists(photo_path):
                os.remove(photo_path)
            
            await jalan.delete()
        else:
            await jalan.edit(f"{ggl} No 'result' key found in the response.")
    
    except requests.exceptions.RequestException as e:
        await jalan.edit(f"{ggl} Request failed: {e}")
    
    except Exception as e:
        await jalan.edit(f"{ggl} An error occurred: {e}")
