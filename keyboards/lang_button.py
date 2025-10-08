from telegram import Update,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import CallbackContext

def lang_button():
    keyboard = [
                [
                InlineKeyboardButton("🇺🇿 Uzbek", callback_data="lang:uz"),
                InlineKeyboardButton("🇷🇺 Русский", callback_data="lang:ru")
                ]
            ]
    
    return InlineKeyboardMarkup(keyboard)