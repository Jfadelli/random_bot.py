# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # command_words = [".decide", ".d"]

    # check if user message contains command_words, i.e. .d or .decide
    if message.content == '.d' or '.decide' :
        split_message = message.content.split(", ")

        if ".d " in split_message[0]:
            split_message[0] = split_message[0].replace(".d ","")

        if ".d " in split_message[0]:
            split_message[0] = split_message[0].replace(".decide ","")

        if len(split_message) == 1:
            games = ["CS:GO", "Planetside 2", "PUBG "]
            
        if len(split_message) > 1:
            games = []
            for i in split_message:
                games.append(i)

        response = random.choice(games)
        await message.channel.send(response)    

client.run(TOKEN)