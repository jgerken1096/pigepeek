# iterables.py
# lists and dictionaries

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
        'end': {'day': '15', 'month': '2'}},
}

# Ids are for both archiving and unarchiving
# Test: 940331847618007090, 1007872442884178021
# Main: 883177197832126565, 889587732651855972
archive_ids = {
    'pigepeek': 940331847618007090,
    'pigepeek_archive': 1007872442884178021
    # 'pigepeek': 883177197832126565,
    # 'pigepeek_archive': 889587732651855972
}