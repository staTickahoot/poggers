import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    if bot.user is not None:
        print(f'Logged in as {bot.user.name}')
    else:
        print("Failed to log in. Check your bot token and network connection.")
      
@bot.command()
async def pog(ctx):
    await ctx.send('Im very pog')

@bot.command()
async def poggers(ctx):
    await ctx.send('Im super poggers')

bot.run('MTI2MTE0MTMyNzI1Nzc5NjcxOQ.GytcnR.Ddf7x4du6CuTA-nh6Zi854RxflAwzBFeFOYSno')