import os
import random
import telebot

TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['Start', 'start'])
def wellcome(message):
    first_name = message.from_user.first_name
    bot.reply_to(message, f'Hey {first_name}, Welcome 😃')
                    
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
    Description = '1️⃣ /start : start and welcome\n 2️⃣ /game : Play game\n 3️⃣ /age : Your age\n 4️⃣ /voice : text to voice\n 5️⃣ /max : maximum in list\n 6️⃣ /argmax : highest number argument in list\n 7️⃣ /qrcode : product QR code\n\nAli Yaghoubian 👨‍💻\nSupport: @Alijackoub'
    bot.send_message(message.chat.id, Description)        

bot.polling()
