import discord
import random
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True

papel = ['canudo','papel_higiênico','caderno','livro']
plastico = ['caixa_de-toddynho', 'garrafa', 'boneco_do_Hulk']
metal = ['pilha', 'motorola']

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}, que te ajuda a jogar o lixo no lugar certo!')

@bot.command()
async def reciclar(ctx, objeto):
    if objeto in papel:
        await ctx.send(f'Isso é feito de papel, você deve jogar no lixo destinado ao papel!')
    elif objeto in plastico:
        await ctx.send(f'Isso é feito de plástico, você deve jogar no lixo destinado a plástico!')
    elif objeto in metal:
        await ctx.send(f'Isso é feito de metal, você deve jogar no lixo destinado ao metal')
    else:
        await ctx.send(f'Não sabemos sobre essa informação, nos desculpe.')

bot.run('')
