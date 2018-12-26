import telepot
import time
from mtranslate import translate

bot = telepot.Bot('YOUR_AUTHORIZATION_TOKEN')
telegram()

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type=='text':
        text=msg['text']
        if text=='/start':
            bot.sendMessage(chat_id,'hi,welcome to ranslation bot,for guiding how to work with bot enter /help:')
        elif text=='/help':
             bot.sendMessage(chat_id,'for translating from English to persian enter  number 1,otherwise enter number 2:')
             number=input()
             if number =='1':
                 bot.sendMessage(chat_id,'plz enter your text in English')
                 matn=input()
                 tarjome=translate(matn,'fa','en')
                 print('your translated text is:')
                 bot.sendMessage(chat_id,tarjome)
             elif number =='2':
                 bot.sendMessage(chat_id,'plz enter your text in Persian')
                 matn2=input()
                 tarjome2=translate(matn,'en','fa')
                 print('your translated text is:')
                 bot.sendMessage(chat_id,tarjome2)
                 
                 
            
        

def telegram():

     update = request.get_json()
    if "message" in update:
        handle(update['message'])

# Keep the program running.
while 1:
    time.sleep(10)
