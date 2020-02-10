"""
      ===== IU7QUIZ BOT CONFIG =====
      Copyright (C) 2020 IU7OG Team.

      Настройки и константы для бота.
"""

from math import log
from datetime import datetime
import os

# Конфигурация серверной части бота.
TOKEN = os.environ['TOKEN']

# Конфигурация MongoDB.
DB_NAME = os.environ['DB_NAME']
DB_USER = os.environ['DB_USER']
DB_PASS = os.environ['DB_PASS']
DB_HOST = os.environ['DB_HOST']
DB_IP = os.environ['DB_IP']
HOST = f"mongodb://{DB_USER}:{DB_PASS}@{DB_HOST}:27017/{DB_NAME}"
SIDE_HOST = f"mongodb://{DB_USER}:{DB_PASS}@{DB_IP}:27017/{DB_NAME}"

# Конфигурация клиентской части бота.
GROUPS_BTNS = ("ИУ7-21Б", "ИУ7-22Б", "ИУ7-23Б",
               "ИУ7-24Б", "ИУ7-25Б", "ИУ7-26Б")
ANSWERS_BTNS = {"A": 1, "B": 2, "C": 3, "D": 4}
SCROLL_BTNS = ("◀️", "▶️")
READY_BTN = "Готов"
LB_MEDALS = {1: "🥇", 2: "🥈", 3: "🥉"}
LB_PAGE_SIZE = 10
LECTOR_ID = 414583310 # заменить
LIVE_Q_DELAY = 60
# Здесь указывается дата первой лекции, от нее ведется отсчет.
#FIRST_CLASS_DAY = datetime(2020, 2, 11, 8, 30)
FIRST_CLASS_DAY = datetime(2020, 2, 10, 23, 55)
CLASS_OFFSET = 14  # Время в днях до следующей лекции.
CLASS_DURATION = 5400  # Длительность лекции в секундах.

# Конфигурация рейтинговой системы.
# Коэффициенты главной формулы.
WAITING_FACTOR = 0.35
ANSWER_TIME_FACTOR = 1 - WAITING_FACTOR
ERR_DCRMNT_FACTOR = 0.2
COMPLEXITY_FACTOR = 0.2
SYMBOLS_PER_SECOND = 25

# Коэффициент потери баллов за ожидание (кол-во часов,
# когда из-за ожидания теряется 50% баллов за ожидание).
HALF_WAITING_HOURS = 12
HALF_WAITING_FACTOR = log(2) / HALF_WAITING_HOURS

# Конфигурация вебхука.

WEBHOOK_HOST = os.environ['DB_DOMAIN']
WEBHOOK_PORT = 8443
WEBHOOK_LISTEN = "0.0.0.0"

WEBHOOK_SSL_CERT = os.environ['SSL_CERT']
WEBHOOK_SSL_PRIV = os.environ['SSL_KEY']

WEBHOOK_URL_BASE = "https://{}:{}".format(WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(TOKEN)

# Флаг отладочной печати (если True, то она будет)
DEV_MODE_RATING = False
DEV_MODE_QUEUE = True

# Настройки времени.
#FIRST_QUESTION_DAY = datetime(2020, 2, 11, 10, 0)
FIRST_QUESTION_DAY = datetime(2020, 2, 10, 23, 55)
LB_TIMEOUT = 20

# Конфигурация парсера.
RECORD_SIZE = 6
# Конфигурация Google Spreadsheets API.
SCOPE = ["https://spreadsheets.google.com/feeds"]
SH_CREDENTIALS = os.environ['SH_CREDENTIALS']
SH_URL = os.environ['SH_URL']

# Информационные сообщения
INFO_MSG = "📮 *IU7QuizBot* by IU7OG Team 📮\n\n" \
    "Данный бот предназаначен для закрепления студентами лекционного материала " \
    "по курсу *Программирование на Си* в *МГТУ им. Н.Э. Баумана*, " \
    "на кафедре *ИУ7*.\n\n" \
    "🛠 Разработчики:\n" \
    "📍 Романов Алексей @mRRvz\n" \
    "📍 Пересторонин Павел @Justarone\n" \
    "📍 Кононенко Сергей @hackfeed\n" \
    "📍 Нитенко Михаил @VASYA\_VAN\n" \
    "📍 Якуба Дмитрий @xGULZAx\n\n" \
    "🔱 Все права защищены. 2020 год.\n" \
    "📡 [iu7og.design](https://iu7og.design) 📡\n"

RULES_MSG = "🤯 Система оценивания зависит от следующих факторов:\n\n" \
    "1. Время отклика боту.\n\n" \
    "2. Время ответа на вопрос.\n\n" \
    "3. Сложность вопроса (зависит от того, сколько людей ответили на вопрос с 1 раза).\n\n" \
    "4. Количество неправильных ответов на вопрос.\n\n" \
    "⚠️ *Четвертый* фактор весомее *второго*, поэтому лучше потратить больше времени, " \
    "но ответить правильно, чем наоборот\n\n" \
    "💡 Каждый день Вы получаете новый вопрос. " \
    "В случае правильного ответа с первого раза, " \
    "бот считает, что вы хорошо усвоили тему " \
    "и больше не задает этот вопрос.\n\n" \
    "🤔 Если же с 1 раза вам не удается ответить правильно, " \
    "то чтобы бот закончил задавать вопрос повторно " \
    "(такие вопросы задаются сразу после нового), нужно " \
    "доказать свои знания двумя подряд правильными ответами " \
    "на этот же вопрос. "

HELP_MSG = "❓ Не знаете, что делать❓\n" \
    "🥵 Вы можете:\n\n" \
    "1. Вызвать команду */question*, и после этого бот будет ждать от вас вопрос преподавателю " \
    "(доступно только во время лекций) 👨‍🏫\n\n" \
    "2. Вызвать команду */leaderboard*, чтобы узнать текущее положение дел в соревновании 🔝\n\n" \
    "3. Отправить простое сообщение боту. Правда пока он не умеет на них отвечать ☹️\n\n" \
    "4. Вызвать команду */info*, чтобы узнать информацию о команде " \
    "разработчиков (в случае каких-то проблем с ботом - пишите им!) и о проекте 📝\n\n" \
    "5. Вызвать команду */rules* и получить информацию о правилах оценивания и работы бота 📃\n"

# Количество вопросов, добавляемое за день
QUESTION_PORTION = 5
