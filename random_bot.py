# bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

command_words = [".decide", ".d", ".roll", ".r"]

def find_command(message):
    for word in message.split(" "):
        if word in command_words:
            return [message.find(word), word]
        else:
            return [0, "no command"]

def command_parser(message):
    curr_command = find_command(message)[1]

    if curr_command == "no command":
        pass

    elif curr_command == '.d' or curr_command == '.decide':
        return decide_parser(message, curr_command)

    elif curr_command == '.r' or curr_command == '.roll':
        return roll_parser(message)

    else:
        return "no command"

def roll_parser(message):
    message_contents = message.split(" ")
    dice_value = message_contents[1]

    if dice_value[0] == "d":
        dice_value = dice_value[1::]
    roll = random.randint(1,int(dice_value))
    return roll
        
def decide_parser(message, curr_command):
    curr_list = message.split(", ")
    curr_list[0] = curr_list[0][((len(curr_command))+1)::]
    decision = random.choice(curr_list)
    return decision
    
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to Slim\'s Discord server! This bot was coded by Slim, Whooooooa Cool!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    response = command_parser(message.content)

    await message.channel.send(response)    

client.run(TOKEN)