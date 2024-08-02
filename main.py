import sqlite3
import telebot
from telebot import types




TOKEN = "YOUR_TOKEN"  # Замените на токен вашего бота
bot = telebot.TeleBot(TOKEN)

# Создание базы данных и таблицы
def create_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY
        )
    ''')
    conn.commit()
    conn.close()

# Добавление пользователя в базу данных
def add_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO users (id) VALUES (?)', (user_id,))
    conn.commit()
    conn.close()


answers = "Перепроверь ещё раз свой запрос"  # Сообщение в случае неправильной комманды


@bot.message_handler(commands=["start"])
def welcome(message):                       # Функция welcome и главные кнопки меню
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # Какая-то фишка для работы кнопок                
    button3 = types.KeyboardButton('Поиск по коду')
    button4 = types.KeyboardButton('ТГК с фильмами')
    button5 = types.KeyboardButton('Настройки')           # Вывод кнопок на экран пользователю
    markup.row(button3, button4, button5)
    user_id = message.from_user.id
    add_user(user_id)

    if message.text == '/start':
        # Отправляю приветственный текст
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nМеня зовут ФИЛЬМОБОТ и я твой проводник в мир кино и сериалов :)\nДля начала выбери способ поиска фильма в меню ниже: ', reply_markup=markup)  # Приветственное сообщение пользователю, не забываем про markup
    else:
        bot.send_message(message.chat.id, 'Перекинул тебя в главное меню! Выбирай!', reply_markup=markup) # если пользователь по своему желанию зашёл в меню



@bot.message_handler(commands=['users_admin'])
def list_users(message):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM users')
    users = cursor.fetchall()
    conn.close()

    if users:
        user_ids = "\n".join(str(user[0]) for user in users)
        bot.send_message(message.chat.id, f"Сохраненные ID пользователей:\n{user_ids}")
    else:
        bot.send_message(message.chat.id, "Нет сохраненных пользователей.")


@bot.message_handler()
def info(message):
    if message.text == 'Поиск по коду':
        bot.send_message(message.chat.id, "Введите номер фильма:")
        bot.register_next_step_handler(message, search)
    elif message.text == 'ТГК с фильмами':
        tgk(message)  # Регистрируем следующий шаг
    elif message.text == 'Настройки':
        settings(message)
def search(message):
        n = int(message.text)  # Получаем число из сообщения
        my_dict = {
            1: {
                "Название": "Интерстеллар",
                "Описание": "Космическая одиссея о группе астронавтов, которые исследуют червоточину в поисках нового дома для человечества.",
                "Ссылка": "https://www.imdb.com/title/tt0816692/"
            },
            2: {
                "Название": "Начало",
                "Описание": "Вор, специализирующийся на краже идей, получает задание внедриться в сознание человека и изменить его мысли.",
                "Ссылка": "https://www.imdb.com/title/tt1375666/"
            },
            3: {
                "Название": "Матрица",
                "Описание": "Программист Нейо узнает о правде о своей реальности и о том, что он может изменить мир.",
                "Ссылка": "https://www.imdb.com/title/tt0133093/"
            },
            4: {
                "Название": "Побег из Шоушенка",
                "Описание": "История о дружбе двух заключенных, которые пытаются сбежать из тюрьмы Шоушенк.",
                "Ссылка": "https://www.imdb.com/title/tt0111161/"
            },
            5: {
                "Название": "Сияние",
                "Описание": "Писатель с семьей становится смотрителем у отеля, где начинают происходить странные события.",
                "Ссылка": "https://www.imdb.com/title/tt0081505/"
            }
        }

        if n in my_dict:
            movie = my_dict[n]
            response = f"Название: {movie['Название']}\nОписание: {movie['Описание']}\nСсылка: {movie['Ссылка']}"
            bot.send_message(message.chat.id, response)
        else:
            bot.send_message(message.chat.id, "Фильм не найден. Пожалуйста, попробуйте другой номер.")



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

def main():
    create_database()




bot.polling(none_stop=True)
