import discord
import  os
import requests
import json
import random
from googletrans import Translator
from discord.ext import commands

bot = commands.Bot(command_prefix = ["ec!","Ec!","EC!","eC!"],case_insensitive=True)
client = discord.Client()

benzin = "Benzini Shell'den yarrağı kelden diyorlar doğru mu abla? Bilmem doğrudur herhalde!"
kaan = "Ben Orhan'ın karısıyım. Bana ondan başkası sahip olamaz!"
orhan = "Kaan'ın kocası. Boş zamanlarını onu pompalamakla geçirir."

bad_words = ["amk", "sikim", "siktir", "yarak", "yarrak", "oc","oç", "amcik","amcık","orospu",
             "orosbu", "aq", "sikik", "sikeyim", "pic", "piç", "fahişe", "fahise",
             "yarrag","yarrağım","sikerim","sikiyim", "sik"]

chuck_words = ["Yüce Chuck seni kutsasın pis günahkar!",
               "Yüce Chuck öfkene hakim olmanı emreder!",
               "Yüce Chuck tarafından aforoz edildiniz!",
               "Yüce Chuck ahlaklı bir birey olmanı yeğler!"]
hi_words = ["$selam","$sa","$merhaba","$selamun","$selamin"]

chat_words = ["$naber", "$nbr", "$nasilsin", "$nasılsın"]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)

    translator = Translator()
    word = json_data[0]['q']

    translation = translator.translate(word, src="en", dest='tr')
    quote = translation.text + " -" + json_data[0]['a']
    return (quote)




@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    if msg.startswith('$kaan'):
        await message.channel.send(kaan)

    if msg.startswith('$orhan'):
        await message.channel.send(orhan)

    if msg.startswith('$benzin'):
        await message.channel.send(benzin)



    msg = message.content.lower()
    if any(word in msg for word in bad_words):
        author = message.author.mention
        await message.delete()
        quote = get_quote()
        await message.channel.send(random.choice(chuck_words) + author +"\n"+ quote)

    msg = message.content.lower()
    if any(word in msg for word in hi_words):
        author = message.author.mention
        await message.channel.send("selam " + author + "!")

    msg = message.content.lower()
    if any(word in msg for word in chat_words):
        author = message.author.mention
        await message.channel.send("Harika! Sen? " + author + "!")



bot.run(os.getenv('TOKEN'))