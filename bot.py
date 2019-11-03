token = "NjM4NjU0MzU5NDIwNDAzNzEy.XblGmg.11eFdiq955oZJGb7R4fM6lInDNc" #You get that from the discord developer portal
userid = "548486527114674176" #You own UserID
prefix = "m!" #Prefix for jacc

import discord
from discord.ext import commands
import time

print("Started Dm Bot")

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Do " + prefix + "dm 'message' to run Rana.")
    await bot.change_presence(activity=discord.Activity(name='FreeFire' , type=1))
    

try:
    async def self_check(ctx):
        if bot.user.id == userid or ctx.message.author.id:
            return True
        else:
            return False

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def dm(ctx, *, message):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.send(message)
                print(f"Sent {user.name} a DM.")
            except:
                print(f"Couldn't DM {user.name}.")
        print("Sent all the server a DM.")

  
except:
    pass

bot.run(token)
