# bot.py
import os, random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intent = discord.Intents.default()
intent.members = True
intent.message_content = True
client = discord.Client(intents=intent)


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(f'{client.user.name} has connected to Discord!')
    print(f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})')

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
    elif message.content == 'raise-exception':
        raise discord.DiscordException
    
bot = commands.Bot(command_prefix='!', intents = discord.Intents.default())

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

bot.run(TOKEN)

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