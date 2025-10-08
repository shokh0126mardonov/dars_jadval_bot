from telegram import InlineKeyboardMarkup,InlineKeyboardButton

def uz_course():
    keyboard = [
        [InlineKeyboardButton("1-kurs",callback_data="uz:1")],
        [InlineKeyboardButton("2-kurs",callback_data="uz:2")],
        [InlineKeyboardButton("3-kurs",callback_data="uz:3")],
        [InlineKeyboardButton("4-kurs",callback_data="uz:4")],
        [InlineKeyboardButton("◀️ orqaga",callback_data="back:uz")]
        ]
    
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def ru_course():
    keyboard = [
        [InlineKeyboardButton("1-курс", callback_data="ru:1")],
        [InlineKeyboardButton("2-курс", callback_data="ru:2")],
        [InlineKeyboardButton("3-курс", callback_data="ru:3")],
        [InlineKeyboardButton("4-курс", callback_data="ru:4")],
        [InlineKeyboardButton("◀️ назад",callback_data="back:ru")]
    ]
    return InlineKeyboardMarkup(keyboard)