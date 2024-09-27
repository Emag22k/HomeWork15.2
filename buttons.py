from telebot import types

#Кнопка отправки номера
def number_button():
    kb=types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1=types.KeyboardButton('Отправить номер☎️', request_contact=True)
    kb.add(but1)

    return kb