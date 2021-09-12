import discord
client = discord.Client()

@client.event
async def on_ready():
    try:
        print('Logged in as {0.user}'.format(client))
    except:
        print("Could not login")

@client.event
async def on_message(message):
    if message.author == client.user:  #  so we don't respond to our own messages- we shouldn't but just in case
        return
    if message.content.startswith("!delete"):  #  if a message needs to be deleted
        await message.channel.purge()

client.run(<insert your token here>)
