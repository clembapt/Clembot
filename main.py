import discord
import os
from discord.ext import commands, tasks

client = discord.Client()
bot = commands.Bot("!")
target_channel_id = 853227884055232515

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!xqcow'):
        await message.channel.send('https://www.twitch.tv/xqcow')

@tasks.loop(hours=24)
async def called_once_a_day():
    message_channel = bot.get_channel(target_channel_id)
    await message_channel.send("sa fais 24h")

@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")

called_once_a_day.start()    
 


token = os.environ['token'] 
bot.run(token)
client.run(token)
