from telegram import InlineKeyboardButton,InlineKeyboardMarkup


def course_uz():
    
    keyboard = [
        [InlineKeyboardButton("Kursni tanlash",callback_data="course:uz")]
    ]
    return InlineKeyboardMarkup(keyboard)

def course_ru():
    
    keyboard = [
        [InlineKeyboardButton("Выберите курс",callback_data="course:ru")]
    ]
    return InlineKeyboardMarkup(keyboard)