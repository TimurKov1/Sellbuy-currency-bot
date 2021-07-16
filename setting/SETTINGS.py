import telebot

def buttons():
    board = telebot.types.ReplyKeyboardMarkup(True, True)
    return board

URL = 'https://ru.myfin.by/currency'
URL_1 = 'http://www.cbr.ru/currency_base/daily/'
TOKEN = '1845891200:AAFx1gD2x-pQBqqUSHWu07pVxNe8fOlQuCg'

BOARD_NEW = buttons()
BOARD_NEW.row('🇺🇸 USD', '🇪🇺 EUR', '💰 Все курсы')
BOARD_NEW.row('🥇 Лучшие курсы', '🔎 Выбрать банк', '📉 Курсы ЦБ')
BOARD_1 = buttons()
BOARD_1.row('СберБанк', 'Банк «Открытие»', 'Банк ВТБ')
BOARD_1.row('Газпромбанк', 'Росбанк', 'Райффайзенбанк')
BOARD_1.row('Тинькофф Банк', 'Россельхозбанк', '🔙 Назад')


