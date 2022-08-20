# helpers.py
# abstraction from main
import time
import datetime

import pause as pause
import pytz


import pandas as pd
from random import randint

import pytz

from iterables import *


# Handles deletion of improper messages
async def delete_wrong_message(message, peek_emoji_dic):
    await message.delete()
    return


# Handles hidden gem (Easter egg) to pigepeek back to the user
# Chance the denominator ( 1 / chance )
async def try_hidden_gem(message, peek_emoji_dic, chance):
    pigepeek_type = message.channel.name

    # Hidden gem (easter egg) to pigepeek back to the user
    min_chance = 1
    max_chance = chance
    result_chance = randint(min_chance, max_chance)
    if result_chance != max_chance:
        return

    # Str = only one type of pigepeek id
    if isinstance(peek_emoji_dic[pigepeek_type], str):
        await message.channel.send(peek_emoji_dic[pigepeek_type])
        return
    elif isinstance(peek_emoji_dic[pigepeek_type], list):
        list_random_pos = randint(0, (len(peek_emoji_dic[pigepeek_type]) - 1))
        await message.channel.send(peek_emoji_dic[pigepeek_type][list_random_pos])
        return

    return


# Checks if the user can pigepeek in this channel
def is_correct_channel_for_pigepeeking(message, peek_emoji_dic):
    if message.channel.name in peek_emoji_dic.keys():
        return True
    return False


def user_is_pigepeeking(message, peek_emoji_dic):
    pigepeek_type = message.channel.name

    if isinstance(peek_emoji_dic[pigepeek_type], list):
        if message.content.strip().lower() in peek_emoji_dic[pigepeek_type]:
            return True
    elif isinstance(peek_emoji_dic[pigepeek_type], str):
        if message.content.strip().lower() == peek_emoji_dic[pigepeek_type]:
            return True
    return False


# Increases the users pigepeeks by one
def increase_pigepeek_count(user_id):
    df = pd.read_csv("pigepeek_counter.csv")

    if user_id not in df.user_id.values:
        # New User
        df_new_user = pd.DataFrame(data=[[user_id, 1]],
                                   columns=['user_id', 'pigepeek_count']).convert_dtypes(convert_integer=True)
        df = pd.concat([df, df_new_user])
        df.to_csv(r'pigepeek_counter.csv', index=False)
    else:
        # Existing User
        query = df.where(df.user_id == user_id).convert_dtypes(convert_integer=True).pigepeek_count

        df.update(query + 1)
        df.to_csv(r'pigepeek_counter.csv', index=False)


# Function called at bot startup
def verify_and_create_csv_file():
    # If file has no header, add file header
    try:
        df = pd.read_csv("pigepeek_counter.csv")
    except (pd.errors.EmptyDataError, FileNotFoundError):
        print('File was empty. New CSV file created')
        df = pd.DataFrame(columns=['user_id', 'pigepeek_count'])
        df.to_csv(r'pigepeek_counter.csv', index=False)
        return

    # Confirming columns are appropriately named
    df = pd.read_csv("pigepeek_counter.csv")
    columns = list(df.columns)
    if columns != ['user_id', 'pigepeek_count']:
        print('Header was changed. Rewriting header')
        df = pd.DataFrame(columns=['user_id', 'pigepeek_count'])
        df.to_csv(r'pigepeek_counter.csv', index=False)
        return


# Should call this at the start of every day, midnight
# Checks if current date is within pigepeek event season. Checks month, then day
def find_ongoing_celebrations():
    # Check between certain times of the year. If not, return
    localtime = time.localtime(time.time())
    day = localtime.tm_mday
    month = localtime.tm_mon
    # Debug test days
    # day = '14'
    # month = '12'
    # pigepeek celebrations currently active
    celebrations = []

    for pigepeek_type in seasonal_dates.keys():
        if month == seasonal_dates[pigepeek_type]['start']['month'] or \
                month == seasonal_dates[pigepeek_type]['end']['month']:
            if int(day) in range(int(seasonal_dates[pigepeek_type]['start']['day']),
                                 int(seasonal_dates[pigepeek_type]['end']['day'])):
                # Cheer the user for the celebration
                pigepeek_cheer(pigepeek_type)
                celebrations.append(pigepeek_type)

    return celebrations


# Archives and unarchives channels
async def process_archives(client):
    # Get a list of all channels that contain the name(s) seasonal_dates.keys()
    # Get their ids in a list
    celebrations = find_ongoing_celebrations()
    channels = client.get_all_channels()
    archive_category_channels = MyDictionary()

    for num_id in archive_ids:
        archive_category_channels.add(client.get_channel(archive_ids[num_id]).name,
                                      client.get_channel(archive_ids[num_id]))

    for i, channel in enumerate(channels):
        if channel.name in seasonal_dates.keys():
            if str(channel.type) == 'text':
                if channel.name in celebrations:
                    # Unarchive channel
                    await channel.move(category=archive_category_channels['pigepeek'],
                                       sync_permissions=True,
                                       beginning=True,
                                       offset=1 + i,
                                       reason='Seasonal event happening')
                else:
                    # Archive channel
                    if channel.category == archive_category_channels['pigepeek']:
                        await channel.move(category=archive_category_channels['pigepeek archive'],
                                           sync_permissions=True,
                                           beginning=True,
                                           offset=i,
                                           reason='Seasonal event not happening')


def pigepeek_cheer(peek_type: str):
    print('♥ ~Celebrating ' + peek_type + '~ ♥')


# Checks if it's the start of a new day
async def wait_for_new_day(discord):
    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)

    midnight = datetime.datetime(
        year=tomorrow.year, month=tomorrow.month, day=tomorrow.day,
        hour=0, minute=0, microsecond=0)

    pause.until(midnight)
    return


class MyDictionary(dict):
    # Function to add key:value
    def add(self, key, value):
        self[key] = value
