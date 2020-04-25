import asyncio
import base64
import json
import os
import yaml

from dotenv import load_dotenv
from langs import Langs

from pyromod import listen, filters
from pyrogram import Client

# Load variables on .env to os.environ
load_dotenv()

def tryint(value):
    try:
        return int(value)
    except:
        return value
def b64encode(value:str):
    return base64.b64encode(value.encode()).decode()
def b64decode(value:str):
    return base64.b64decode(value.encode()).decode()

required_env_vars = ['LOGS_CHAT', 'SUDOERS_LIST', 'DATABASE_URL']
for required in required_env_vars:
    if required not in os.environ:
        raise AttributeError(f'Missing required env variable: {required}')
    if not os.getenv(required):
        raise ValueError(f'Invalid value for required env variable {required}')

# Extra **kwargs for creating pyrogram.Client
pyrogram_config = os.getenv('PYROGRAM_CONFIG') or b64encode('{}')
pyrogram_config = b64decode(pyrogram_config)
pyrogram_config = json.loads(pyrogram_config)

app = Client(os.getenv('PYROGRAM_SESSION') or 'bot', plugins={"root":"plugins"}, **pyrogram_config)
app.set_parse_mode('html')

with open('./strings/ptbr.yml') as ptfp:
    langs = Langs(
        escape_html=True,
        ptbr=yaml.safe_load(ptfp),
    )
    
logs_chat = tryint(os.getenv('LOGS_CHAT'))
sudoers = list(map(tryint, os.getenv('SUDOERS_LIST').split(' ')))
