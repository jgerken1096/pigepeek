# MAIN.py
import os
import discord

from dotenv import load_dotenv
from helpers import *
from iterables import pigepeek_emoji_ids_dic

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    verify_and_create_csv_file()

    while True:
        await wait_for_new_day(discord)
        await process_archives(client)


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
    if is_correct_channel_for_pigepeeking(message):
        if user_is_pigepeeking(message):
            increase_pigepeek_count(message.author.id)
            await try_hidden_gem(message, 3)
        else:
            await delete_wrong_message(message,)
    return


if __name__ == "__main__":
    client.run(TOKEN)
