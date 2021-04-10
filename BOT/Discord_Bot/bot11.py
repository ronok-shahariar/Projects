import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is ready.')


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)


def is_it_me(ctx):
    return ctx.author.id == 755096368955260979


@client.command()
@commands.check(is_it_me)
async def example(ctx):
    await ctx.send(f'Hi im {ctx.author}')


client.run('')
