# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.default())
# on_ready() will be called once client is ready for further action
@client.event
async def on_ready():

    # discord.utils.find() can improve the simplicity and readability of this code
    # by replacing the for loop with an abstracted function
    # for guild in client.guilds:
    #     if guild.name == GUILD:
    #         break
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

client.run(TOKEN)