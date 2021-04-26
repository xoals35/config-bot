import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord.flags import Intents
from config import token, owner, botid, prefix


bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('봇실행 완료')

#============================================================================================================================================================================
#환영, 퇴장 알림 코드는 시스템 채널에 보내집니다. 
@bot.event
async def on_member_join(member):
    embed=discord.Embed(title=f'입장알림',description=f'{member.mention}님  환영합니다  \n현재 서버 인원수: {str(len(member.guild.members))}명',color=discord.Color.blue())
    embed.set_thumbnail(url=member.avatar_url)
    await member.guild.system_channel.send(embed=embed)

@bot.event
async def on_member_remove(member):
    embed=discord.Embed(title=f'퇴장알림',description=f'{member.mention}님  잘가요ㅠㅠ  \n현재 서버 인원수: {str(len(member.guild.members))}명',color=discord.Color.red())
    embed.set_thumbnail(url=member.avatar_url)
    await member.guild.system_channel.send(embed=embed)

    
bot.run(token) #config 설정하고 봇실행 하고 오류가 뜨면 token을 token, bot=True 바꾸세요
