# MAIN.py
import os
import discord

from dotenv import load_dotenv
from helpers import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.messages = True
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    verify_and_create_csv_file()

    #while True:
        #await wait_for_new_day(discord)
        #await process_archives(client)


@client.event
async def on_member_join(member):
    # Direct messages
    await member.create_dm()
    await member.dm_channel.send(
        f'Welcome to :pigepeek:, {member.name} :)'
    )

    # Role management
    await give_pigepeek_role(member)


@client.event
async def on_message(message):
    # Making bot not check its own message
    if message.author == client.user:
        return

    # Handles deletion of improper messages, processes hidden gems (easter eggs) and disallows back-to-back pigepeeking
    if is_correct_channel_for_pigepeeking(message):
        if user_is_pigepeeking(message):
            if not await user_already_pigepeeked(message):
                increase_pigepeek_count(message.author.id)
                await try_hidden_gem(message, 3)
            else:
                await delete_wrong_message(message)
        else:
            await delete_wrong_message(message)
    return


if __name__ == "__main__":
    client.run(TOKEN)
