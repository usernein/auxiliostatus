import re

from pyrogram import Client, Filters
from pyromod.helpers import ikb

@Client.on_message(Filters.regex(r'^(?P<cpf>([\._\-]*[0-9][\._\-]*){11})|(?P<code>\w+)$'))
async def on_query(client, message, lang):
    cpf = re.sub(r'\D', '', message.matches[0]['cpf'])
    code = message.matches[0]['code']
    
    await message.reply(str([cpf, code]))