import random
import telebot
import sqlite3
from telebot import types   # Библиотеки(можешь добавить)           

TOKEN = "YOUR_CODE"    # Наш токен для работы бота
bot = telebot.TeleBot(TOKEN)

answers = ["Перепроверь ещё раз свой запрос"]   # Сообщение в случае неправильной комманды


@bot.message_handler(commands=["start"])    # User запускает бот
def welcome(message):                       # Функция welcome и главные кнопки меню
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # Какая-то фишка для работы кнопок                
    button1 = types.KeyboardButton('Все фильмы')
    button2 = types.KeyboardButton('Поиск по жанрам')
    button3 = types.KeyboardButton('Поиск по коду')
    button4 = types.KeyboardButton('ТГК с фильмами')
    button5 = types.KeyboardButton('Настройки')
    markup.row(button1, button2)            # Вывод кнопок на экран пользователю
    markup.row(button3, button4)
    markup.row(button5)

    if message.text == '/start':
        # Отправляю приветственный текст
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nМеня зовут ФИЛЬМОБОТ и я твой проводник в мир кино и сериалов :)\nДля начала выбери способ поиска фильма в меню ниже: ', reply_markup=markup)  # Приветственное сообщение пользователю, не забываем про markup
    else:
        bot.send_message(message.chat.id, 'Перекинул тебя в главное меню! Выбирай!', reply_markup=markup) # если пользователь по своему желанию зашёл в меню

@bot.message_handler(content_types='photo') # Если user прислал в бот фото
def get_photo(message):
    bot.send_message(message.chat.id, "Извини, у меня нет возможности просматривать фото")
    
# Обработка обычных текстовых команд, описанных в кнопках
@bot.message_handler()
def info(message):
    if message.text == 'Все фильмы' :   # Если происходит действие - функция
        allFilms(message)           

    elif message.text == 'Поиск по жанрам': # Если происходит действие - функция
        searchFilms(message)

    elif message.text == 'Поиск по коду':   # Если происходит действие - функция
        searchCode(message)

    elif message.text == 'ТГК с фильмами':  # Если происходит действие - функция
        tgkMethod(message)

    elif message.text == 'Настройки':       # Если происходит действие - функция
        settings(message)

    elif message.text == 'Драмы' or message.text == 'Комедии' or message.text == 'Боевики' or message.text == 'Мультфильмы' or message.text == 'Романтические' or message.text == 'Триллеры' :    
        dataSearch(message)

    elif message.text == '🔹 Фильм - 1' or message.text == '🔹 Фильм - 2' or message.text == '🔹 Фильм - 3' or message.text == '🔹 Фильм - 4' or message.text == '🔹 Фильм - 5' or message.text == '🔹 Фильм - 6' or message.text == '🔹 Фильм - 7' or message.text == '🔹 Фильм - 8':
        funcFilm(message)

    elif message.text == '↩️ Назад в меню':
        welcome(message)


def funcFilm(message):
    if message.text == '🔹 Фильм - 1':                          # Здесь добавляй всю инфу со всех кнопок
        bot.send_message(message.chat.id, 'Информация о фильме:')   # Тут добавим информацию о фильмах
    elif message.text == '🔹 Фильм - 2':
        bot.send_message(message.chat.id, 'Информация о фильме:')
    elif message.text == '🔹 Фильм - 3':
        bot.send_message(message.chat.id, 'Информация о фильме:')
    elif message.text == '🔹 Фильм - 4':
        bot.send_message(message.chat.id, 'Информация о фильме:')
    elif message.text == '🔹 Фильм - 5':
        bot.send_message(message.chat.id, 'Информация о фильме:')
    elif message.text == '🔹 Фильм - 6':
        bot.send_message(message.chat.id, 'Информация о фильме:')
    elif message.text == '🔹 Фильм - 7':
        bot.send_message(message.chat.id, 'Информация о фильме:')
    elif message.text == '🔹 Фильм - 8':
        bot.send_message(message.chat.id, 'Информация о фильме:') 
    

