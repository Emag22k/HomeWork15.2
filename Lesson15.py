import telebot
import DataBase as db
import buttons as butt


#Создаем объект бота
bot=telebot.TeleBot('7838544838:AAG3Sd4H8_XNguLIAagqFrbkOCZfCvzdOOA')

#Обратока команды\ start
@bot.message_handler(commands=["start"])
def start(message):
    user_id=message.from_user.id
    products =db.get_pr_buttons()
    if db.rechek(user_id):
        bot.send_message(user_id, "Привет! Выберите пунк меню", reply_markup=butt.main_menu(products))
    else:
        bot.send_message(user_id, "Привет! Давайте начем регистрацию!\n"
                                              "Введите ваше Имя!", reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_name)


#Этап получения имени
def get_name(message):
    user_id=message.from_user.id
    user_name=message.text
    bot.send_message(user_id, "Для дальнейшей регистрации отправте номер телефона", reply_markup=butt.number_button())


    bot.register_next_step_handler(message,get_number,user_name)

#Этап получения номера
def get_number(message,user_name):
    user_id = message.from_user.id
    #Проверям отправлен ли номер по кнопке
    if message.contact:
        user_number=message.contact.phone_number
        db.register(user_id,user_name,user_number)
        bot.send_message(user_id, f"Вы успешно зарегестрированы {user_name}!", reply_markup=telebot.types.ReplyKeyboardRemove())

    else:
        bot.send_message(user_id, "Отправьте номер через кнопку ниже!")
        bot.register_next_step_handler(message, get_number, user_name)

bot.polling(non_stop=True)