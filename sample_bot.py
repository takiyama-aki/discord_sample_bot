import discord
from discord.ext import commands
import random


client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

OMIKUJI = ['大吉', '吉', '中吉', '小吉', '末吉', '凶', '大凶']

@client.event
async def on_ready():
    print('ログインしました')

@client.command()
async def hello(ctx):
    await ctx.send('Hello!')

@client.command()
async def omikuji(ctx):
    await ctx.send(f'あなたの運勢は"{OMIKUJI[random.randrange(len(OMIKUJI))]}"!')

@client.command()
async def test(ctx):
    await ctx.send('適切に起動できてます')

@client.command()
async def hoge(ctx):
    await ctx.send('ほげほげ')



TOKEN = 'ここにトークン'
client.run(TOKEN)