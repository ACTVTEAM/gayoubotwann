from PyroUbot import *

__MODULE__ = "ɢᴀᴍᴇ"
__HELP__ = """
<b>-- 📦 Folder Untuk Game --</b>

<blockquote><b>🚀 Perintah : <code>{0}catur</code>
📝 Penjelasan : untuk memunculkan game catur</b></blockquote>
<blockquote><b>🚀 Perintah : <code>{0}game</code>
📝 Penjelasan : untuk memunculkan game random</b></blockquote>

<blockquote><b>⚠️Note: jumlah menu game 500+</b></blockquote>
"""


@WANN.UBOT("catur")
@WANN.TOP_CMD
async def _(client, message):
    try:
        x = await client.get_inline_bot_results("GameFactoryBot")
        msg = message.reply_to_message or message
        await client.send_inline_bot_result(
            message.chat.id, x.query_id, x.results[0].id, reply_to_message_id=msg.id
        )
    except Exception as error:
        await message.reply(error)


@WANN.UBOT("game")
@WANN.TOP_CMD
async def game_cmd(client, message):
    try:
        x = await client.get_inline_bot_results("gamee")
        msg = message.reply_to_message or message
        random_index = random.randint(0, len(x.results) - 1)
        await client.send_inline_bot_result(
            message.chat.id, x.query_id, x.results[random_index].id, reply_to_message_id=msg.id
        )
    except Exception as error:
        await message.reply(error)
