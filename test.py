import discord

client = discord.Client()
TOKEN = 'OTkzNzYwMDI5Mjg5MjMwNDM3.GT2i2M.QC2NqKAkFzKCMXLw1A75_yFgrWNY0ZuHOkp7Bg'

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    

client.run(TOKEN)