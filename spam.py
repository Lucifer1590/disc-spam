import discum
import random
import time
bot = discum.Client(token="{token}",)


#words=['hi', 'hello', 'to the moon', 'this is cool', 'its ok', 'wow',"don't stop", "Wats goin on", "hehe", "keep grinding", 'this server is cool', 'its awsome', 'grinding', 'just a bit more', 'haha', 'this project is good', 'to the moo$

with open("wordlist.txt","r") as file:
    words = file.read().split("\n")

for i in range (100):
    bot.sendMessage('{channelid}',random.choice(words) )
    time.sleep(1)


bot.gateway.run()

