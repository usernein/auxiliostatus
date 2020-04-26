import json
import re

from pyrogram import Client, Filters
from pyromod.helpers import ikb

import auxilio

@Client.on_message(Filters.regex(r'^(?P<cpf>([\._\-]*[0-9][\._\-]*){11})\|(?P<code>\w+)$'))
async def on_query(client, message, lang):
    cpf = re.sub(r'\D', '', message.matches[0]['cpf'])
    code = message.matches[0]['code']
    
    if not auxilio.valid_cpf(cpf):
        return await message.reply(lang.error_invalid_cpf)
    
    try:
        status = auxilio.status(cpf, code)
        await message.reply('<code>'+json.dumps(status, indent=4)+'</code>')
    except auxilio.InvalidCode:
        await message.reply('Código inválido ou expirado.')
    except auxilio.InvalidResponse as e:
        await message.reply(f'Ocorreu um erro com a resposta da API: {e}')