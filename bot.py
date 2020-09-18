import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = "NzU2NDQ3Njc2MTY5NDUzNjAw.X2R-zA.EsccrfkV4GcsaI_EssyPA6a0RrM"
GUILD = os.getenv("Adi's Souffle")

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

client.run(TOKEN)