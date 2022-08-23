# time_helpers.py
import asyncio
import datetime
import time

from py_helpers.json_helpers import seasonal_dates, archive_ids, default_emoji_name


class MyDictionary(dict):
    # Function to add key:value
    def add(self, key, value):
        self[key] = value


# Should call this at the start of every day, midnight
# Checks if current date is within emoji seasonal events. Checks month, then day
def find_ongoing_celebrations():
    # Check between certain times of the year. If not, return
    localtime = time.localtime(time.time())
    day = localtime.tm_mday
    month = localtime.tm_mon
    # Debug test days
    # day = '14'
    # month = '12'
    # emoji celebrations currently active
    celebrations = []

    for emoji_type in seasonal_dates.keys():
        if month == seasonal_dates[emoji_type]['start']['month'] or \
                month == seasonal_dates[emoji_type]['end']['month']:
            if int(day) in range(int(seasonal_dates[emoji_type]['start']['day']),
                                 int(seasonal_dates[emoji_type]['end']['day'])):
                # Cheer the user for the celebration
                emoji_cheer(emoji_type)
                celebrations.append(emoji_type)

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
                    await channel.move(category=archive_category_channels[default_emoji_name],
                                       sync_permissions=True,
                                       beginning=True,
                                       offset=1 + i,
                                       reason='Seasonal event happening')
                else:
                    # Archive channel
                    if channel.category == archive_category_channels[default_emoji_name]:
                        await channel.move(category=archive_category_channels[default_emoji_name],
                                           sync_permissions=True,
                                           beginning=True,
                                           offset=i,
                                           reason='Seasonal event not happening')


def emoji_cheer(peek_type: str):
    print('♥ ~Celebrating ' + peek_type + '~ ♥')


# Waits until the start of midnight
async def wait_for_new_day():
    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
    midnight = datetime.datetime(
        year=tomorrow.year, month=tomorrow.month, day=tomorrow.day,
        hour=0, minute=0, microsecond=0)

    seconds_until_next_day = (midnight - datetime.datetime.now()).total_seconds()
    await asyncio.sleep(seconds_until_next_day)