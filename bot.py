import discord
import os
import time
import asyncio
import logging
import socket
from discord.ext import commands
import subprocess

print('===================')
print('Lancement du bot...')

TOKEN = "token"

client = commands.Bot(command_prefix = '_')
client.remove_command('help')
client.vc = 0
client.ping = 0

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="game", url="https://www.twitch.tv/liberto"))
    print('Bot lancé')
    print('===================')
    channelv = client.get_channel(id channel vocal)
    client.vc = await channelv.connect()

async def Detection():
    await client.wait_until_ready()
    while not client.is_closed():
        serveur = client.get_guild(id serveur)
        channel = client.get_channel(id channel écrit général)
        region = serveur.region
        regionstr = str(region)
        await asyncio.sleep(2)
        test = client.vc.endpoint

        try:
            cmd = "ping -c {} -W {} {}".format(1, 1, test).split(' ')
            output = subprocess.check_output(cmd).decode().strip()
            lines = output.split("\n")
            total = lines[-2].split(',')[3].split()[1]
            loss = lines[-2].split(',')[2].split()[0]
            timing = lines[-1].split()[3].split('/')

        except:
            if regionstr == "eu-west":
                await serveur.edit(region="eu-central")
                embed = discord.Embed(
                    title = ('La Centrale Anti-DDoS'),
                    colour = discord.Colour.green()
                )

                embed.add_field(name='Protection DDoS activée !', value="Les attaques devraient cesser...", inline=True)
                await channel.send(embed=embed)

            elif regionstr == "eu-central":
                await serveur.edit(region="eu-west")
                embed = discord.Embed(
                    title = ('La Centrale Anti-DDoS'),
                    colour = discord.Colour.green()
                )

                embed.add_field(name='Protection DDoS activée !', value="Les attaques devraient cesser...", inline=True)
                await channel.send(embed=embed)

            else:
                await serveur.edit(region="eu-central")
                embed = discord.Embed(
                    title = ('La Centrale Anti-DDoS'),
                    colour = discord.Colour.green()
                )

                embed.add_field(name='Protection DDoS activée !', value="Les attaques devraient cesser...", inline=True)
                await channel.send(embed=embed)

            print("Attaque contrée")


        try:
            client.ping = float(timing[1])
            maxping = float(100)
            if client.ping > maxping:
                if regionstr == "eu-west":
                    await serveur.edit(region="eu-central")
                    embed = discord.Embed(
                        title = ('La Centrale Anti-DDoS'),
                        colour = discord.Colour.green()
                    )

                    embed.add_field(name='Protection DDoS activée !', value="Les attaques devraient cesser...", inline=True)
                    await channel.send(embed=embed)

                elif regionstr == "eu-central":
                    await serveur.edit(region="eu-west")
                    embed = discord.Embed(
                        title = ('La Centrale Anti-DDoS'),
                        colour = discord.Colour.green()
                    )

                    embed.add_field(name='Protection DDoS activée !', value="Les attaques devraient cesser...", inline=True)
                    await channel.send(embed=embed)

                else:
                    await serveur.edit(region="eu-central")
                    embed = discord.Embed(
                        title = ('La Centrale Anti-DDoS'),
                        colour = discord.Colour.green()
                    )

                    embed.add_field(name='Protection DDoS activée !', value="Les attaques devraient cesser...", inline=True)
                    await channel.send(embed=embed)

                print("Attaque contrée")
            else:
                a = 1
        except:
            print('error')

@client.command()
@commands.has_role("DDOS")
async def jeu(ctx, *jeuu):
    channel = ctx.message.channel
    jeuuu = ' '.join(jeuu)
    await client.change_presence(activity=discord.Streaming(name=jeuuu, url="https://www.twitch.tv/liberto"))
    embed = discord.Embed(
        title = ('La Centrale Anti-DDoS'),
        colour = discord.Colour.green()
    )

    embed.add_field(name='Statut de jeu:', value=("changé en " + jeuuu), inline=True)
    await channel.send(embed=embed)

@client.command()
@commands.has_role("DDOS")
async def region(ctx):
    channel = ctx.message.channel
    nserveur = ctx.guild.name
    region = ctx.guild.region
    regionstr = str(region)
    serveur = ctx.guild
    await channel.send("Région: " + regionstr)

@client.command()
@commands.has_role("DDOS")
async def help(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        title = ('Page d\'aide '),
        colour = discord.Colour.green()
    )

    embed.set_thumbnail(url='https://images-ext-2.discordapp.net/external/kY3ozLi_4-DZ5qoqfJ95B0U6l5bnDrziQq-PYT-BEDc/https/cdn.discordapp.com/icons/556943011536437268/65f028a6bad42a6d0ac14a8254f9e18e.png')
    embed.add_field(name='_ping', value="Donne le ping.", inline=True)
    embed.add_field(name='_endpoint', value="Donne l'endpoint", inline=True)
    embed.add_field(name='_region', value="Donne la région.", inline=True)
    embed.add_field(name='_jeu', value="Change le statut du bot.", inline=True)

    await channel.send(embed=embed)


@client.command()
@commands.has_role("DDOS")
async def endpoint(ctx):
    channel = ctx.message.channel
    test = client.vc.endpoint

    await channel.send("Endpoint: " + test + " ou " + socket.gethostbyname(client.vc.endpoint))

@client.command()
@commands.has_role("DDOS")
async def ping(ctx):
    channel = ctx.message.channel
    ping = str(client.ping)
    await channel.send("Ping: " + ping + " ms")

client.loop.create_task(Detection())
client.run(TOKEN)
