import discord
from discord.ext import commands


client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@client.event
async def on_ready():
    print('ログインしました')

@client.command()
async def test(ctx):
    await ctx.send('適切に起動できてます')

@client.command()
async def hoge(ctx):
    await ctx.send('ほげほげ')

TOKEN = 'ここにトークン'
client.run(TOKEN)