import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    @commands.command()
    async def 幸運指數(self, ctx):
       lucky = random.randint(1,100)
       await ctx.send(F'>>> :star2::four_leaf_clover:你今天的幸運指數:four_leaf_clover::star2:\n你的幸運指數為: {lucky} %!')

    @commands.command()
    async def 摸魚燒(self, ctx):
       await ctx.send(jdata['fish_burn'])

    @commands.command()
    async def 撿到(self, ctx):
       git = random.choice(jdata['pic'])
       pic = discord.File(git)
       await ctx.send(file= pic)
    
       if git == jdata['pic'][0]:
           await ctx.send('大悲賦索引 !')
       elif git == jdata['pic'][1]:
           await ctx.send('大悲賦終章 !')
       elif git == jdata['pic'][2]:
           await ctx.send('大悲賦殘捲 !')
       elif git == jdata['pic'][3]:
           await ctx.send('大鐵 !')
       elif git == jdata['pic'][4]:
           await ctx.send('孔雀翎片 !')
       elif git == jdata['pic'][5]:
           await ctx.send('孔雀翎扣 !')
       elif git == jdata['pic'][6]:
           await ctx.send('孔雀翎匣 !')
       elif git == jdata['pic'][7]:
           await ctx.send('恒會 !')
       elif git == jdata['pic'][8]:
           await ctx.send('韌守 !')
       elif git == jdata['pic'][9]:
           await ctx.send('傷命 !')
       elif git == jdata['pic'][10]:
           await ctx.send('會命 !')
       elif git == jdata['pic'][11]:
           await ctx.send('賦力 !') 

def setup(bot):
    bot.add_cog(React(bot))