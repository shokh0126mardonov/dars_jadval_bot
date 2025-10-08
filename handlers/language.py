from telegram import Update
from telegram.ext import CallbackContext
from keyboards import uz_course,ru_course,course_ru,course_uz

def get_language(update: Update, context: CallbackContext):
    callback_data = update.callback_query.data
    
    _,lang = callback_data.split(":")
    
    if lang == "uz":
        text = "🇺🇿 O'zbek tili tanlandi"
        course = course_uz()
    
    elif lang == "ru":
        text = "🇷🇺 выбран русский язык"
        course = course_ru()
        
    update.callback_query.answer(text)
    update.callback_query.message.reply_text(text,reply_markup=course)
    