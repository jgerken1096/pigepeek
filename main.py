# MAIN.py / BOT

import os

import discord

from dotenv import load_dotenv
from helpers import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    verify_and_create_csv_file()
    # check date

    channels = client.get_all_channels()


    # check_to_process_archives(channels)


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

    # Handles deletion of improper messages and processes hidden gems (easter eggs)
    if is_correct_channel_for_pigepeeking(message, pigepeek_emoji_ids_dic):
        if user_is_pigepeeking(message, pigepeek_emoji_ids_dic):
            increase_pigepeek_count(message.author.id)
            await try_hidden_gem(message, pigepeek_emoji_ids_dic, 3)
        else:
            await delete_wrong_message(message, pigepeek_emoji_ids_dic)

    return


client.run(TOKEN)
