import random
import telebot

bot = telebot.TeleBot("2019327355:AAF9JCQPiBsOQKrEivcNfGlAoFk5nWKQ0jc")
game_flag = 1
game_answer_number = random.randint(0, 1000)

@bot.message_handler(commands=['Start', 'start', 'شروع'])
def wellcome(message):
    first_name = message.from_user.first_name
    bot.reply_to(message, f'{first_name} خوش اومدی')

@bot.message_handler(commands=['Game', 'game', 'بازی'])
def play_game(message):
    bot.reply_to(message, 'بازی حدس عدد')
    bot.send_message(message.chat.id, 'یک عدد بین ۰ تا ۱۰۰۰ بگو')
    global game_flag
    game_flag = 1
    print('0')
    
if game_flag == 1:
    print('1')
    @bot.message_handler(func=lambda message: True)
    def check_game(message):
        print('2')
        while True:
            if int(message.text) > game_answer_number:
                bot.send_message(message.chat.id, 'کمترش کن')
            elif int(message.text) < game_answer_number:
                bot.send_message(message.chat.id, 'بیشترش کن')
            elif int(message.text) == game_answer_number:
                bot.send_message(message.chat.id, 'ماشالااااا خودشه\nپیداش کردی')
                global game_flag
                game_flag = 0
                break
                
bot.polling()
