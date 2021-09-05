import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(827783390819385368)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(827783390819385368)
    await channel.send(f'{member} leave!')


bot.run('ODgzNjgxNjUxNjgxNTI5ODY3.YTNeqw.lBSs0PuzDi_LiZr6UhwMtdiv04Y')