from telegram import Update,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import CallbackContext
import json

def days_uz(update: Update,context: CallbackContext):
    message = update.callback_query.data
    data = message.split(":")
    
    lang = data[0]
    course = data[1]
    direction = data[2]
    
    keyboard = [
        [InlineKeyboardButton("Dushanba",callback_data=f"{lang}:{course}:{direction}:Dushanba")],
        [InlineKeyboardButton("Seshanba",callback_data=f"{lang}:{course}:{direction}:Seshanba")],
        [InlineKeyboardButton("Chorshanba",callback_data=f"{lang}:{course}:{direction}:Chorshanba")],
        [InlineKeyboardButton("Payshanba",callback_data=f"{lang}:{course}:{direction}:Payshanba")],
        [InlineKeyboardButton("Juma",callback_data=f"{lang}:{course}:{direction}:Juma")],
        [InlineKeyboardButton("Shanba",callback_data=f"{lang}:{course}:{direction}:Shanba")],
        [InlineKeyboardButton("⬅️ orqaga", callback_data=f"{lang}:{course}:{direction}:back")]
    ]
    
    reply_markup= InlineKeyboardMarkup(inline_keyboard=keyboard)
    
    
    with open("database/lessons.json",'r') as file:
        users = file.read()
        lessons = json.loads(users)
        title = lessons[lang][course][direction]['title']
    
    update.callback_query.message.reply_text(
        text=f"{title} guruh tanlandi kunni tanlang",reply_markup=reply_markup
    )
    
def days_ru(update: Update, context: CallbackContext):
    message = update.callback_query.data
    data = message.split(":")
    
    lang = data[0]       # "ru"
    course = data[1]
    direction = data[2]
    
    keyboard = [
        [InlineKeyboardButton("Понедельник", callback_data=f"{lang}:{course}:{direction}:Понедельник")],
        [InlineKeyboardButton("Вторник", callback_data=f"{lang}:{course}:{direction}:Вторник")],
        [InlineKeyboardButton("Среда", callback_data=f"{lang}:{course}:{direction}:Среда")],
        [InlineKeyboardButton("Четверг", callback_data=f"{lang}:{course}:{direction}:Четверг")],
        [InlineKeyboardButton("Пятница", callback_data=f"{lang}:{course}:{direction}:Пятница")],
        [InlineKeyboardButton("Суббота", callback_data=f"{lang}:{course}:{direction}:Суббота")],
        [InlineKeyboardButton("⬅️ назад", callback_data=f"{lang}:{course}:{direction}:back")]
    ]
    
    reply_markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    
    
    with open("database/lessons.json",'r') as file:
        users = file.read()
        lessons = json.loads(users)
        title = lessons[lang][course][direction]['title']
    
    update.callback_query.message.reply_text(
        text=f"{title} группа выбрана, теперь выберите день недели:",
        reply_markup=reply_markup
    )