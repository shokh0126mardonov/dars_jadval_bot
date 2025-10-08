from telegram import Update
from telegram.ext import CallbackContext
from keyboards import lang_button
from decorators import logger

@logger
def start(update: Update, context: CallbackContext):
    if update.message: 
        update.message.reply_text(
            text="Salom! Tilni tanlang \nПривет! Выберите язык:",
            reply_markup=lang_button()
        )
    elif update.callback_query: 
        update.callback_query.message.reply_text(
            text="Salom! Tilni tanlang \n\nПривет! Выберите язык:",
            reply_markup=lang_button()
        )