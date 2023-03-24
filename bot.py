# bot.py
import os, random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    # await suspends the execution of the surrounding coroutine
    # until the execution of each coroutine has finished.
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

client.run(TOKEN)

# class CustomClient(discord.Client):
#     async def on_ready(self):
#         print(f'{self.user} has connected to Discord!')

# # Client an instance of CustomClient
# # which has an overridden on_ready() function
# client = CustomClient()
# client.run(TOKEN)

# client = discord.Client(intents=discord.Intents.default())
# # on_ready() will be called once client is ready for further action
# @client.event
# async def on_ready():

#     # discord.utils.find() can improve the simplicity and readability of this code
#     # by replacing the for loop with an abstracted function
#     # for guild in client.guilds:
#     #     if guild.name == GUILD:
#     #         break
#     # guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
#     # get() takes the iterable and some keyword arguments, in this case name=GUILD
#     guild = discord.utils.get(client.guilds, name=GUILD)
#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})'
#     )

#     members = '\n - '.join([member.name for member in guild.members])
#     print(f'Guild Members:\n - {members}')

# client.run(TOKEN)