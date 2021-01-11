import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
from datetime import datetime,timezone,timedelta

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    
    @commands.command()
    async def 幸運指數(self, ctx):  
        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt2 = dt1.astimezone(timezone(timedelta(hours=8)))    
        lucky = random.randint(1,100)
        username = ctx.author.name
        embed=discord.Embed(title=f":star2::four_leaf_clover:{username}今天的幸運指數:four_leaf_clover::star2:",
         description=f"{username}, 你今天的幸運指數為: {lucky} % !", color=0xd5c034,
         timestamp = dt2)
        embed.set_footer(text=f"{username}輸入指令",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
 
    @commands.command()
    async def 摸魚燒(self, ctx):  
        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt2 = dt1.astimezone(timezone(timedelta(hours=8)))              
        embed=discord.Embed(title="摸魚燒",
         description=jdata['fish_burn'], color=0xd5c034, timestamp = dt2)
        embed.set_thumbnail(url="https://i.imgur.com/HbMxwtQ.jpg")
        await ctx.send(embed=embed)

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
           await ctx.send('恒慧 !')
       elif git == jdata['pic'][8]:
           await ctx.send('韌守 !')
       elif git == jdata['pic'][9]:
           await ctx.send('傷命 !')
       elif git == jdata['pic'][10]:
           await ctx.send('會命 !')
       elif git == jdata['pic'][11]:
           await ctx.send('賦力 !') 
  
    @commands.command()
    async def 吃啥(self, ctx):
        git = random.choice(jdata['night_eat'])
        await ctx.send(git)

    @commands.command()
    async def 大州府(self, ctx):
        big_week = random.choice(jdata['big_week'])
        await ctx.send(f'大州府會出現在: {big_week} !!!')
    
    @commands.command()
    async def 登記(self, ctx):
        await ctx.send(f">>> [靠賽登記表]\n{jdata['check_in']}")
        
def setup(bot):
    bot.add_cog(React(bot))