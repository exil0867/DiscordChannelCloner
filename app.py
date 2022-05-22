import discord
import json
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

config = None

with open('config.json', 'r') as read_file:
    config = json.load(read_file)

async def cloneMessage(message, channel_id, hook_id):
    channel = client.get_channel(channel_id)
    channel_hooks = await channel.webhooks()
    hook = discord.utils.get(channel_hooks, id=hook_id)
    attachments = message.attachments
    files = []
    for x in attachments:
        file = await x.to_file()
        files.append(file)
    await hook.send(content=message.content, username=f'{message.author.display_name} in {message.channel.name} at {message.created_at}', avatar_url=message.author.avatar_url, files=files)

@client.event
async def on_message(message):
    for x in config:
        if message.channel.id in x['source']:
            await cloneMessage(message, x['channel_id'], x['hook_id'])

client.run(os.getenv('TOKEN'))
