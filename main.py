# MAIN.py / BOT

import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Welcome to :pigepeek:, {member.name}. :)'
    )

@client.event
async def on_message(message):
    # Making bot not check its own message
    if message.author == client.user:
        return

    # Potentially could instead make the bot list all the server emojis id's and store them in a list
    # List of acceptable pigepeek emojis
    pigepeek_emoji_ids = [
        '<:pigepeek:940345904664305675>',
        '<:pigepeek:883177483204177960>'
    ]

    # If not :pigepeek:ing
    if message.content.strip().lower() not in pigepeek_emoji_ids:
        await message.delete()

    # If :pigepeek:ing
    if message.content.strip().lower() not in pigepeek_emoji_ids:
        # Easter egg to pigepeek back
        min_chance = 1
        max_chance = 1500
        result_chance = random.randint(min_chance, max_chance)
        if result_chance == max_chance:
            await message.channel.send('<:pigepeek:940345904664305675>')
    return

client.run(TOKEN)
