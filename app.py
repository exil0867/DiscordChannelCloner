import discord
import json
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

config = None

with open('config/config.json', 'r') as read_file:
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
    embed = discord.Embed(
        title='Message details',
        timestamp=message.created_at
    )
    embed.set_author(name=f'{message.author.name}#{message.author.discriminator}', icon_url=message.author.avatar_url)
    embed.add_field(name="Server name", value=message.channel.guild.name)
    embed.add_field(name="Channel name", value=message.channel.name)
    embed.add_field(name="Author ID", value=message.author.id)
    embed.add_field(name="Message ID", value=message.id)
    embed.add_field(name="Channel ID", value=channel_id)
    embed.add_field(name="Hook ID", value=hook_id)
    embed.add_field(name="Message date", value=message.created_at)
    hook_message = await hook.send(embed=embed, wait=True)
    await hook_message.reply(content=message.content, files=files)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.invisible, afk=False)

@client.event
async def on_message(message):
    for x in config:
        if message.channel.id in x['source']:
            await cloneMessage(message, x['channel_id'], x['hook_id'])

client.run(os.getenv('TOKEN'))
