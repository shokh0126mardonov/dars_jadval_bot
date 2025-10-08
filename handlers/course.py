from telegram import Update
from telegram.ext import CallbackContext
from keyboards import uz_course,ru_course

def uz_course_handler(update: Update, context: CallbackContext):
    update.callback_query.message.reply_text(text="Kursni tanlang",reply_markup=uz_course())

def ru_course_handler(update: Update, context: CallbackContext):
    update.callback_query.message.reply_text(text="Выбрать курс",reply_markup=ru_course())