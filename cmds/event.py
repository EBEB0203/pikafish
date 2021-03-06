import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.git_channel(int(jdata['Welcome_channel']))
        await channel.send(f'{member} join!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.git_channel(int(jdata['Leave_channel']))
        await channel.send(f'{member} leave!')
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        keyname = jdata["keyname"]
        
        if msg.content in keyname  and msg.author != self.bot.user:
            await msg.channel.send(random.choice(jdata['keyv']))
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandNotFound):
            await ctx.send("不要亂打指令好ㄇ !")
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("參數要填 懂 ??")
        else:
            await ctx.send("你打錯了! 大錯特錯!!!")
def setup(bot):
    bot.add_cog(Event(bot))