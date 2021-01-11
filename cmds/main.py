import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
from datetime import datetime,timezone,timedelta
import random

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

    @commands.command()
    async def botsay(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    # @commands.command()
    # async def rand_squad(self, ctx):
    #     online = []
    #     for member in ctx.guild.members:
    #         if str(member.status) == 'online' and member.bot == False:
    #             online.append(member.name)

    #     random_online = random.sample(online, k=20)
    #     for i in range(4):
    #         r = random.sample(random_online, k=5)
    #         await ctx.send(a)
    #         for j in r:
    #             random_online.remove(neme)


    # @commands.command()
    # async def cls(self, ctx, num: int):
    #     await ctx.channel.purge(limit = num+1)
    
    
    # @commands.command()
    # async def em(self, ctx):
    #     dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
    #     dt2 = dt1.astimezone(timezone(timedelta(hours=8)))
    #     embed=discord.Embed(title="標題", url="https://www.facebook.com/OhR0203/",
    #      description="內容", color=0xd5c034,
    #      timestamp = dt2)
    #     embed.set_author(name="EB", url="https://www.facebook.com/OhR0203/")
    #     embed.add_field(name="1", value="11", inline=False)
    #     embed.add_field(name="2", value="22", inline=False)
    #     embed.add_field(name="3", value="33", inline=False)
    #     embed.add_field(name="4", value="44", inline=False)
    #     embed.set_footer(text="1234")
    #     await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Main(bot))