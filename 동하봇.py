import discord
import datetime
import os
client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game ("프로봇 개발중..삐..삑..")
    await client.change_presence (status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("프로봇 안녕"):
        await message.channel.send("안녕 나는 프로봇이야")
    if message.content.startswith("프로봇 뭐해?"):
        await message.channel.send("난 지금 평행세계에 있어 ㅎㅎ")
    if message.content.startswith("프로봇 동하님 유튜브 링크 알려줘"):
        await message.channel.send("https://www.youtube.com/channel/UC8l-MCj2jpgyLO-GS-jBmzQ")
    if message.content.startswith("프로봇 동하님 트위치 링크 알려줘"):
        await message.channel.send("https://www.twitch.tv/dongha_7")
    if message.content.startswith("프로봇 배고파"):
        await message.channel.send("제가 맛있는 삼겹살을 해드리겠습니다 ㅃ...삐삑")
    if message.content.startswith("프로봇 녀석을 제거해줘"):
        await message.channel.send("누구를 말씀이십니까? 전 언제나 준비되어 있는 살인 로봇 동하봇입니다")
    if message.content.startswith("프로봇 가을이를 죽여줘"):
        await message.channel.send("가을 , 본명 조재호님을 처단하겠습니다. 팔다리는 어떻게 할까요?")
    if message.content.startswith("프로봇 마크 사이트 알려줘"):
        await message.channel.send("https://www.minecraft.net/ko-kr/")
    if message.content.startswith("프로봇 마인리스트 사이트 알려줘"):
        await message.channel.send("https://minelist.kr/")
    if message.content.startswith("프로봇 동하님이 하는 게임 알려줘"):
        await message.channel.send("동하님이 하는게임은 배틀그라운드 , 오버워치 , 마인크래프트 , osu! , 콜오브듀티: 워존 입니다.")
    if message.content.startswith("프로봇 뉴스"):
        await message.channel.send("https://news.naver.com/")
    if message.content.startswith("프로봇 펭룬이는 누구야?"):
        await message.channel.send("펭룬 , 나이 14세 국적 대한민국 펭귄의 탈을 쓰고 있는 인간이다.")
    if message.content.startswith("프로봇 동하는 누구야?"):
        await message.channel.send("동하 , 나이 18세 취미 영화 및 게임 / 코딩 / 마술 이고 , 내년에 수능보는 사람이다")

    if message.content.startswith ("/사진"):
        pic = message.content.split (" ")[1]
        await message.channel.send (file=discord.File (pic))


@client.event
async def on_message(message):
    if message.content.startswith ("/내정보"):
        date = datetime.datetime.utcfromtimestamp (((int (message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed (color=0x00ff00)
        embed.add_field (name="이름", value=message.author.name, inline=True)
        embed.add_field (name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field (name="가입일", value=str (date.year) + "년" + str (date.month) + "월" + str (date.day) + "일",
                         inline=True)
        embed.add_field (name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail (url=message.author.avatar_url)
        await message.channel.send (embed=embed)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
