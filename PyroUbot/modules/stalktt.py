import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "ꜱᴛᴀʟᴋᴛᴛ"
__HELP__ = """
<b>-- 📦 ꜱᴛᴀʟᴋᴛᴛ --</b>

<blockquote><b>🚀 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}stalktt</code> 
<i>📝 Penjelasan : untuk stalk tiktok menggunakan username</i></b></blockquote>
"""

@WANN.UBOT("stalktt")
async def stalktt(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"{prs} Processing...")
    
    if len(message.command) != 2:
        return await jalan.edit(f"{ggl} Please use the command `stalktt` followed by the tiktok username.")
    
    username = message.command[1]
    chat_id = message.chat.id
    url = f"https://widipe.com/download/tiktokstalk?username={username}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            hasil = data['result']
            username = hasil['username']
            description = hasil['description']
            likes = hasil['likes']
            followers = hasil['followers']
            following = hasil['following']
            totalPosts = hasil['totalPosts']
            photoUrl = hasil['profile']
            caption = f"""
<b><emoji id=5841235769728962577>⭐</emoji>Username: <code>{username}</code></b>
<b><emoji id=5843952899184398024>⭐</emoji>Description: <code>{description}</code></b>
<b><emoji id=5841243255856960314>⭐</emoji>Likes: <code>{likes}</code></b>
<b><emoji id=5352566966454330504>⭐</emoji>Followers: <code>{followers}</code></b>
<b><emoji id=5353036831581544549>⭐</emoji>Following: <code>{following}</code></b>
<b><emoji id=5841243255856960314>⭐</emoji>TotalPosts: <code>{totalPosts}</code></b>
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
