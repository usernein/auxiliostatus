from pyrogram import Client, Filters
from pyromod.helpers import ikb

@Client.on_message(Filters.command('help'))
async def onhelp(client, message, lang):
    await message.reply(lang.help_text, disable_web_page_preview=True)