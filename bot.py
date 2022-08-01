# bot.py
import os
from colorama import Fore, Back, Style

print("Bekleyin, önemli modüller yükleniyor...")

os.system("cls")
print("------------------------------------------------------")
print("Merhaba!")
print("")
print(Fore.GREEN + "(!) Botu çalıştırmak için [ENTER] basın.")
print(Style.RESET_ALL)
print("github.com/trashbin7/DcGamesTR")
print("------------------------------------------------------")
input()
os.system("cls")
print("------------------------------------------------------")
print("Bot yükleniyor...")
print()
print(Fore.GREEN + "---" + Fore.RED + "-----------------")
print(Style.RESET_ALL)
print("importlar/değişkenler kuruluyor...")
print("------------------------------------------------------")
import discord
from dotenv import load_dotenv
import time
import random
os.system("cls")
print("------------------------------------------------------")
print("Bot yükleniyor...")
print()
print(Fore.GREEN + "-----------" + Fore.RED + "---------")
print(Style.RESET_ALL)
print("Token yükleniyor...")
print("------------------------------------------------------")
load_dotenv()
TOKEN = os.environ["TOKEN"]
GUILD = ('DISCORD_GUILD')

client = discord.Client()

os.system("cls")
print("------------------------------------------------------")
print("Bot yükleniyor...")
print()
print(Fore.GREEN + "---------------" + Fore.RED + "-----")
print(Style.RESET_ALL)
print("Sunucu ismi alınıyor...")
print("------------------------------------------------------")
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    os.system("cls")
    print("------------------------------------------------------")
    print("Bot yükleniyor...")
    print()
    print(Fore.GREEN + "--------------------")
    print(Style.RESET_ALL)
    print("Tamamen hazır!")
    print("------------------------------------------------------")
    time.sleep(0.3)
    os.system("cls")
    print("------------------------------------------------------")
    print(Fore.YELLOW + str(client.user) + Style.RESET_ALL + " Aşağıdaki sunucuya bağlı:")
    print(Fore.YELLOW + str(guild.name))
    print(Style.RESET_ALL + "(id: " + Fore.YELLOW + str(guild.id) + Style.RESET_ALL + ")")
    print()
    print()
    print("------------------------------------------------------")


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Merhaba {member.name}, Discord sunucumuza hoş geldin! \n discord.gg/4w8D6yrKCX")

@client.event
async def on_member_remove(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Merhaba {member.name}, Discord sunucumuzdan ayrıldın! \n discord.gg/4w8D6yrKCX")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.yardım'):
        await message.channel.send('**YARDIM (BOT V0.4)** \n `.ping` - bot pingini gösterir. \n `.sunucu` - sunucu bilgisini gösterir. \n `.kullanıcı` - kullanıcı bilgisini gösterir. \n \n bu botda birkaç gizli özellik var ||günaydın|| gibi. onları sizin bulmanız gerekecek!')

    if message.content.startswith('.ping'):
        await message.channel.send('Pong!')
    if message.content.startswith(".sunucu"):
        await message.channel.send("Sunucu ismi: " + str(message.guild.name))
    if message.content.startswith(".sunucusahibi"):
        await message.channel.send("Sunucu sahibi: Mertcinarsah74 ve Drexy")
    if message.content.startswith(".sunucuid"):
        await message.channel.send("Sunucu ID: " + str(message.guild.id))
    if message.content.startswith("sa"):
        await message.channel.send("as")
    if message.content.startswith(".kullanıcı"):
        await message.channel.send("Kullanıcı ismi: " + str(message.author.name))
    if message.content.startswith("günaydın"):
        await message.channel.send("sana da günaydın!")
    if message.content.startswith("iyi geceler"):
        await message.channel.send("sana da iyi geceler!")

# kendime not: buraya iyi günler yazızını ekleyeceğim.

@client.event
async def on_member_ban(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Merhaba {member.name}, Discord sunucumuzdan **banlandın!** \n discord.gg/4w8D6yrKCX")

@client.event
async def on_member_unban(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Merhaba {member.name}, Discord sunucumuzdaki **banın kaldırıldı!** \n discord.gg/4w8D6yrKCX")


client.run(TOKEN)

