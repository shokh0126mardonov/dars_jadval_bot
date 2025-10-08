from telegram import InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import CallbackContext
from telegram import Update 
from keyboards.direction import one_button,tree_button,two_button,four_button,one_button_ru,two_button_ru,tree_button_ru,four_button_ru
import json


def back_direction(update: Update, context: CallbackContext):
    message = update.callback_query.data
    if message.endswith(":back"):
        data = message.split(":")
        
        lang = data[0]
        course = data[1]
        direction = data[2]
        
        with open("database/lessons.json",'r') as file:
            users = file.read()
            lessons = json.loads(users)
            title = lessons[lang][course][direction]['title']
    
        
        if lang == "uz":
            if course == "1":
                kurs = one_button
            elif course == "2":
                kurs = two_button    
            elif course == "3":
                kurs = tree_button
            elif course == "4":
                kurs = four_button

            text="Yo'nalishingizni tanlang"
        elif  lang == "ru":
            if course == "1":
                kurs = one_button_ru
            elif course == "2":
                kurs = two_button_ru    
            elif course == "3":
                kurs = tree_button_ru
            elif course == "4":
                kurs = four_button_ru 
            text="Выберите направление"
                
        update.callback_query.message.reply_text(
            text = text,
            reply_markup=kurs()
        )