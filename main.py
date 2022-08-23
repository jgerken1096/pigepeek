# MAIN.py
import os
import discord

from dotenv import load_dotenv

from py_helpers.csv_helpers import verify_and_create_csv_file, increase_emoji_count
from py_helpers.time_helpers import wait_for_new_day, process_archives
from py_helpers.user_helpers import user_already_sent_emoji, delete_wrong_message, try_hidden_gem, \
    is_correct_channel_for_sending_emoji, user_is_sending_correct_emoji, give_default_emoji_role

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

    while True:
        await wait_for_new_day()
        await process_archives(client)


@client.event
async def on_member_join(member):
    # Direct messages
    await member.create_dm()
    await member.dm_channel.send(
        f'Welcome to :pigepeek:, {member.name} :)'
    )

    # Role management
    await give_default_emoji_role(member)


@client.event
async def on_message(message):
    # Making bot not check its own message
    if message.author == client.user:
        return

    # Handles deletion of improper messages, processes hidden gems (easter eggs) and disallows back-to-back pigepeeking
    if is_correct_channel_for_sending_emoji(message):
        if user_is_sending_correct_emoji(message):
            if not await user_already_sent_emoji(message):
                increase_emoji_count(message.author.id)
                await try_hidden_gem(message)
            else:
                await delete_wrong_message(message)
        else:
            await delete_wrong_message(message)
    return


if __name__ == "__main__":
    client.run(TOKEN)
