import auxilio
import html
import json
import re

from pyrogram import Client, Filters
from pyromod.helpers import ikb

@Client.on_message(Filters.regex(r'^(?P<cpf>([\._\-]*[0-9][\._\-]*){11})\|(?P<code>\w+)$'))
async def on_query(client, message, lang):
    cpf = re.sub(r'\D', '', message.matches[0]['cpf'])
    code = message.matches[0]['code']
    
    if not auxilio.valid_cpf(cpf):
        return await message.reply(lang.error_invalid_cpf)
    
    try:
        status = auxilio.status(cpf, code)
        try:
            await message.reply(lang.status_result(status=status))
        finally:
            await message.reply(f'<code>{html.escape(json.dumps(status, indent=4))}</code>')
    except auxilio.InvalidCode as e:
        await message.reply(lang.error_invalid_code(error=e.api_response))
    except auxilio.InvalidCPF as e:
        await message.reply(lang.error_invalid_cpf(error=e.api_response))
    except auxilio.InvalidResponse as e:
        await message.reply(lang.error_invalid_response(error=e.api_response))