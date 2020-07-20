import discord
import os

client = discord.Client()

@client.event
async def on_rady():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('수바인보'))
    print("Bot status :: online")


@client.event
async def on_message(message):
    if message.content.startswith("돌민 ㅎㅇ?"):
        await message.channel.send("안녕하신가")
    if message.content.startswith("닌로"):
        await message.channel.send("바보")
    if message.content.startswith("<명령어목록"):
        await message.channel.send("명령어는 닌로,닌로배틀태그,돌민 ㅎㅇ? 그리고 잡담이 있음")
    if message.content.startswith("배틀태그"):
        await message.channel.send("BBungŅIÑŔO#1139")
        await message.channel.send("BáBoŃińrô#2341")
        await message.channel.send("닌.로#3378")
    if message.content.startswith("빅스비"):
        await message.channel.send("음란마귀+병신이다")
    if message.content.startswith("개굴"):
        await message.channel.send("개구리 걍 노래를하지마!")
    if message.content.startswith("바보야"):
        await message.channel.send("조까")
    if message.content.startswith("노래틀어줘"):
        await message.channel.send("나와랏 리듬봇!")
    if message.content.startswith("닌.로주챔"):
        await message.channel.send("오버워치:겐지,맥크리,자리야 | 발로란트:세이지,소바")











access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
