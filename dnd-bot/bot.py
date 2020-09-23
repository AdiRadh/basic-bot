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
from dndUtils.DnDClasses import Skill,NPC,Setting, Alignment, Race, Player, Item
from dndUtils.DataUtils import loadJSON,saveJSON


load_dotenv()
TOKEN = "NzU4MTg1MTM3MjU4NjI3MDky.X2rQ7w._m9ZW73H-pPHQVt8FbW70uaCGpQ"
GUILD = os.getenv("Adi's Souffle")

description = 'DnD Bot v0.1'

bot = commands.Bot(command_prefix='roly', description=description)

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

    cmd = message.content
    if "load" in cmd:
        cmd = cmd.replace("load", "")
        settings = loadJSON()
        await message.channel.send("done")
    if " -cs " in cmd:
        cmd = cmd.replace(" -cs ", "")
        args = cmd.split(sep=None)
        if args.length > 2:
            name = args[1]
            campaign = args[0]

        await message.channel.send("done")
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