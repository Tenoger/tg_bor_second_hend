import sqlite3
import telebot
from telebot import types

bot = telebot.TeleBot('7945400484:AAFPbmcBBmh_v9pJKBxtFZI6pgnGL27M0UI')



stat = {}

def get_state(chat_id):
    if chat_id not in stat:
        stat.get(chat_id)
        stat[chat_id] = {
            'for_whom': '',
            'type_cloth': '',
            'category': '',
            'size': '',
            'client_id': '',
            'photos': [],
            'price': ''
        }
    return stat[chat_id]

def clear_user_state(chat_id):
    if chat_id in stat:
        stat[chat_id]['photos'] = []
        stat[chat_id] = {key: '' if key != 'photos' else [] for key in stat[chat_id].keys()}

def back_page_1(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Купить вещь')
    btn2 = types.KeyboardButton('Сдать вещь')
    btn3 = types.KeyboardButton('Информация')
    markup.row(btn1, btn2)
    markup.row(btn3)
    bot.send_message(message.chat.id, 'Привет!', reply_markup=markup)
    bot.register_next_step_handler(message, front_page1)

def back_page_2(message):
    markup1 = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Заполнить заявку на сдачу одежды')
    btn2 = types.KeyboardButton('Информация')
    btn3 = types.KeyboardButton('Назад')
    markup1.row(btn1)
    markup1.row(btn2, btn3)
    bot.send_message(message.chat.id, "Выбери", reply_markup=markup1)
    bot.register_next_step_handler(message, front_page2)

def back_page_3(message):
    btn1 = types.KeyboardButton('Мужчинам')
    btn2 = types.KeyboardButton('Женщинам')
    btn3 = types.KeyboardButton('Детям')
    btn4 = types.KeyboardButton('Отменить заявку')
    markup = types.ReplyKeyboardMarkup()
    markup.row(btn1, btn2, btn3)
    markup.row(btn4)
    bot.send_message(message.chat.id, "Выбери", reply_markup=markup)
    bot.register_next_step_handler(message, front_page3)

def back_page_4(message):
    state = get_state(message.chat.id)
    state['for_whom'] = message.text
    if message.text == "Детям":
        bt1 = types.InlineKeyboardButton("Спортивное", callback_data=f"{message.text} Спортивное")
        bt2 = types.InlineKeyboardButton("Новорождённым", callback_data=f"{message.text} Новорождённым")
        bt3 = types.InlineKeyboardButton("Одежда", callback_data=f"{message.text} Одежда")
        markup = types.InlineKeyboardMarkup()
        markup.row(bt2)
        markup.row(bt3)
        markup.row(bt1)
        bot.send_message(message.chat.id, f'Категории товаров {message.text}', reply_markup=markup)
    else:
        bt1 = types.InlineKeyboardButton("Сумки", callback_data=f"{message.text} Сумки")
        bt2 = types.InlineKeyboardButton("Нижнее бельё", callback_data=f"{message.text} Нижнее бельё")
        bt3 = types.InlineKeyboardButton("Спортивное", callback_data=f"{message.text} Спортивное")
        bt4 = types.InlineKeyboardButton("+Size", callback_data=f"{message.text} +Size")
        bt5 = types.InlineKeyboardButton("Одежда", callback_data=f"{message.text} Одежда")
        bt6 = types.InlineKeyboardButton("Бижутерия", callback_data=f"{message.text} Бижутерия")
        markup = types.InlineKeyboardMarkup()
        markup.row(bt5)
        markup.row(bt1, bt3)
        markup.row(bt2, bt4, bt6)
        bot.send_message(message.chat.id, f'Категории товаров {message.text}', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def back_page_5(callback):
    state = get_state(callback.message.chat.id)

    chat_id = callback.message.chat.id
    if callback.data.startswith("prev_"):
        offset = int(callback.data.split("_")[1])
        category = user_states[chat_id]['category']
        subcategory = user_states[chat_id]['subcategory']
        search_products_with_images(chat_id, category, subcategory, offset=offset)
    elif callback.data.startswith("next_"):
        offset = int(callback.data.split("_")[1])
        category = user_states[chat_id]['category']
        subcategory = user_states[chat_id]['subcategory']
        search_products_with_images(chat_id, category, subcategory, offset=offset)
    elif callback.data.startswith("buy_"):
        bot.answer_callback_query(callback.id, "Товар добавлен в корзину.")
        bot.send_message(chat_id,
                         "Оплату производить по данным реквизитам:2201 7039 4832 0303\nВ комментариях к переводу требуется указать название и стоимость товара\nДля завершения покупки сначала отправьте адрес и следующим сообщением скриншот оплаты.")

        user_states[chat_id] = ['waiting_for_address_and_payment']
    elif callback.data == "back":
        show_categories(callback.message)
    if "Одежда" in callback.data:
        state['category'] = "Одежда"
        if "Мужчинам" in callback.data:
            bt1 = types.KeyboardButton('Брюки')
            bt2 = types.KeyboardButton('Верхняя одежда')
            bt3 = types.KeyboardButton('Джемперы, свитеры и кардиганы')
            bt4 = types.KeyboardButton('Джинсы')
            bt5 = types.KeyboardButton('Домашняя одежда')
            bt6 = types.KeyboardButton('Комбинезоны')
            bt7 = types.KeyboardButton('Костюмы и комплекты')
            bt8 = types.KeyboardButton('Носки')
            bt9 = types.KeyboardButton('Пиджаки, жакеты и жилеты')
            bt10 = types.KeyboardButton('Рубашки')
            bt11 = types.KeyboardButton('Термобельё')
            bt12 = types.KeyboardButton('Толстовки, свитшоты и худи')
            bt13 = types.KeyboardButton('Футболки и майки')
            bt14 = types.KeyboardButton('Шорты')
            markup = types.ReplyKeyboardMarkup()
            markup.row(bt1, bt2, bt3)
            markup.row(bt4, bt5, bt6)
            markup.row(bt7, bt8, bt9)
            markup.row(bt10, bt11, bt12)
            markup.row(bt13, bt14)
            bot.send_message(callback.message.chat.id, "Что именно?", reply_markup=markup)
            bot.register_next_step_handler(callback.message, front_page_5)
        elif "Женщинам" in callback.data:
            bt1 = types.KeyboardButton('Блузы и рубашки')
            bt2 = types.KeyboardButton('Брюки, джинсы и капри')
            bt3 = types.KeyboardButton('Верхняя одежда')
            bt4 = types.KeyboardButton('Джемперы, свитеры и кардиганы')
            bt5 = types.KeyboardButton('Домашняя одежда')
            bt6 = types.KeyboardButton('Комбинезоны')
            bt7 = types.KeyboardButton('Костюмы и комплекты')
            bt8 = types.KeyboardButton('Носки,чулки и колготки')
            bt9 = types.KeyboardButton('Майки и топы')
            bt10 = types.KeyboardButton('Пиджаки, жакеты и жилеты')
            bt11 = types.KeyboardButton('Платья и сарафаны')
            bt12 = types.KeyboardButton('Купальники и пляжная одежда')
            bt13 = types.KeyboardButton('Свадебная одежда')
            bt14 = types.KeyboardButton('Шорты')
            bt15 = types.KeyboardButton('Толстовки, свитшоты и худи')
            bt16 = types.KeyboardButton('Футболки и топы')
            bt17 = types.KeyboardButton('Юбки')
            bt18 = types.KeyboardButton('Джинсы и джеггинсы')
            bt19 = types.KeyboardButton('Для беременных')
            markup = types.ReplyKeyboardMarkup()
            markup.row(bt1, bt2, bt3)
            markup.row(bt4, bt5, bt6)
            markup.row(bt7, bt8, bt9)
            markup.row(bt10, bt11, bt12)
            markup.row(bt13, bt14, bt15)
            markup.row(bt16, bt17, bt18, bt19)
            bot.send_message(callback.message.chat.id, "Что именно?", reply_markup=markup)
            bot.register_next_step_handler(callback.message, front_page_5)
        elif "Детям" in callback.data:
            bt1 = types.KeyboardButton('Блузы и рубашки ')
            bt2 = types.KeyboardButton('Брюки и джинсы')
            bt3 = types.KeyboardButton('Верхняя одежда')
            bt4 = types.KeyboardButton('Джемперы и кардиганы')
            bt5 = types.KeyboardButton('Домашняя одежда')
            bt6 = types.KeyboardButton('Комбинезоны')
            bt7 = types.KeyboardButton('Костюмы и комплекты')
            bt8 = types.KeyboardButton('Носки')
            bt9 = types.KeyboardButton('Майки и топы')
            bt10 = types.KeyboardButton('Пиджаки и жакеты')
            bt11 = types.KeyboardButton('Платья и сарафаны')
            bt12 = types.KeyboardButton('Купальники и пляжная одежда')
            bt13 = types.KeyboardButton('Термобелье')
            bt14 = types.KeyboardButton('Шорты')
            bt15 = types.KeyboardButton('Толстовки и свитшоты')
            bt16 = types.KeyboardButton('Футболки и лонгсливы')
            bt17 = types.KeyboardButton('Юбки')
            markup = types.ReplyKeyboardMarkup()
            markup.row(bt1, bt2, bt3)
            markup.row(bt4, bt5, bt6)
            markup.row(bt7, bt8, bt9)
            markup.row(bt10, bt11, bt12)
            markup.row(bt13, bt14, bt15)
            markup.row(bt16, bt17)
            bot.send_message(callback.message.chat.id, "Что именно?", reply_markup=markup)
            bot.register_next_step_handler(callback.message, front_page_5)


    elif any(
            x in callback.data for x in ["Спортивное", "Новорождённым", "Сумки", "Нижнее бельё", "+Size", "Бижутерия"]):
        state['category'] = callback.data
        front_page_5(message=callback.message)


def back_page_9(message):
    bt1 = types.KeyboardButton('Отправить заявку')
    bt2 = types.KeyboardButton('Отменить заявку')
    markup = types.ReplyKeyboardMarkup()
    markup.row(bt1, bt2)
    bot.send_message(message.chat.id, "Выбери", reply_markup=markup)
    bot.register_next_step_handler(message, front_page_10)


@bot.message_handler(commands=['start'])
def Menu(message):
    clear_user_state(message.chat.id)
    back_page_1(message)


def front_page1(message):
    if message.text == "Сдать вещь":
        back_page_2(message)
    elif message.text == "Купить вещь":
        show_categories(message)
    elif message.text == "Информация":
        bot.send_message(message.chat.id,
                         "Здесь вам нужно выбрать, что вы хотите, сдать ненужную вещь или приобрести новую")
        back_page_1(message)
    else:
        Menu(message)

def front_page2(message):
    if message.text == "Заполнить заявку на сдачу одежды":
        back_page_3(message)

    elif message.text == "Информация":
        bot.send_message(message.chat.id,
                         "Чтобы иметь возможность сдать вещь в онлайн секонд хенд, необходимо заполнить соответсвующую заявку, где нужно указать все требуемые характеристики вашей вещи и дождаться ответа администратора бота. Спасибо, что пользуетесь нашим ботом! ")
        back_page_2(message)

    elif message.text == "Назад":
        Menu(message)

    else:
        back_page_2(message)


def front_page3(message):
    if message.text == 'Мужчинам':
        back_page_4(message)
        return
    elif message.text == 'Женщинам':
        back_page_4(message)
        return
    elif message.text == 'Детям':
        back_page_4(message)
        return

    elif message.text == "Отменить заявку":
        Menu(message)
        return
    else:
        back_page_3(message)


def front_page4(message):
    back_page_5(message)


def front_page_5(message):
    state = get_state(message.chat.id)
    state['type_cloth'] = message.text

    bt1 = types.KeyboardButton('Информация')
    bt2 = types.KeyboardButton('Отменить заявку')
    markup = types.ReplyKeyboardMarkup()
    markup.row(bt1, bt2)
    bot.send_message(message.chat.id,
                     "Пришлите фотографи(ю/и) вашей вещи. Пожалуйста, присылайте фотографии по одной. Максимальное количество фотографий - 5.",
                     reply_markup=markup)
    bot.register_next_step_handler(message, page_6)


def page_6(message):
    state = get_state(message.chat.id)
    if message.text == 'Информация':
        bot.send_message(message.chat.id, "Теперь вам нужно прислать фотографию вещи, которую вы хотите сдать")
        bot.register_next_step_handler(message, page_6)
    elif message.text == 'Отменить заявку':
        Menu(message)
    elif message.text == 'Это все фото':
        page_7(message)
        return

    else:
        if (message.photo != None):
            a = []
            state['photos'].append(message.photo[0].file_id)
            bt1 = types.KeyboardButton('Информация')
            bt2 = types.KeyboardButton('Это все фото')
            bt3 = types.KeyboardButton('Отменить заявку')
            markup = types.ReplyKeyboardMarkup()
            markup.row(bt1, bt2)
            markup.row(bt3)
            if len(state['photos']) <= 5:
                bot.send_message(message.chat.id,
                             f"Вы можете прислать еще {5 - len(state['photos'])} фото",
                             reply_markup=markup)
            else:
                page_7(message)
                return
            bot.register_next_step_handler(message, page_6)
        else:
            front_page_5(message)


def page_7(message):
    bt1 = types.KeyboardButton('Отменить заявку')
    markup = types.ReplyKeyboardMarkup()
    markup.row(bt1)
    bot.send_message(message.chat.id, "Напишите размер вашей вещи, если он имеется. Иначе напишите '-' ",
                     reply_markup=markup)
    bot.register_next_step_handler(message, page_8)


def page_8(message):
    state = get_state(message.chat.id)
    state['size'] = message.text
    if message.text == 'Отменить заявку':
        Menu(message)
        return
    bt1 = types.KeyboardButton('Отменить заявку')
    markup = types.ReplyKeyboardMarkup()
    markup.row(bt1)
    bot.send_message(message.chat.id,
                     f"Напишите сумму в рублях, которую бы вы хотели получить за этот товар(требуется написать только число)",
                     reply_markup=markup)
    bot.register_next_step_handler(message, front_page_9)


def front_page_9(message):
    state = get_state(message.chat.id)
    if message.text is not None:
        if all(x in '0123456789' for x in message.text):
            state['price'] = message.text
            if message.text == 'Отменить заявку':
                Menu(message)
                return
            else:
                back_page_9(message)
        else:
            bot.send_message(message.chat.id, f"Нужно написать только число без других символов")
            page_8(message)
    else:
        bot.send_message(message.chat.id, f"Нужно написать только число")
        page_8(message)

def front_page_10(message):
    state = get_state(message.chat.id)
    if message.text == 'Отменить заявку':
        stat['photos'] = []
        Menu(message)
        return
    elif message.text == 'Отправить заявку':
        bot.send_message(message.chat.id, f"Ваша заявка принята и будет рассмотрена!\
                                               Решение о принятии заявки вам напишет администратор\
                                              онлайн-секодхенда в личные сообщения")
        photos_in_message = []
        for i in range(len(state['photos'])):
            if i == 0:
                photos_in_message.append(telebot.types.InputMediaPhoto(state['photos'][i],
                                                                       f"Для кого: {state['for_whom']} \nТип одежды: {state['type_cloth']} \nКатегория: {state['category']} \nРазмер: {state['size']} \nЦена: {state['price']}р \nКлиент: @{message.chat.username}"))
            else:
                photos_in_message.append(telebot.types.InputMediaPhoto(state['photos'][i]))

        bot.send_media_group(1108099611, photos_in_message)
        Menu(message)
    else:
        back_page_9(message)




#-------------------------------------------------------------------------------------


user_states = {}

def create_db():
    conn = sqlite3.connect('shop.db')
    cur = conn.cursor()

    cur.execute(''' 
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        category TEXT,
        subcategory TEXT,
        image_path TEXT
    )
    ''')

    products = [
        ('Футболка мужская 500р', 'Мужчинам🧔', 'Футболки', 'images/men_tshirtspng.png'),
        ('Футболка мужская бесценна', 'Мужчинам🧔', 'Футболки', 'images/завр.png'),
        ('Штаны мужские 1000р', 'Мужчинам🧔', 'Штаны', 'images/насрал в штаны.png'),
        ('Шорты мужские 1500р', 'Мужчинам🧔', 'Штаны', 'images/дырявчики .png'),
        ('Нижнее бельё мужское 1000р', 'Мужчинам🧔', 'Нижнее бельё', 'images/избовичи.png'),
        ('Нижнее бельё мужское 1500р', 'Мужчинам🧔', 'Нижнее бельё', 'images/trusijpg.jpg'),
        ('Футболка женская 15000р', 'Женщинам👩', 'Футболки', 'images/жен фут.png'),
        ('Футболка женская 15р', 'Женщинам👩', 'Футболки', 'images/futjen.jpg'),
        ('Штаны женские 30000р', 'Женщинам👩', 'Штаны', 'images/мешок.png'),
        ('Шорты женские 300р', 'Женщинам👩', 'Штаны', 'images/жен.png'),
        ('Нижнее бельё женское 10р', 'Женщинам👩', 'Нижнее бельё', 'images/чьи.png'),
        ('Нижнее бельё женское 100р', 'Женщинам👩', 'Нижнее бельё', 'images/trusi3.jpg'),
        ('Футболка детская 500р', 'Детям👦', 'Футболки', 'images/евротрак.png'),
        ('Платье детское 50000р', 'Детям👦', 'Футболки', 'images/я дитя.png'),
        ('Штаны детские 10000р', 'Детям👦', 'Штаны', 'images/шаровары.png'),
        ('Штаны детские 100р', 'Детям👦', 'Штаны', 'images/адидас.jpg'),
    ]

    cur.executemany('INSERT INTO products (name, category, subcategory, image_path) VALUES (?, ?, ?, ?)', products)

    conn.commit()
    cur.close()
    conn.close()


create_db()


def search_products_with_images(chat_id, category=None, subcategory=None, offset=0):
    if not category or not subcategory:
        bot.send_message(chat_id, "Ошибка: сначала выберите категорию и подкатегорию.")
        return

    conn = sqlite3.connect('shop.db')
    cur = conn.cursor()

    query = "SELECT * FROM products WHERE category = ? AND subcategory = ? LIMIT 1 OFFSET ?"
    cur.execute(query, (category, subcategory, offset))
    product = cur.fetchone()

    cur.execute("SELECT COUNT(*) FROM products WHERE category = ? AND subcategory = ?", (category, subcategory))
    total_products = cur.fetchone()[0]

    if product:
        product_id, name, category, subcategory, image_path = product

        if chat_id in user_states and 'last_message_id' in user_states[chat_id]:
            try:
                bot.delete_message(chat_id, user_states[chat_id]['last_message_id'])
            except:
                pass


        markup = types.InlineKeyboardMarkup()
        if offset > 0:
            prev_button = types.InlineKeyboardButton("⬅️ Назад", callback_data=f"prev_{offset - 1}")
            markup.add(prev_button)
        if offset + 1 < total_products:
            next_button = types.InlineKeyboardButton("➡️ Вперед", callback_data=f"next_{offset + 1}")
            markup.add(next_button)

        buy_button = types.InlineKeyboardButton("🛒 Купить", callback_data=f"buy_{product_id}")
        exit_button = types.InlineKeyboardButton("🔙 Назад", callback_data="back")
        markup.add(buy_button, exit_button)

        with open(image_path, 'rb') as image_file:
            message = bot.send_photo(
                chat_id,
                image_file,
                caption=f"**{name}**\nКатегория: {category}\nПодкатегория: {subcategory}",
                parse_mode='Markdown',
                reply_markup=markup
            )
        user_states[chat_id]['last_message_id'] = message.message_id

    else:
        bot.send_message(chat_id, "Нет товаров, соответствующих заданным критериям.")

    cur.close()
    conn.close()

@bot.message_handler(func=lambda message: message.text == 'Назад')
def go_back_to_main_menu(message):
    Menu(message)


@bot.message_handler(func=lambda message: message.text == 'Назад' and 'category' in user_states.get(message.chat.id, {}))
def go_back_to_categories(message):
    category = user_states[message.chat.id]['category']
    show_categories(message)


@bot.message_handler(func=lambda message: message.text in ['Купить одежду'])
def show_categories(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Мужчинам🧔', 'Женщинам👩', 'Детям👦')
    markup.row('Назад')
    bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ['Мужчинам🧔', 'Женщинам👩', 'Детям👦'])
def show_subcategories(message):
    category = message.text
    user_states[message.chat.id] = {'category': category}
    markup = types.ReplyKeyboardMarkup()
    subcategories = {
        'Мужчинам🧔': ['Футболки', 'Штаны', 'Нижнее бельё'],
        'Женщинам👩': ['Футболки', 'Штаны', 'Нижнее бельё'],
        'Детям👦': ['Футболки', 'Штаны']
    }
    for subcategory in subcategories[category]:
        markup.add(subcategory)
    markup.add('Назад')
    bot.send_message(message.chat.id, f"Выберите подкатегорию для {category}:", reply_markup=markup)




@bot.message_handler(func=lambda message: message.text in ['Футболки', 'Штаны', 'Нижнее бельё'])
def show_products(message):
    chat_id = message.chat.id
    subcategory = message.text
    user_states[chat_id]['subcategory'] = subcategory
    search_products_with_images(chat_id, category=user_states[chat_id]['category'], subcategory=subcategory)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    chat_id = message.chat.id
    state = user_states.get(chat_id, [])

    if 'waiting_for_address_and_payment' in state:
        address = message.text
        user_states[chat_id].append({'address': address})

        bot.send_message(chat_id, "Адрес сохранён. Отправьте скриншот оплаты.")
        user_states[chat_id] = ['waiting_for_payment_screenshot', {'address': address}]


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    chat_id = message.chat.id
    state = user_states.get(chat_id, [])

    if 'waiting_for_payment_screenshot' in state:
        photo_id = message.photo[-1].file_id

        address = user_states[chat_id][1]['address']
        user_id = message.chat.id

        bot.send_message(
            6829429413,
            f"Новый заказ!\n"
            f"Пользователь: @{message.chat.username}\n"
            f"Telegram ID: {user_id}\n"
            f"Адрес: {address}\n"
        )

        bot.send_photo(
            6829429413,
            photo_id,
            caption="Подтверждение оплаты"
        )

        bot.send_message(chat_id, "С вами скоро свяжется администратор бота. Спасибо за покупку!")

        bot.send_message(chat_id, "Вы вернулись в главное меню:")
        user_states[chat_id] = []
        Menu(message)


bot.polling(none_stop=True)