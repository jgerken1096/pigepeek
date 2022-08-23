# pigepeek
Bot for discord pigepeek server

## About
The pigepeek server is a server for organizational emoji streaking while promoting positive social environment.

## Getting Started Discord Section
- Default emoji in config.json must have a discord (non-admin) role to match it, as well as a discord emoji.
- The concept of this discord role is for design but also for security reasons. Only those with the role can pigepeek, @everyone does not have permission. If the bot is unavaliable for any reason, one can simply revoke the "pigepeek"'s permission to message manually.
- Discord channels must be appropriately named via the emoji ids in config.json. An example for a channel name for one using the ":pigepeek:" emoji, would be, "pigepeek".
- Seasonal date channels should be placed under a category "archive" and non-seasonal dates must be placed under the category "pigepeek". Other categories will be ignored.
- They will be moved at the start of each day in correspondence with the dates inputted in config.json

## Getting Started Bot Section
- Data is managed through csv files. The csv file will be created at bot startup if the file does not already exist.
- A .env must be created with a DISCORD_TOKEN= and DISCORD_GUILD=
- For the .env you can find this information / create it at https://discordapp.com/developers/applications/
- Move config.json outside the docs folder.
- Within the config.json file, one can store the acceptable emoji ids within "emoji_ids". This accepts either singular strings or lists.
- Any values with repeating singular numbers must be replaced with the appropriate ids
- Ids can be obtained in discord developer mode by right-clicking on a component, such as a category heading or emoji, and copying its id.
- Seasonal dates can be made in accord with other emojis that you want to be allowed.
- One may add more seasonal date emojis if they'd like and new start and end times.
- Archive ids config is for the category discord server ids. The default, pigepeek, is required as well as an archives section.
- Hidden gem chance is the chance that the bot will send an emoji in response to your emoji.

## Contributions
If you are interested in contributing to this bot as a user:
- Please submit any issues that arrive when using the bot as well as suggestions for new features. Suggestions should be placed within issues.
If you are interested in contributing to this bot as a programmer:
- Check out the issues and look for one that doesn't look overwelhming. Check for the "good first issue" tag as well. Please make sure to understand current documentation as to not remake already existing code.
