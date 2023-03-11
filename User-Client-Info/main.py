import discord
from discord.ext import commands

intents = discord.Intents.all() # Readme 참고
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('봇이 준비되었습니다!')

@client.event
async def on_message(message):
    if message.content == '!status':
        member = message.author
        print(f"{member.name} 님의 클라이언트 정보:")
        print(f"모바일 정보: {member.mobile_status}")
        print(f"컴퓨터 정보: {member.desktop_status}")
        print(f"웹 정보: {member.web_status}")

client.run('토큰')
