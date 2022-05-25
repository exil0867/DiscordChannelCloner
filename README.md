# DiscordChannelCloner
A script to clone messages from a single or multipe channels into a specified channel using Discord Webhooks. [Cross-server channel cloning is supported]

# config.json example
```json
[
  {
    "channel_id": 13245678913456789, // Target channel ID.
    "hook_id": 13245678913456789, // The ID of the Webhook that is integrated into the target channel.
    "source": [13245678913456789, 13245678913456789] // An array of IDs of channels to clone messages from.
  }
]
```

# Deploy the script using Docker
Run:
```
git clone git@github.com:exilvm/DiscordChannelCloner.git %% cd DiscordChannelCloner
```
Set your TOKEN and CONFIG_DIRECTORY (the path to a directory that contains config.json) environment variables and run:
```
docker-compose up -d
```

# About using this script for regular bots.
This script uses [discord.py-self](https://github.com/dolfies/discord.py-self), if you want to run this script on a regular bot use [discord.py](https://github.com/Rapptz/discord.py) instead.