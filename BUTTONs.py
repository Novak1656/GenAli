from telebot import types
from database import query


class Keyboard():

    @staticmethod
    def get_btn_name(btn_name):
        bt = []
        for elm in btn_name:
            bt.append(str(elm[0]))
        return bt

    @staticmethod
    def get_prod(show_prod):
        prod = []
        for i in show_prod:
            prod.append(list(i))
        return prod

    @staticmethod
    def start_keyboard():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_name = query.execute(""" SELECT name FROM product_type """).fetchall()
        bt = Keyboard.get_btn_name(btn_name)
        markup.add(*bt)
        return markup

    @staticmethod
    def char_list():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_all = types.KeyboardButton('Посмотреть все')
        btn_back = types.KeyboardButton('Назад')
        btn_name = query.execute(""" SELECT name FROM character ORDER BY name """).fetchall()
        bt = Keyboard.get_btn_name(btn_name)
        markup.add(btn_all, btn_back, *bt)
        return markup

