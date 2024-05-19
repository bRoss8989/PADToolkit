import discord
import asyncio
import pandas as pd
from Modules.Discord.discordpass import DISCORD_TOKEN
from Modules.Discord.rr_msg import rr_msg
from Modules.Discord.dnpc_msg import dnpc_msg
from Modules.Discord.hcc_msg import hcc_msg

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

                if channel.name == 'hcc-livedata' and isinstance(channel, discord.TextChannel):

                    await channel.purge(limit=20)
                    
                    fk794b, fk794c, fk794d, HRT, vh331g, vh331a = hcc_msg()
                    
                    df_fk794b = pd.DataFrame(fk794b)
                    df_fk794c = pd.DataFrame(fk794c)
                    df_fk794d = pd.DataFrame(fk794d)
                    df_HRT = pd.DataFrame(HRT)
                    df_vh331g = pd.DataFrame(vh331g)
                    df_vh331a = pd.DataFrame(vh331a)
                    
    
                    md1 = df_fk794b.to_markdown()
                    md2 = df_fk794c.to_markdown()
                    md3 = df_HRT.to_markdown()
                    md4 = df_vh331g.to_markdown()
                    md5 = df_vh331a.to_markdown()
                    md6 = df_fk794d.to_markdown()
    
                    discord_message2 = (
                        f"Boucher Production Summary\n```\n{md1}\n```\n"
                        f"fk794c Supply Summary\n```\n{md2}\n```\n"
                        f"fk794d Supply Summary\n```\n{md6}\n```\n"
                        f"HRT Supply Summary\n```\n{md3}\n```\n"
                        f"Avalon Supply Summary\n```\n{md4}\n```\n"
                        f"Promitor Supply Summary\n```\n{md5}\n```\n"
                    )
                    
                    await channel.send(discord_message2)

        await asyncio.sleep(3600)  # Sleeps for 1 hour

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    client.loop.create_task(send_msg())


client.run(DISCORD_TOKEN)