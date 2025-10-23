import discord

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send("Hello!")
    elif message.content.startswith('bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('this bot sucks'):
        await message.channel.send("no u")
    else:
        await message.channel.send(message.content)

client.run("MTQyODQ4ODMxMzMxNjE4MDEyOA.GomAZp.CqD958zyO5fSbGYF49OWtVej9e8KAPwmELsQ0o")
