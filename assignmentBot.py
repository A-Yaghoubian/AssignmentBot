import random
import telebot
from khayyam import JalaliDatetime
from gtts import gTTS

bot = telebot.TeleBot("2019327355:AAF9JCQPiBsOQKrEivcNfGlAoFk5nWKQ0jc")

@bot.message_handler(commands=['Start', 'start', 'شروع'])
def wellcome(message):
    first_name = message.from_user.first_name
    bot.reply_to(message, f'{first_name} خوش اومدی')

@bot.message_handler(commands=['Game', 'game', 'بازی'])
def play_game(message):
    bot.reply_to(message, 'بازی حدس عدد')
    bot.send_message(message.chat.id, 'یک عدد بین ۰ تا ۱۰۰۰ بگو')
    game(random.randint(0, 1000))

def game(answer_number):
    def loop_game():
        @bot.message_handler(func=lambda message: True)
        def game_works(message):
            if int(message.text) > answer_number:
                bot.send_message(message.chat.id, 'کمترش کن')
                loop_game()
            elif int(message.text) < answer_number:
                bot.send_message(message.chat.id, 'بیشترش کن')
                loop_game()
            elif int(message.text) == answer_number:
                bot.send_message(message.chat.id, 'ماشالااااا خودشه\nپیداش کردی')
    loop_game()
    
# @bot.message_handler(commands=['Age', 'age', 'سن'])
# def calculate_age(message):
#     bot.send_message(message.chat.id, 'Example: 27/4/1379')
#     age()

# def age():
#     @bot.message_handler(func=lambda message: True)
#     def age_works(message):
#         slash_counter = 0
#         for letter in message.text:
#             if letter == '/':
#                 slash_counter += 1
#         if slash_counter == 2:
#             input_text = message.text
#             input_list = input_text.split('/')
#             difference = JalaliDatetime.now() - JalaliDatetime(input_list[2], input_list[1], input_list[0])
#             difference = int(((str(difference)).split(' '))[0])
#             y = difference // 365
#             difference %= 365
#             m = difference // 30
#             difference %= 30
#             d = difference
#             bot.send_message(message.chat.id, f'You are {y} years, {m} months and {d} days old :)')
#         else:
#             bot.send_message(message.chat.id, 'Wrong input!')
            
@bot.message_handler(commands=['voice'])
def voice_producer(message):
    bot.reply_to(message, 'Enter your message')
    voice()
    
def voice():
    @bot.message_handler(func=lambda message: True)
    def voice_works(message):
        message_text = message.text
        language = 'en'        
        message_voice = gTTS(text=message_text, lang=language, slow=False)
        bot.send_voice(message.chat.id, message_voice)
        bot.send_voice(message.chat.id, "FILEID")
                    
bot.polling()
