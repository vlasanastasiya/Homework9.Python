import telebot
import calculate
bot = telebot.TeleBot(calculate.CALC_BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Калькулятор!!!')
    pass


@bot.message_handler(content_types=['text'])
def calc(message):
    try:
        bot.send_message(message.chat.id, eval(message.text))
        pass

    except:
        bot.send_message(message.chat.id, f'Not this:{message.text}!!!')
        bot.send_message(message.chat.id, '(2+2*2)')
        pass
    pass


bot.polling()
