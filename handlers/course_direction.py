from telegram import Update
from telegram.ext import CallbackContext
from keyboards import one_button,two_button,tree_button,four_button,one_button_ru,tree_button_ru,two_button_ru,four_button_ru

def one_course(update: Update,context: CallbackContext):
    update.callback_query.message.reply_text(
        "Yo'nalishingizni Tanlang!",reply_markup=one_button()
    )
    
def two_course(update: Update,context: CallbackContext):
    update.callback_query.message.reply_text(
        "Yo'nalishingizni Tanlang!",reply_markup=two_button()
    )
    
def tree_course(update: Update,context: CallbackContext):
    update.callback_query.message.reply_text(
        "Yo'nalishingizni Tanlang!",reply_markup=tree_button()
    )
    
def four_course(update: Update,context: CallbackContext):
    update.callback_query.message.reply_text(
        "Yo'nalishingizni Tanlang!",reply_markup=four_button()
    )
    
def one_course_ru(update: Update,context: CallbackContext):
    update.callback_query.message.reply_text(
        "Выбирайте свое направление!",reply_markup=one_button_ru()
    )
    
def two_course_ru(update: Update,context: CallbackContext):
    update.callback_query.message.reply_text(
        "Выбирайте свое направление!",reply_markup=two_button_ru()
    )
    
def tree_course_ru(update: Update,context: CallbackContext):
    update.callback_query.message.reply_text(
        "Выбирайте свое направление!",reply_markup=tree_button_ru()
    )
    
def four_course_ru(update: Update,context: CallbackContext):
    update.callback_query.message.reply_text(
        "Выбирайте свое направление!",reply_markup=four_button_ru()
    )
