import discord
from discord.ext import commands
import random
import json

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


'''
@bot.event
async def on_member_join(member):
    channel = bot.git_channel(795616804578787338)
    await channel.send(F'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.git_channel(795616890630176788)
    await channel.send(F'{member} leave!')
'''

bot.run("Nzk1NTk4NTY5MDE2MDAwNTUy.X_Ls6A.3bz7KI80ae6jSHOCz2mYJnRHMHs")


