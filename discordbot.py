import discord
import asyncio
import pandas as pd
from Modules.Discord.discordpass import DISCORD_TOKEN
from Modules.Discord.rr_msg import rr_msg

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
            
            if channel.name == 'rr-livedata' and isinstance(channel, discord.TextChannel):
                
                ff, he3, h = rr_msg()
                
                ff_df = pd.DataFrame(ff)
                he3_df = pd.DataFrame(he3)
                h_df = pd.DataFrame(h)

                md1 = ff_df.to_markdown()
                md2 = he3_df.to_markdown()
                md3 = h_df.to_markdown()

                discord_message = (
                    f"VH-778b REF base summary\n```\n{md1}\n```\n"
                    f"VH-043e HE3 base summary\n```\n{md2}\n```\n"
                    f"Hydron H base summary\n```\n{md3}\n```"
                )
                
                await channel.send(discord_message)

#            if channel.name == 'hcc-livedata' and isinstance(channel, discord.TextChannel):
#                await channel.send('Bot here')            


client.run(DISCORD_TOKEN)