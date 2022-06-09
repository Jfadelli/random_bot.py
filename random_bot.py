# bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

def find_command(message):
    command_words = [".decide", ".d"]
    
    for word in message.split(" "):
        if word in command_words:
            return [message.find(word), word]
        else:
            return None

def message_parser(message):
    curr_command = find_command(message)[1]
    curr_list = message.split(", ")
    curr_list[0] = curr_list[0][(len(curr_command)+1)::]
    return curr_list
    
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to Slim\'s Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    response = random.choice(message_parser(message.content))
    await message.channel.send(response)    

client.run(TOKEN)