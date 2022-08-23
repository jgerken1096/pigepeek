# json_helpers.py
import json
import sys


# Returns the values such as dictionaries from the config file
# Request must be list but can hold one or more values
# Acceptable request names: 'emoji_ids', 'seasonal_dates', 'archive_ids', 'hidden_gem_chance'
def json_fetch(request: list):
    with open('../config.json') as json_data:
        data = json.load(json_data, )

    # Checking for inappropriate data in config.json
    for item in data:
        match item:
            case 'emoji_ids':
                continue
            case 'seasonal_dates':
                continue
            case 'archive_ids':
                continue
            case 'hidden_gem_chance':
                continue
            case 'default_emoji_name':
                continue
            case _:
                print("Non-default config file components found", file=sys.stderr)
                return

    # If one item in list
    if len(request) == 1:
        for item in request:
            match item:
                case 'emoji_ids':
                    return data[item]
                case 'seasonal_dates':
                    return data[item]
                case 'archive_ids':
                    return data[item]
                case 'hidden_gem_chance':
                    return data[item]
                case 'default_emoji_name':
                    return data[item]
                case _:
                    print("Requested data does not exist", file=sys.stderr)
                    return
    # If more than one item in list
    else:
        values_to_return = []
        for item in request:
            match item:
                case 'emoji_ids':
                    values_to_return.append(data[item])
                case 'seasonal_dates':
                    values_to_return.append(data[item])
                case 'archive_ids':
                    values_to_return.append(data[item])
                case 'hidden_gem_chance':
                    values_to_return.append(data[item])
                case 'default_emoji_name':
                    values_to_return.append(data[item])
                case _:
                    print("Requested data that doesn't exist", file=sys.stderr)
                    return
        return values_to_return


emoji_ids, seasonal_dates, archive_ids, default_emoji_name, hidden_gem_chance = json_fetch([
    'emoji_ids', 'seasonal_dates', 'archive_ids', 'default_emoji_name', 'hidden_gem_chance'])
