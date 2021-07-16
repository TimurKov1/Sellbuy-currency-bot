from setting.SETTINGS import *

from parsing.parsing import Parsing
import telebot
from parsing.sort import Information

bot = telebot.TeleBot(TOKEN)
bank_site = Parsing(URL, URL_1)
bank_site_1 = bank_site.get_info()
currency = bank_site.currency
info = Information(bank_site_1, currency)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 
'''Привет!

Это бот телеграмм, в котором вы можете узнать лучший курс покупки 
и продажи интересующей вас валюты, или узнать её действующий курс.

Выберите валюту, курс которой хотите узнать:''', reply_markup=BOARD_NEW)


@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет!')

    elif message.text == '🇺🇸 USD':
        bot.send_message(message.chat.id, info.print_usd_eur(info.buy_usd, info.sell_usd, '🇺🇸 USD'), reply_markup=buttons().row('🥇 Лучшие курсы USD', '🔙 Назад'))
    
    elif message.text == '🥇 Лучшие курсы USD':
        bot.send_message(message.chat.id, info.print_best_currency(info.usd_buy, info.best_buy_usd, info.usd_sell, info.best_sell_usd, '🇺🇸 USD'), reply_markup=buttons().row('🥇 Лучшие курсы USD', '🔙 Назад'))

    elif message.text == '🔙 Назад':
        bot.send_message(message.chat.id, 'Выберите валюту, курс которой хотите узнать: ', reply_markup=BOARD_NEW)

    elif message.text == '🇪🇺 EUR':
        bot.send_message(message.chat.id, info.print_usd_eur(info.buy_eur, info.sell_eur, '🇪🇺 EUR'), reply_markup=buttons().row('🥇 Лучшие курсы EUR', '🔙 Назад'))

    elif message.text == '🥇 Лучшие курсы EUR':
        bot.send_message(message.chat.id, info.print_best_currency(info.eur_buy, info.best_buy_eur, info.eur_sell, info.best_sell_eur, '🇪🇺 EUR'), reply_markup=buttons().row('🥇 Лучшие курсы EUR', '🔙 Назад'))

    elif message.text == '🔎 Выбрать банк':
        bot.send_message(message.chat.id, 'Выберите один из данных банков:', reply_markup=BOARD_1)

    elif message.text in info.banks:
        bot.send_message(message.chat.id, info.print_bank(message.text), reply_markup=BOARD_1)

    elif message.text == '💰 Все курсы':
        bot.send_message(message.chat.id, info.print_currency(), reply_markup=BOARD_NEW)

    elif message.text == '🥇 Лучшие курсы':
        bot.send_message(message.chat.id, info.best_course(), reply_markup=BOARD_NEW)

    elif message.text == '📉 Курсы ЦБ':
        bot.send_message(message.chat.id, info.print_CB(), reply_markup=BOARD_NEW)

    else:
        bot.send_message(message.chat.id, 'Выберите валюту, курс которой хотите узнать:')

bot.polling()
