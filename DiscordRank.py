import discord
from discord.ext import commands
print(discord.__version__)
import requests
import urllib.parse
import sys
print(sys.version)


TOKEN = 'MTA2NzU5MjE2Mjk3NzUxNzY0OA.G0lhBo.vHfCkA8M0n0LWKr3Gw9DYxDSAvIQESH_61sIN0'

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='.', intents=intents)

@client.event
async def on_ready():
    print('Logged in as', client.user)

@client.event
async def on_message(message):
    if message.content.startswith("!rank"):
        playername = " ".join(message.content.split(" ")[1:]) #combine all elements after the first one into a single string
        encoded_playername = urllib.parse.quote(playername)
        url = f'https://accelerategaming.com/leaderboard/testleaderboard.php?player={encoded_playername}'
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            await message.channel.send(content)
        else:
            await message.channel.send("URL not accessible")


client.run('MTA2NzU5MjE2Mjk3NzUxNzY0OA.G0lhBo.vHfCkA8M0n0LWKr3Gw9DYxDSAvIQESH_61sIN0')

