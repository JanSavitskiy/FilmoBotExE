import sqlite3
from telebot import TeleBot, types

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot = TeleBot('YOUR_TOKEN')

def create_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY
    )
    ''')
    conn.commit()
    conn.close()  # Закрываем соединение

# Добавление пользователя в базу данных
def add_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO users (id) VALUES (?)', (user_id,))
    conn.commit()
    conn.close()  # Закрываем соединение

answers = "Перепроверь ещё раз свой запрос"  # Сообщение в случае неправильной команды

@bot.message_handler(commands=["start"])
def welcome(message):                       # Функция welcome и главные кнопки меню
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # Какая-то фишка для работы кнопок                
    button1 = types.KeyboardButton('Поиск по жанрам')
    button2 = types.KeyboardButton('Поиск по коду')
    button3 = types.KeyboardButton('ТГК с фильмами')
    button5 = types.KeyboardButton('Настройки')           # Вывод кнопок на экран пользователю
    markup.row(button1, button2, button3)
    markup.row(button5)
    user_id = message.from_user.id
    add_user(user_id)

    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nМеня зовут ФИЛЬМОБОТ и я твой проводник в мир кино и сериалов :)\nДля начала выбери способ поиска фильма в меню ниже: ', reply_markup=markup)

@bot.message_handler(commands=['users_admin'])
def list_users(message):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM users')
    users = cursor.fetchall()
    conn.close()  # Закрываем соединение
    user_ids = [str(user[0]) for user in users]
    bot.send_message(message.chat.id, "Список пользователей:\n" + "\n".join(user_ids))


@bot.message_handler()
def info(message):
    if message.text == 'Поиск по коду':
        bot.send_message(message.chat.id, "Введите номер фильма:")
        bot.register_next_step_handler(message, search)
    elif message.text == 'ТГК с фильмами':
        tgk(message)  # Регистрируем следующий шаг
    elif message.text == 'Настройки':
        settings(message)
    elif message.text == 'Поиск по жанрам':
        bot.send_message(message.chat.id, "Введите жанр фильма:\n\nP.s Вводите жанр правильно\n\nДоступные жанры: Драма, Ужасы, Фантастика, Комедия, Романтика")
        bot.register_next_step_handler(message, searchGenre)
    elif message.text == '↩️ Назад в меню':
        welcome(message)
    else:
        bot.send_message(message.chat.id, answers)

my_dict = {
    1: {
        "Название": "Интерстеллар",
        "Описание": "Космическая одиссея о группе астронавтов, которые исследуют червоточину в поисках нового дома для человечества.",
        "Ссылка": "https://www.imdb.com/title/tt0816692/",
        "Жанр": "Фантастика"
    },
    2: {
        "Название": "Начало",
        "Описание": "Вор, специализирующийся на краже идей, получает задание внедриться в сознание человека и изменить его мысли.",
        "Ссылка": "https://www.imdb.com/title/tt1375666/",
        "Жанр": "Фантастика"
    },
    3: {
        "Название": "Матрица",
        "Описание": "Программист Нейо узнает о правде о своей реальности и о том, что он может изменить мир.",
        "Ссылка": "https://www.imdb.com/title/tt0133093/",
        "Жанр": "Фантастика"
    },
    4: {
        "Название": "Побег из Шоушенка",
        "Описание": "История о дружбе двух заключенных, которые пытаются сбежать из тюрьмы Шоушенк.",
        "Ссылка": "https://www.imdb.com/title/tt0111161/",
        "Жанр": "Драма"
    },
    5: {
        "Название": "Сияние",
        "Описание": "Писатель с семьей становится смотрителем у отеля, где начинают происходить странные события.",
        "Ссылка": "https://www.imdb.com/title/tt0081505/",
        "Жанр": "Ужасы"
    }, 
    6: {
        "Название": "Тупой и еще тупее",
        "Описание": "После того, как женщина оставляет портфель в терминале аэропорта, тупой водитель лимузина и его еще более тупой друг отправляются в веселую поездку по пересеченной местности в Аспен, чтобы вернуть его.",
        "Ссылка": "https://www.imdb.com/title/tt0109686/?ref_=ls_t_1",
        "Жанр" : "Комедия"
    },
    7: {
        "Название": "Красавица и чудовище",
        "Описание": "Принц, обреченный провести свои дни в образе отвратительного монстра, намеревается вернуть себе человечность, завоевав любовь молодой женщины.",
        "Ссылка": "https://www.imdb.com/title/tt0101414/?ref_=ls_t_5",
        "Жанр": "Романтика"
    }
}

def search(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1)
    
    try:
        n = int(message.text)  # Получаем число из сообщения
        
        if n in my_dict:
            movie = my_dict[n]
            response = f"Название: {movie['Название']}\n\nОписание: {movie['Описание']}\n\nСсылка: {movie['Ссылка']}"
            bot.send_message(message.chat.id, response, reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Фильм не найден. Пожалуйста, попробуйте другой номер.", reply_markup=markup)

    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное числовое значение.")

def searchGenre(message): 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1)

    # Маппинг жанров на их названия
    genre_map = {
        'Фантастика': "Фантастика",
        'Драма': "Драма",
        'Ужасы': "Ужасы",
        'Комедия': "Комедия",
        'Романтика': "Романтика"
    }

    genre_key = message.text.capitalize()  # Приводим текст сообщения к корректному формату
    response = ""

    if genre_key in genre_map:
        genre_name = genre_map[genre_key]
        response += f"Фильмы в жанре '{genre_name}':\n"
        found = False
        
        for movie in my_dict.values():
            if movie["Жанр"] == genre_name:
                response += f"- {movie['Название']}: {movie['Описание']}\n\nСсылка: {movie['Ссылка']}\n"
                found = True
        
        # Проверяем, были ли найдены фильмы
        if not found:
            response = f"Фильмы в жанре '{genre_name}' не найдены."

    else:
        response = "Пожалуйста, выберите другой жанр."

    bot.send_message(message.chat.id, response, reply_markup=markup)



def tgk(message):
    # Тут оставим ссылку на наш приватный тг канал
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("↩️ Назад в меню")
    markup.row(button1)

    bot.send_message(message.chat.id, 'Подпишись -> https://t.me/+DJTaOu_I6q9jMGVi', reply_markup=markup)


def settings(message):
    # Если хочешь, то дополни настройки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("↩️ Назад в меню")
    markup.row(button1)
    bot.send_message(message.chat.id, 'О проблемах писать -> @jansavitskiy', reply_markup=markup)

# Создаем базу данных при запуске бота
create_database()

# Запуск бота
bot.polling(none_stop=True)
