import os
import random
import aioredis
import d20
import discord
import motor.motor_asyncio
from aiohttp import ClientOSError, ClientResponseError
from discord.errors import Forbidden, HTTPException, InvalidArgument, NotFound
from discord.ext import commands
from discord.ext.commands.errors import CommandInvokeError
from dotenv import load_dotenv


load_dotenv()
TOKEN = "NzU2NDQ3Njc2MTY5NDUzNjAw.X2R-zA.mP7lsF47h0NoAibyt1BloS6PkGs"
GUILD = os.getenv("Adi's Souffle")

description = 'DnD Bot v0.1'

bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
        'Toight',
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    elif message.content == 'suck ur mum':
        response = 'no suck ur mum'
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        response = 'Command not recognised'
        await message.channel.send(response)
        raise discord.DiscordException


@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
            return "Unhandled Message"
        else:
            raise


bot.run(TOKEN)