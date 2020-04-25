import constructors
from pyrogram import Client, Filters

@Client.on_callback_query(Filters.callback_data('start'))
async def onstart(client, query, lang):
    text, keyboard = constructors.start(query, lang)
    
    await query.edit(text, reply_markup=keyboard, disable_web_page_preview=True)
    await query.answer()