import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord.flags import Intents
from config import token, owner, botid, prefix


bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('봇실행 완료')





bot.run(token) #config 설정하고 봇실행 하고 오류가 뜨면 token을 token, bot=True 바꾸세요