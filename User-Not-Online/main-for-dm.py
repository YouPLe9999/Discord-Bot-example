import discord
from discord.ext import commands
import asyncio

# 봇 설정
intents = discord.Intents.all() # Readme 참고
client = discord.Client()
interval = 300  # 초 단위, 멤버 상태를 확인하는 간격

# 멤버 상태 확인 함수
async def check_member_status():
    await client.wait_until_ready()
    while not client.is_closed():
        for guild in client.guilds:
            for member in guild.members:
                if str(member.status) != "online":
                    # 멤버가 온라인 상태가 아닌 경우 DM 채널로 메시지 전송
                    dm_channel = await member.create_dm()
                    await dm_channel.send("당신은 지금 온라인 상태가 아닙니다!")
        # 지정된 시간 간격으로 상태를 확인
        await asyncio.sleep(interval)

# 봇 동작 시작
@client.event
async def on_ready():
    print("봇이 시작되었습니다.")
    client.loop.create_task(check_member_status())

# 봇 실행
client.run('토큰')
