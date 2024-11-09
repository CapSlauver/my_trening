











import telebot
from telebot import types

# Замените "YOUR_BOT_TOKEN" на ваш токен бота
bot = telebot.TeleBot("7580650965:AAG3lr1b8vQxzMxTwS6n5agftOl8ouZIkn0")


YOUR_CHAT_ID = "906044683"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = types.KeyboardButton("ценники за продажу своей карты")
    itembtn2 = types.KeyboardButton("инфа о безопасности")
    itembtn3 = types.KeyboardButton("ответы на частые вопросы")
    itembtn4 = types.KeyboardButton("форма анкеты для продажи карты")
    itembtn5 = types.KeyboardButton("Готов продать карту")
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)

    bot.send_message(message.chat.id, "Приведствую тебя, ты нажал старт, значит ты готов продать свою карту и получить за это сумму🤑 \nРАБОТАЕМ ТОЛЬКО ПО МСК", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "ценники за продажу своей карты":
        bot.send_message(message.chat.id, "Сбер 14+ - 6.000 \n Сбер 18+ - 10.000 \nАльфа - 5.000 \nотп 18+ - 4.500 \nПСБ 18+ - 4.500 \nРсхб 18+ - 6.000")
    elif message.text == "инфа о безопасности":
        bot.send_message(message.chat.id, "Данные паспорта и другая личная информация не уходят за пределы моих рук \nона нужна исключительно в целях перевязать карту в банковском приложении")
    elif message.text == "ответы на частые вопросы":
        bot.send_message(message.chat.id, "Все встречи по продажам карт проходят только в мск сити.\n\nОдна карта на человека (по одной каждого банка; если есть доп. карты либо закрывает либо отдает) \n\nАнкета обязательно (на альфу или отп банк можно только: ФИО; номер телефона; тг; номер карты; пин)\n\nальфы и ОТП банк без блоков откручиваем, можешь не переживать если сдаешь эти банки \n\nТак же трафик у нас вторичный (только проверенные клиенты) и еще мы не работаем с казино\n\nна каждого человека 14+ можно оформить: \nАльфа \nСбер \nОТП (попробуйте, там вроде есть молодежная карта) \n\nНа каждого 18+ можно оформить: \nАльфа \nСбер \nОТП  \nПСБ (только Оранж клуб нужен, если будешь его делать на кого-то, то напиши, я напишу как) \n\nРоссельхозбанк (там тоже нужно делать его строго по инструкции так как нужна не одна карта)\n\nТак же никакой чернухи, казино и прочей ебатни у меня нет, офис на котором я стою работает больше года, а я больше 3-х месяцев, до меня тип работал больше 6-ти месяцев")
    elif message.text == "форма анкеты для продажи карты":
        bot.send_message(message.chat.id, "ФИО: \nФамилия Имя Отчество\nПаспортные данные: \nСерия и номер:\nКод подразделения:\nДата выдачи:\n\nДата рождения:  \nДД.ММ.ГГГГ\n\nФактический адрес проживания:  \nУлица, дом, квартира\n\nАдрес по прописке:  \nУлица, дом, квартира\n\nНомер личной карты (которую отдаешь):  \n16-значный номер карты\n\nНазвание банка (альфа/сбер и тд):\n\n Кредиты/ипотеки:  \nДа/Нет, если да, укажите детали\nЛичный номер телефона:  \nНомер телефона\n\nМесто работы/учебы: \nНаименование организации или учебного заведения\n\nДата и адрес получения карты/открытия счета:  \nДД.ММ.ГГГГ и точный адрес отделения банка (можно примерно если очень тяжело вспомнить)\n\nПоследнее посещение Сбербанка (Дата, адрес, цель):  \nДД.ММ.ГГГГ, адрес отделения, цель посещения (можно примерно если очень тяжело вспомнить)\n\nКодовое слово (обязательно):  \nКодовое слово для операций\n(если нет, пишем «нет», если есть, но не помните, пишите хотяб примерное)\n\nРодственники (проживающие по прописке):  \nФИО проживающих по тому же адресу (просто пишем родственника, а не его фио, например «бабушка»/«мама»/«папа»\n\nФИО матери:  \nФамилия Имя Отчество матери\n\nПоследние крупные покупки:\n\nИнформация о последних онлайн-покупках (подписках):\n\nИнформация по месту жительства:  \nБлижайшая улица, наличие ТЦ или магазинов, дом, количество этажей, номер подъезда\n\nТелефон, с которого запускался Сбер (модель телефона):  \nМарка и модель телефона\n\nДевичья фамилия (если замужем):  \nДевичья фамилия\n\nПинкод:\nТг для контакта:\nМожно не заполнять только про родителей, остальное обязательно")
    elif message.text == "Готов продать карту":
        bot.send_message(message.chat.id, "введите всю инфу также, как в примере анкеты")
        bot.register_next_step_handler(message, process_message)

def process_message(message):
    user_message = message.text
    bot.send_message(message.chat.id, f"Вы написали: {user_message}")
    bot.send_message(YOUR_CHAT_ID, f"Пользователь написал: {user_message}")  # Отправка сообщения вам


bot.polling()