def dataSearch(message):      # Тут сложно разобраться, постараюсь объяснить. Это функция отвечает за поиск фильмов по жанрам
    if message.text == 'Драмы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # В кнопки с фильмами добавишь фильмочки и серильчучки
        button1 = types.KeyboardButton('🔹 Фильм - 1')
        button2 = types.KeyboardButton('🔹 Фильм - 2')
        button3 = types.KeyboardButton('🔹 Фильм - 3')
        button4 = types.KeyboardButton('🔹 Фильм - 4')
        button5 = types.KeyboardButton('🔹 Фильм - 5')
        button6 = types.KeyboardButton('🔹 Фильм - 6')
        button7 = types.KeyboardButton('🔹 Фильм - 7')
        button8 = types.KeyboardButton('🔹 Фильм - 8')
        button10 = types.KeyboardButton('↩️ Назад в меню')
        markup.row(button1, button2)
        markup.row(button3, button4)
        markup.row(button5, button6)
        markup.row(button7, button8)
        markup.row(button10)


        bot.send_message(message.chat.id, 'Информация о фильме:', reply_markup=markup)
            
    elif message.text == 'Комедии':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        button1 = types.KeyboardButton('🔹 Фильм - 1')
        button2 = types.KeyboardButton('🔹 Фильм - 2')
        button3 = types.KeyboardButton('🔹 Фильм - 3')
        button4 = types.KeyboardButton('🔹 Фильм - 4')
        button5 = types.KeyboardButton('🔹 Фильм - 5')
        button6 = types.KeyboardButton('🔹 Фильм - 6')
        button7 = types.KeyboardButton('🔹 Фильм - 7')
        button8 = types.KeyboardButton('🔹 Фильм - 8')
        button10 = types.KeyboardButton('↩️ Назад в меню')
        markup.row(button1, button2)
        markup.row(button3, button4)
        markup.row(button5, button6)
        markup.row(button7, button8)
        markup.row(button10)

        bot.send_message(message.chat.id, 'Информация о фильме:', reply_markup=markup)

    elif message.text == 'Боевики':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        button1 = types.KeyboardButton('🔹 Фильм - 1')
        button2 = types.KeyboardButton('🔹 Фильм - 2')
        button3 = types.KeyboardButton('🔹 Фильм - 3')
        button4 = types.KeyboardButton('🔹 Фильм - 4')
        button5 = types.KeyboardButton('🔹 Фильм - 5')
        button6 = types.KeyboardButton('🔹 Фильм - 6')
        button7 = types.KeyboardButton('🔹 Фильм - 7')
        button8 = types.KeyboardButton('🔹 Фильм - 8')
        button10 = types.KeyboardButton('↩️ Назад в меню')
        markup.row(button1, button2)
        markup.row(button3, button4)
        markup.row(button5, button6)
        markup.row(button7, button8)
        markup.row(button10)

        bot.send_message(message.chat.id, 'Информация о фильме:', reply_markup=markup)

    elif message.text == 'Мультфильмы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        button1 = types.KeyboardButton('🔹 Фильм - 1')
        button2 = types.KeyboardButton('🔹 Фильм - 2')
        button3 = types.KeyboardButton('🔹 Фильм - 3')
        button4 = types.KeyboardButton('🔹 Фильм - 4')
        button5 = types.KeyboardButton('🔹 Фильм - 5')
        button6 = types.KeyboardButton('🔹 Фильм - 6')
        button7 = types.KeyboardButton('🔹 Фильм - 7')
        button8 = types.KeyboardButton('🔹 Фильм - 8')
        button10 = types.KeyboardButton('↩️ Назад в меню')
        markup.row(button1, button2)
        markup.row(button3, button4)
        markup.row(button5, button6)
        markup.row(button7, button8)
        markup.row(button10)

        bot.send_message(message.chat.id, 'Информация о фильме:', reply_markup=markup)
    
    elif message.text == 'Триллеры':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        button1 = types.KeyboardButton('🔹 Фильм - 1')
        button2 = types.KeyboardButton('🔹 Фильм - 2')
        button3 = types.KeyboardButton('🔹 Фильм - 3')
        button4 = types.KeyboardButton('🔹 Фильм - 4')
        button5 = types.KeyboardButton('🔹 Фильм - 5')
        button6 = types.KeyboardButton('🔹 Фильм - 6')
        button7 = types.KeyboardButton('🔹 Фильм - 7')
        button8 = types.KeyboardButton('🔹 Фильм - 8')
        button10 = types.KeyboardButton('↩️ Назад в меню')
        markup.row(button1, button2)
        markup.row(button3, button4)
        markup.row(button5, button6)
        markup.row(button7, button8)
        markup.row(button10)

        bot.send_message(message.chat.id, 'Информация о фильме:', reply_markup=markup)

    elif message.text == 'Романтические':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        button1 = types.KeyboardButton('🔹 Фильм - 1')
        button2 = types.KeyboardButton('🔹 Фильм - 2')
        button3 = types.KeyboardButton('🔹 Фильм - 3')
        button4 = types.KeyboardButton('🔹 Фильм - 4')
        button5 = types.KeyboardButton('🔹 Фильм - 5')
        button6 = types.KeyboardButton('🔹 Фильм - 6')
        button7 = types.KeyboardButton('🔹 Фильм - 7')
        button8 = types.KeyboardButton('🔹 Фильм - 8')
        button10 = types.KeyboardButton('↩️ Назад в меню')
        markup.row(button1, button2)
        markup.row(button3, button4)
        markup.row(button5, button6)
        markup.row(button7, button8)
        markup.row(button10)

        bot.send_message(message.chat.id, 'Информация о фильме:', reply_markup=markup)

    


