import os
import random
import telebot
from khayyam import JalaliDatetime
from gtts import gTTS
import qrcode

TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['Start', 'start'])
def wellcome(message):
    first_name = message.from_user.first_name
    bot.reply_to(message, f'Hey {first_name}, Welcome 😃')
    
@bot.message_handler(commands=['Voice', 'voice'])
def voice_producer(message):
    msg = bot.send_message(message.chat.id, 'Enter your message')
    bot.register_next_step_handler(msg, voice_works)

def voice_works(message):
    try:
        message_text = message.text
        language = 'en'
        message_voice = gTTS(text=message_text, lang=language, slow=False)
        message_voice.save('your_voice.ogg')
        voice = open('your_voice.ogg', 'rb')
        bot.send_voice(message.chat.id, voice)
    except:
        bot.send_message(message.chat.id, 'WARNING ⚠\nPlease try again')

@bot.message_handler(commands=['Qrcode', 'qrcode'])
def qrcode_producer(message):
    msg = bot.send_message(message.chat.id, 'Enter text or web address or ...\n🔑 Example: www.google.com')
    bot.register_next_step_handler(msg, qrcode_works)
    
def qrcode_works(message):
    try:
        message_text = message.text
        qrcode_image = qrcode.make(message_text)
        qrcode_image.save('your_qrcode.png')
        qrCode = open('your_qrcode.png', 'rb')
        bot.send_photo(message.chat.id, qrCode)
    except:
        bot.send_message(message.chat.id, 'WARNING ⚠\nPlease try again')    
                    
@bot.message_handler(commands=['max', 'Max', 'MAX'])
def maxx(message):
    Description = "Write a list of your numbers (each separated by a ',')\nI will find the largest number and tell you 😎"
    msg = bot.send_message(message.chat.id, Description)
    bot.register_next_step_handler(msg, max_works)

def max_works(message):
    try:
        numbers_text = message.text
        numbers_list = numbers_text.split(',')
        numbers_list = list(map(int, numbers_list))
        answer = str(max(numbers_list))
        bot.send_message(message.chat.id, f'The largest number is {answer}')
    except:
        bot.send_message(message.chat.id, "WARNING ⚠\nDo you just enter numbers and ','? 🤔\nPlease try again")

@bot.message_handler(commands=['argmax', 'Argmax'])
def argmaxx(message):
    Description = "Write a list of your numbers (each separated by a ',')\nI will find the largest number and tell you its index 🧠\nList index starts from 0 ☺"
    msg = bot.send_message(message.chat.id, Description)
    bot.register_next_step_handler(msg, arg_works)

def arg_works(message):
    try:
        numbers_text = message.text
        numbers_list = numbers_text.split(',')
        numbers_list = list(map(int, numbers_list))
        answer_1 = str(max(numbers_list))
        answer_2 = str(numbers_list.index(max(numbers_list)))
        bot.send_message(message.chat.id, f'The largest number: {answer_1}\nIts index: {answer_2}')
    except:
        bot.send_message(message.chat.id, "WARNING ⚠\nDo you just enter numbers and ','? 🤔\nPlease try again")
        
@bot.message_handler(commands=['help', 'Help', 'HELP'])
def help(message):
    Description = '1️⃣ /start : start and welcome\n2️⃣ /game : Play game\n3️⃣ /age : Your age\n4️⃣ /voice : text to voice\n5️⃣ /max : maximum in list\n6️⃣ /argmax : highest number argument in list\n7️⃣ /qrcode : product QR code\n\nAli Yaghoubian 👨‍💻\nSupport: @Alijackoub'
    bot.send_message(message.chat.id, Description)        

bot.polling()
