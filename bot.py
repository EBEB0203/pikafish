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
    await ctx.send(F'{random.random(1,100)} ('%')')


@bot.event
async def on_member_join(member):
    channel = bot.git_channel(int(jdata['Welcome_channel']))
    await channel.send(F'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.git_channel(int(jdata['Leave_channel']))
    await channel.send(F'{member} leave!')


bot.run(jdata['TOKEN'])