def allFilms(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # В кнопки с фильмами добавишь фильмочки и серильчучки
    button1 = types.KeyboardButton('🔹 Фильм - 1')
    button2 = types.KeyboardButton('🔹 Фильм - 2')
    button3 = types.KeyboardButton('🔹 Фильм - 3')
    button4 = types.KeyboardButton('🔹 Фильм - 4')
    button5 = types.KeyboardButton('🔹 Фильм - 5')
    button6 = types.KeyboardButton('🔹 Фильм - 6')
    button7 = types.KeyboardButton('🔹 Фильм - 7')
    button8 = types.KeyboardButton('🔹 Фильм - 8')
    button10 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5, button6)
    markup.row(button7, button8)
    markup.row(button10)

    
    bot.send_message(message.chat.id, 'Вот все фильмы, которые вы можете посмотреть сейчас:', reply_markup=markup)


def searchFilms(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # Как-то лень объяснять, но надеюсь ты понял
    button1 = types.KeyboardButton('Драмы')
    button2 = types.KeyboardButton('Комедии')
    button3 = types.KeyboardButton('Боевики')
    button4 = types.KeyboardButton('Мультфильмы')
    button5 = types.KeyboardButton('Романтические')
    button6 = types.KeyboardButton('Триллеры')
    button7 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5, button6)
    markup.row(button7)

    bot.send_message(message.chat.id, 'Отсортировал по жанрам для вас', reply_markup=markup)


def searchCode(message):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     button1 = types.KeyboardButton("Ввести код фильма")
     button2 = types.KeyboardButton("↩️ Назад в меню")
     markup.row(button1, button2)

     bot.send_message(message.chat.id, 'Введите код фильма после нажатия на кнопку', reply_markup=markup)


def tgkMethod(message):
    # Тут оставим ссылку на наш приватный тг канал
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("↩️ Назад в меню")
    markup.row(button1)
    bot.send_message(message.chat.id, 'Подпишись -> @...', reply_markup=markup)


def settings(message):  # Если хочешь, то дополни настройки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("↩️ Назад в меню")
    markup.row(button1)
    bot.send_message(message.chat.id, 'О проблемах писать -> @jansavitskiy', reply_markup=markup)


bot.polling(none_stop = True) # Запускаем бота
