import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

from datetime import datetime,timezone,timedelta
dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
dt2 = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
       await ctx.send(f'{round(self.bot.latency*1000)} (ms)')
    '''
    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="標題", url="https://www.facebook.com/OhR0203/",
         description="內容", color=0xd5c034,
         timestamp = dt2)
        embed.set_author(name="EB", url="https://www.facebook.com/OhR0203/")
        embed.add_field(name="1", value="11", inline=False)
        embed.add_field(name="2", value="22", inline=False)
        embed.add_field(name="3", value="33", inline=False)
        embed.add_field(name="4", value="44", inline=False)
        embed.set_footer(text="1234")
        await ctx.send(embed=embed)
    '''
def setup(bot):
    bot.add_cog(Main(bot))