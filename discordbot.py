import discord
import asyncio
from Modules.Discord.discordpass import DISCORD_TOKEN

intents = discord.Intents.default()
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    await client.wait_until_ready()  # Wait until the bot is fully ready and its internal cache is populated

    # Assuming 'general' is the name of the channel you want to send a message to
    # This code will look for a channel named 'general' in all servers the bot is part of and send a message to the first one it finds
    for guild in client.guilds:
        for channel in guild.channels:
            
            if channel.name == 'test3' and isinstance(channel, discord.TextChannel):
                await channel.send('Bot here')

            if channel.name == 'general' and isinstance(channel, discord.TextChannel):
                await channel.send('Bot here')            


client.run(DISCORD_TOKEN)