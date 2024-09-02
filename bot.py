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

@client.event
async def on_message(message):
 #respond to messages from other users, not from the bot
     if message.author == client.user:
         return
 # responds if bot is mentioned in the message
     if client.user in message.mentions:

 #OpenAI API to generate a response to the message
         response = openai.Completion.create(
         engine="text-davinci-002",
         prompt=f"{message.content}",
         max_tokens=100,
         temperature=0,
          )

 # Send the response as a message
     await message.channel.send(response.choices[0].text)

#function call to start the bot
client.run(TOKEN)


