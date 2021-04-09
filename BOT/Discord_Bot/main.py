import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is ready.')

client.run('ODMwMDA1NzY4NDg4ODc4MTAw.YHAZGw.MKaDsiClCnVNwc6txDkTY164hrI')