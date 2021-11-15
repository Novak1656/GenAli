from TOKEN import bot
from BUTTONs import Keyboard
from database import query
from pars import pars


keyboard = Keyboard()


@bot.message_handler(commands=['start'])
def start(message):
    markup = keyboard.start_keyboard()
    bot.send_message(message.from_user.id, "Добро пожаловать в GenshinAli!"
                                           " Выбери категорию товаров, которая тебя интересует.", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def char_list(message):
    markup = keyboard.char_list()
    type_prod_list = query.execute(""" SELECT name FROM product_type """).fetchall()
    bn_t = keyboard.get_btn_name(type_prod_list)
    char_name = query.execute(""" SELECT name FROM character """).fetchall()
    bn_n = keyboard.get_btn_name(char_name)
    global type

    for elm in bn_t:
        if message.text == elm:
            bot.send_message(message.from_user.id, "Выбери персонажа, товары с которым тебя интересуют. Или напиши его имя боту.",
                             reply_markup=markup)
            type = elm
            print(type)

    for el in bn_n:
        if message.text == el:
            enter_data = []
            enter_data.append(el)
            enter_data.append(type)
            print(type)
            show_prod = query.execute(""" SELECT name, link FROM product WHERE char=? and type=? """, enter_data).fetchall()
            prod = keyboard.get_prod(show_prod)
            print(prod)
            if len(prod) > 0:
                for pr in prod:
                    print(pr)
                    img, prise = pars(pr[1])
                    label = pr[0] + '\n\n' + 'Цена: ' + prise + '\n\n' + 'Ссылка на товар: ' + pr[1]
                    bot.send_photo(message.from_user.id, img, caption=label)
            else:
                bot.send_message(message.from_user.id, "К сожалению товаров с данным персонажем не найдено :(")

    if message.text == 'Назад':
        start(message)
    elif message.text == 'Посмотреть все':
        tp = []
        tp.append(type)
        all_prod = query.execute(""" SELECT name, link FROM product WHERE type=? """, tp).fetchall()
        prod = keyboard.get_prod(all_prod)
        for pr in prod:
            img, prise = pars(pr[1])
            label = pr[0] + '\n\n' + 'Цена: ' + prise + '\n\n' + 'Ссылка на товар: ' + pr[1]
            bot.send_photo(message.from_user.id, img, caption=label)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)