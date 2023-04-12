# DiscordChannelCloner
A script to clone messages (along with their details) from single or multiple channels into a specified channel using Discord Webhooks. Cross-server channel cloning is supported.

## Configuration
Example `config.json`:
```json
[
  {
    "channel_id": 13245678913456789, // Target channel ID.
    "hook_id": 13245678913456789, // The ID of the Webhook integrated into the target channel.
    "source": [13245678913456789, 13245678913456789] // An array of channel IDs to clone messages from.
  }
]
```

Note that the self-host user must have the `manage_webhooks` permission.

## Deployment

The Docker image can be found at GitHub's Container Registry:
```
docker pull ghcr.io/exilvm/discordchannelcloner:master
```

### Docker Compose

It is recommended to deploy Discord Channel Cloner using Docker Compose. Check the [`docker-compose.yml`](https://github.com/exilvm/DiscordChannelCloner/blob/master/docker-compose.yml) file in this repository.

### Building the Image Yourself

To build the Docker image yourself, run the following commands:

```
git clone git@github.com:exilvm/DiscordChannelCloner.git && cd DiscordChannelCloner
```

Set your `TOKEN` and `CONFIG_DIRECTORY` environment variables to the appropriate values, and run:

```
docker-compose up -d
```

## Using this script for regular bots
This script uses [discord.py-self](https://github.com/dolfies/discord.py-self). If you want to run this script on a regular bot, use [discord.py](https://github.com/Rapptz/discord.py) instead.
