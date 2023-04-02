#ДЗ на вторник:
# Добавить функционал боту:
# Кнопки:
#     Хочу анекдот - показывает текстовый анекдот
#     Хочу спать
#     Прощание с ботом
#     Приветствие бота
import random
import telebot
from telebot import types
# 6021092396:AAHyGzNkuRA_nuyF6K5fEAh_GlPIDaUHOGw
spis_anekdot = ['Похоже, специалистам IТ-поддержки, рекомендующим все болячки на ноуте лечить перезагрузкой, школьные учителя слишком часто говорили: "Выйди и зайди по- нормальному. "',
                'Извеcтнoе изpечение Будды глacит: "Baши cтpaдaния вызвaны вaшим coпpoтивлением тoму, что еcть". Т. е. cтpадaния вoзмoжны тoлькo тoгдa, кoгдa мы oткaзываемcя пpинимaть пpоиcходящее. Еcли вы мoжете чтo–тo изменить, пpимите меpы. Ho еcли изменения невoзмoжны, тo у вac еcть двa ваpиaнтa: пpинять cитуaцию и oтпуcтить негaтив или дoлгo, увлеченнo и cтрacтнo cтpадaть.',
                '-Ваш тренер что-нибудь понимает в футболе? \n - Конечно! Перед каждой игрой он объясняет нам, как мы можем выиграть, а потом после игры анализирует, почему мы проиграли.',
                'Сдам в аренду мысли. На одну ночь. Просто реально выспаться нужно.',
                'Нервный пассажир спрашивает у стюардессы: \n - Часто ли разбиваются самолеты вашей компании? \n - Только один раз.'
                ]

token = "6021092396:AAHyGzNkuRA_nuyF6K5fEAh_GlPIDaUHOGw"
bot = telebot.TeleBot(token)


def virt_klav():
    klav = types.InlineKeyboardMarkup(row_width=1)
    drink_but = types.InlineKeyboardButton(text='Хочу пить', callback_data='1')
    eat_but = types.InlineKeyboardButton(text='Хочу есть', callback_data='2')
    anekdot_but = types.InlineKeyboardButton(text='Хочу анекдот', callback_data='3')
    goodbye_but = types.InlineKeyboardButton(text='Пока, Бот', callback_data='4')
    hello_but = types.InlineKeyboardButton(text='Привет, Бот', callback_data='5')
    sleep_but = types.InlineKeyboardButton(text='Хочу спать', callback_data='6')
    klav.add(drink_but, eat_but, anekdot_but,sleep_but, goodbye_but, hello_but)
    return klav

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, 'Привет, выберите что вы хотите: ', reply_markup=virt_klav())


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == '1':
            img = 'https://oskada.ru/wp-content/uploads/2015/11/315.jpg'
            bot.send_photo(chat_id=call.message.chat.id, photo=img, caption='Картинка воды', reply_markup=virt_klav())

        if call.data == '2':
            img = 'https://avatars.mds.yandex.net/i?id=c2cee3a2c9e4ea4a230b609ba50d996d7cf06931-8754774-images-thumbs&n=13'
            bot.send_photo(chat_id=call.message.chat.id, photo=img, caption='Картинка еды', reply_markup=virt_klav())

        if call.data == '3':
            bot.send_message(chat_id=call.message.chat.id, text=f'{spis_anekdot[random.randrange(len(spis_anekdot))]}',
                             reply_markup=virt_klav())

        if call.data == '6':
            img = 'https://avatars.mds.yandex.net/i?id=111e961b6fb5fa01e107e5c8c5a6b8eb6d2c31b4-8186614-images-thumbs&n=13'
            bot.send_photo(chat_id=call.message.chat.id, photo=img, caption='Иди спать!', reply_markup=virt_klav())

        if call.data == '4':
            bot.send_message(chat_id=call.message.chat.id, text=f'Пока {call.message.from_user.first_name}!',
                             reply_markup=virt_klav())

        if call.data == '5':
            bot.send_message(chat_id=call.message.chat.id, text=f'Привет {call.message.from_user.first_name}!',
                             reply_markup=virt_klav())




bot.polling(none_stop=True)
