#important modules
import os
import discord as dc
import openai
from dotenv import load_dotenv

#Bot token and openai API for AI chat
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_KEY = os.getenv('OPENAI_KEY')

# Set up the OpenAI API client
openai.api_key = OPENAI_KEY

#used for future modications, if we add commands to bot
intents = dc.Intents.all( )
client = dc.Client(command_prefix='!', intents=intents)

#gives confirmation when bot in started
@client.event
async def on_ready():
    print('Bot is online ._.')


