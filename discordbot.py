import discord
import asyncio
import pandas as pd
from Modules.Discord.discordpass import DISCORD_TOKEN
from Modules.Discord.rr_msg import rr_msg
from Modules.Discord.dnpc_msg import dnpc_msg

intents = discord.Intents.default()
client = discord.Client(intents=intents)



@client.event
async def send_msg():

    while True:
        
        for guild in client.guilds:
            for channel in guild.channels:
                
                if channel.name == 'rr-livedata' and isinstance(channel, discord.TextChannel):

                    await channel.purge(limit=20)
                    
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
    
                if channel.name == 'dnpc-livedata' and isinstance(channel, discord.TextChannel):

                    await channel.purge(limit=20)
                    
                    deimos_supply, nike_supply, deimos_prod, nike_prod = dnpc_msg()
                    
                    DS_df = pd.DataFrame(deimos_supply)
                    NS_df = pd.DataFrame(nike_supply)
                    DP_df = pd.DataFrame(deimos_prod)
                    NP_df = pd.DataFrame(nike_prod)
                    
    
                    md1 = DS_df.to_markdown()
                    md2 = NS_df.to_markdown()
                    md3 = DP_df.to_markdown()
                    md4 = NP_df.to_markdown()
    
                    discord_message2 = (
                        f"Deimos Supply Summary\n```\n{md1}\n```\n"
                        f"Deimos Production Summary\n```\n{md3}\n```\n"
                        f"Nike Supply Summary\n```\n{md2}\n```\n"
                        f"Nike Prod Summary\n```\n{md4}\n```\n"
                    )
                    
                    await channel.send(discord_message2)

        await asyncio.sleep(3600)  # Sleeps for 1 hour

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    client.loop.create_task(send_msg())


client.run(DISCORD_TOKEN)