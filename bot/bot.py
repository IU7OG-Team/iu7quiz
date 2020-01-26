"""
      ===== IU7QUIZ TELEGRAM BOT =====
      Copyright (C) 2020 IU7OG Team.

      Telegram-бот, помогающий студентам кафедры ИУ7 закрепить лекционный материал по курсу
      "Программирование на СИ", путём рассылки вопросов по прошедшим лекциям.
"""

from datetime import datetime
from functools import reduce

import time
import multiprocessing
import telebot
import schedule
import mongoengine

from dbinstances import Student, Question
from config import TOKEN, HOST, GROUPS_BTNS, ANSWERS_BTNS

bot = telebot.TeleBot(TOKEN)
mongoengine.connect(host=HOST)


def create_markup(buttons):
    """
        Создание клавиатуры из inline кнопок в два столбца.
    """

    markup = telebot.types.InlineKeyboardMarkup()

    for btn_odd, btn_even in zip(buttons[::2], buttons[1::2]):
        markup.add(
            telebot.types.InlineKeyboardButton(
                text=btn_odd, callback_data=btn_odd),
            telebot.types.InlineKeyboardButton(
                text=btn_even, callback_data=btn_even)
        )

    return markup


def schedule_message():
    """
        Планировщик сообщений.
    """
    def sending_messages():
        """
            Отправка сообщения.
        """

        question = Question.objects(day=datetime.today().weekday())[0]
        for student in Student.objects():
            bot.send_message(
                student.user_id,
                "❓ " + question.text + reduce(lambda x, y: x + "📌 " + y + "\n", question.answers, "\n\n"),
                reply_markup=create_markup(ANSWERS_BTNS)
            )

    schedule.every(1).minutes.do(sending_messages)
    while True:
        schedule.run_pending()
        time.sleep(1)


@bot.message_handler(commands=["start"])
def authorization(message):
    """
        Выбор учебной группы для авторизации.
    """

    if not Student.objects(user_id=message.from_user.id):
        bot.send_message(
            message.chat.id,
            "💬 Укажите свою учебную группу: ",
            reply_markup=create_markup(GROUPS_BTNS)
        )

    else:
        bot.send_message(
            message.chat.id, "⚠️ Вы уже зарегистрированы в системе.")



"""
@bot.message_handler(commands=["unreg"])
def delete(message):
    #Отладочная комманда.

    Question.objects().delete()
    question = Question(
        day=6,
        text="ФИО преподавателя, читающего лекции по Программированию в данном семестре: ",
        answers=
            ["A. Кострицкий Антон Александрович",
            "B. Кострицкий Александр Сергеевич",
            "C. Кострицкий Сергей Владимирович",
            "D. Кострицкий Игорь Владимирович"],
        correct_answer="B"
    )
    print(question.answers)
    question.save()

    print(message)
    print(Student.objects(user_id=message.from_user.id))
    Student.objects(user_id=message.from_user.id).delete()
    print(Student.objects(user_id=message.from_user.id))
"""



@bot.message_handler(commands=["leaderboard"])
def show_leaderboard(message):
    """
        Вывод лидерборда среди учеников.
    """

    if Student.objects(user_id=message.from_user.id):
        msg = ""
        for student in Student.objects():
            msg += "Логин: " + str(student.login) + \
                "\nГруппа: " + student.group + "\n"
    else:
        msg = "❌ Пожалуйста, укажите свою учебную группу."

    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=["help"])
def help_message(message):
    """
        Информация о боте.
    """

    bot.send_message(
        message.chat.id, "Тут напишем про себя и про преподавателей.")


# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     """
#         Задать вопрос преподавателю во время лекции.
#     """
#     bot.reply_to(message, "📮 Ваш вопрос принят!")


@bot.callback_query_handler(lambda call: call.data in GROUPS_BTNS)
def query_handler_reg(call):
    """
        Обработка нажатия inline-кнопок с выбором группы студентом.
    """

    bot.answer_callback_query(call.id)
    if not Student.objects(user_id=call.message.chat.id):
        student = Student(
            user_id=call.message.chat.id,
            login=call.message.chat.username,
            group=call.data
        )

        student.save()
        bot.send_message(call.message.chat.id,
                         "✅ Вы успешно зарегистрированы в системе.")


@bot.callback_query_handler(lambda call: call.data in ANSWERS_BTNS)
def query_handler_questions(call):
    """
        Обработка нажатия inline-кнопок с выбором ответа студентом.
    """

    bot.answer_callback_query(call.id)
    question = Question.objects(day=datetime.today().weekday())[0]
    if call.data == question.correct_answer:
        bot.send_message(call.message.chat.id, "Правильный ответ")
    else:
        bot.send_message(call.message.chat.id, "Неверный ответ")


if __name__ == "__main__":
    multiprocessing.Process(target=schedule_message, args=()).start()
    bot.polling()
