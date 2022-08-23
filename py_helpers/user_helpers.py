# user_helpers.py
# handles user-related functions
import pandas as pd

from random import randint
from py_helpers.json_helpers import emoji_ids, default_emoji_name, hidden_gem_chance


# Verifies user is not sending the same emoji back-to-back
async def user_already_sent_emoji(message):
    # Receiving history for last two messages
    messages = [message async for message in message.channel.history(limit=2)]
    current_message_author_id = messages[0].author.id
    previous_message_author_id = messages[1].author.id

    if current_message_author_id == previous_message_author_id:
        return True
    return False


# Handles deletion of improper messages
async def delete_wrong_message(message):
    await message.delete()
    return


# Handles hidden gem (Easter egg) to re-send the emoji back to the user
# Chance is the denominator ( 1 / chance )
async def try_hidden_gem(message):
    emoji_type = message.channel.name

    min_chance = 1
    max_chance = hidden_gem_chance
    result_chance = randint(min_chance, max_chance)
    if result_chance != max_chance:
        return

    # Str = only one type of emoji id
    if isinstance(emoji_ids[emoji_type], str):
        await message.channel.send(emoji_ids[emoji_type])
        return
    elif isinstance(emoji_ids[emoji_type], list):
        list_random_pos = randint(0, (len(emoji_ids[emoji_type]) - 1))
        await message.channel.send(emoji_ids[emoji_type][list_random_pos])
        return

    return


# Checks if the user can send acceptable emojis in this channel
def is_correct_channel_for_sending_emoji(message):
    if message.channel.name in emoji_ids.keys():
        return True
    return False


def user_is_sending_correct_emoji(message):
    emoji_type = message.channel.name

    if isinstance(emoji_ids[emoji_type], list):
        if message.content.strip().lower() in emoji_ids[emoji_type]:
            return True
    elif isinstance(emoji_ids[emoji_type], str):
        if message.content.strip().lower() == emoji_ids[emoji_type]:
            return True
    return False


# Increases the user's emoji count by one
def increase_emoji_count(user_id):
    df = pd.read_csv("../emoji_counter.csv")

    if user_id not in df.user_id.values:
        # New User
        df_new_user = pd.DataFrame(data=[[user_id, 1]],
                                   columns=['user_id', 'emoji_count']).convert_dtypes(convert_integer=True)
        df = pd.concat([df, df_new_user])
        df.to_csv(r'emoji_counter.csv', index=False)
    else:
        # Existing User
        query = df.where(df.user_id == user_id).convert_dtypes(convert_integer=True).emoji_count

        df.update(query + 1)
        df.to_csv(r'emoji_counter.csv', index=False)


async def give_default_emoji_role(member):
    roles = member.guild.roles
    default_role = None
    for role in roles:
        if role.name == default_emoji_name:
            # Future proofing
            if not role.permissions.administrator:
                if not default_emoji_name:
                    default_role = role
                else:
                    print("More than one default emoji role found", file=sys.stderr)
                    return

    if not default_role:
        print("Default emoji role could not be found", file=sys.stderr)
        return

    await member.add_roles(default_role, reason='joined server')