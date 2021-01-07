import discord
from discord.ext import commands
import random
import json

#呼叫Json
with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix = ">")

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)} (ms)')

@bot.command()
async def 幸運指數(ctx):
    lucky = random.randint(1,100)
    await ctx.send(F'>>> :star2::four_leaf_clover:你今天的幸運指數:four_leaf_clover::star2:\n你的幸運指數為: {lucky} %!')

@bot.command()
async def 摸魚燒(ctx):
    await ctx.send(jdata['fish_burn'])





'''
@bot.event
async def on_member_join(member):
    channel = bot.git_channel(int(jdata['Welcome_channel']))
    await channel.send(F'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.git_channel(int(jdata['Leave_channel']))
    await channel.send(F'{member} leave!')
'''

bot.run(jdata['TOKEN'])


