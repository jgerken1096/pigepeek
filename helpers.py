# helpers.py
# abstraction from main
import pandas as pd
import time

from random import randint

# Lists and Dictionaries
# Pigepeek Test Emoji '<:pigepeek:940345904664305675>'
# Pigepeek Main Server Emojis
# Potentially could instead make the bot list all the server emojis id's and store them in a list
pigepeek_emoji_ids = [
    '<:pigepeek:940345904664305675>',
    '<:pigepeek:883177483204177960>',
    '<:pigepeek:888604853402755122>',
    '<:pigepeek:888604861548072960>',
    '<:pigepeek:888604870209331232>',
    '<:pigepeek:888604876601446421>',
    '<:pigepeek:888604883266187305>',
    '<:pigepeek:888604888764915782>',
    '<:pigepeek:888604897229037578>',
    '<:pigepeek:888604903969284147>',
    '<:pigepeek:888604909233131561>',
    '<:pigepeek:888604915377786891>',
    '<:pigepeek:888604921811845162>',
    '<:pigepeek:888604926975045642>',
    '<:pigepeek:888604933073535017>',
    '<:pigepeek:888604940455534615>',
    '<:pigepeek:888604944964415499>',
    '<:pigepeek:888604949297107005>',
    '<:pigepeek:888604957404708875>',
    '<:pigepeek:888604964119797821>',
    '<:pigepeek:888604966590251049>',
    '<:pigepeek:888604971640172614>',
    '<:pigepeek:888604976782389248>',
    '<:pigepeek:888604982989971456>',
    '<:pigepeek:888604987112980480>',
    '<:pigepeek:888604990787190875>',
    '<:pigepeek:888604995728060426>',
    '<:pigepeek:860545545805234187>',
    '<:pigepeek:974019444009476197>',
    '<:pigepeek:993763656288436304>'
]

pigepeek_emoji_ids_dic = {
    "pigepeek": pigepeek_emoji_ids,
    "festivepeek": "<:festivepeek:916746661324271646>",
    "spookepeek": '<:spookepeek:899747028379250718>',
    "luvepeek": "<:luvepeek:1006728505368772721>"
}


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


# Day, Month
seasonal_dates = {
    'festivepeek': {
        'start': {'day': '6', 'month': '12'},
        'end': {'day': '26', 'month': '12'}},
    'spookepeek': {
        'start': {'day': '17', 'month': '10'},
        'end': {'day': '1', 'month': '11'}},
    'luvepeek': {
        'start': {'day': '7', 'month': '2'},
        'end': {'day': '15', 'month': '2'}}
}

# Test: 940331847618007090, 1007872442884178021
# Main: 883177197832126565, 889587732651855972
archive_ids = {
    'pigepeek': 940331847618007090,
    'pigepeek_archive': 1007872442884178021
    # 'pigepeek': 883177197832126565,
    # 'pigepeek_archive': 889587732651855972
}


def check_to_process_archives(channels):
    # Check between certain times of the year. If not, return
    localtime = time.localtime(time.time())
    day = localtime.tm_mday
    month = localtime.tm_mon
    day = '20'
    month = '12'
    # pigepeek celebrations currently active
    celebrations = []

    # Checks if current date is within pigepeek event season. Checks month, then day
    for pigepeek_type in seasonal_dates.keys():
        if month == seasonal_dates[pigepeek_type]['start']['month'] or \
                month == seasonal_dates[pigepeek_type]['end']['month']:
            print('within the right month!')
            for _pigepeek_type in seasonal_dates.keys():
                if int(day) in range(int(seasonal_dates[_pigepeek_type]['start']['day']),
                                     int(seasonal_dates[_pigepeek_type]['end']['day'])):
                    print('within right days!')
                    # Cheer the user for the celebration
                    pigepeek_cheer(_pigepeek_type)
                    celebrations.append(_pigepeek_type)
                else:
                    print('not within right days!')
        else:
            print('not within the right month!')

    print(celebrations)
    if not celebrations:
        print('no celebration going on')
        return

    # Get a list of all channels that contain the name(s) seasonal_dates.keys()
    # Get their ids in a list
    seasonal_channels = []
    for channel in channels:
        if channel.name in seasonal_dates.keys():
            if str(channel.type) == 'text':
                seasonal_channels.append(channel)

    for channel in seasonal_channels:
        print()
        #channel.edit(category='pigepeek')
        # channel.move(category='pigepeek')

    print(seasonal_channels)
    # print(channels)


def check_to_unarchive():
    print()


def pigepeek_cheer(peek_type: str):
    print('♥ ~Celebrating ' + peek_type + '~ ♥')
