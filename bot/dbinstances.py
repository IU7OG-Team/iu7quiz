"""
      ===== IU7QUIZ DATA BASE INSTANCES =====
      Copyright (C) 2020 IU7OG Team.

      В данном файле описсываются классы, доступные в
      базе данных (документы), используемые ботом и их поля.
"""

from mongoengine import Document, IntField, StringField, ListField


class Student(Document):
    """
        Класс, описывающий студента в БД.
    """

    user_id = IntField(required=True)
    login = StringField(required=True, max_length=200, default="None")
    group = StringField(required=True, max_length=200, default="None")
    meta = {"allow_inheritance": True}


class Question(Document):
    """
        Класс, описывающий вопрос и варианты ответа для него.
    """

    day = IntField(required=True)
    text = StringField(required=True, max_length=300)
    answers = ListField(StringField(required=True, max_length=100))
    correct_answer = StringField(required=True, max_length=1)
