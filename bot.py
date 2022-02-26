import discord
from discord.ext import commands

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print(f'Bot is now online')

@client.command(aliases=['p', 'q'])
async def ping(ctx, arg=None):
    if arg == "pong":
        await ctx.send('Nice job, you just ponged yourself')

    else:
        await ctx.send(f'Pong! Here is you ping: {round(client.latency * 1000)}ms')

client.run('OTQ3MTI5MzM5MDQ3MjAyODE2.Yhow7w.lOz4ohQ6GLcXah-nO3zGxoRC5lI')
