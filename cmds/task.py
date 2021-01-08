import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.count = 0
        #間隔輸出
        # async def interval():
        #     await self.bot.wait_until_ready()
        #     self.channel = self.bot.get_channel(797101234514690059)
        #     while not self.bot.is_closed():
        #         await self.channel.send('hi eb is god')
        #         await asyncio.sleep(5)
        
        # self.bg_task = self.bot.loop.create_task(interval())

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(797101234514690059)
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime('%H%M')
                with open('setting.json', 'r', encoding='utf8') as jfile:
                    jdata = json.load(jfile)
                if now_time == jdata['time'] and self.count == 0:
                    await self.channel.send('Task Working!')
                    self.count = 1
                    await asyncio.sleep(1)
                else:
                    pass
                    await asyncio.sleep(1)

        self.bg_task = self.bot.loop.create_task(time_task())
        
    @commands.command()
    async def set_channel(self, ctx, ch: int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set channel: {self.channel.mention}')

    @commands.command()
    async def set_time(self, ctx, time):
        self.count = 0
        with open('setting.json', 'r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        jdata['time'] = time
        with open('setting.json', 'w', encoding='utf8') as jfile:
            json.dump(jdata, jfile, indent=4)

def setup(bot):
    bot.add_cog(Task(bot))