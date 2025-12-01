import os
import json
import sys
from datetime import date

from telegram import Update
from telegram.ext import CallbackContext
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from app.models import Lesson, Group

def send_lesson(update: Update, context: CallbackContext):
    query = update.callback_query
    
    query.answer()
    
    try:
        lang, course_id, direction, day = query.data.split(':')
    except ValueError:
        query.message.reply_text("Noto'g'ri ma'lumot formati ❌")
        return

    # 3️⃣ JSON fayldan guruh nomini olish
    try:
        with open("database/lessons.json", 'r', encoding='utf-8') as file:
            lessons_json = json.load(file)
            group_name = lessons_json[lang][course_id][direction]['title']
    except FileNotFoundError:
        query.message.reply_text("Ma'lumotlar bazasi topilmadi ❌")
        return
    except KeyError as e:
        query.message.reply_text(f"Ma'lumotlar bazasida xatolik: {e} ❌")
        return
    except Exception as e:
        query.message.reply_text(f"JSON faylni o'qishda xatolik: {e} ❌")
        return

    # 4️⃣ Database'dan guruhni topish
    group_data = Group.objects.filter(name=group_name).first()
    if not group_data:
        query.message.reply_text(f'Guruh topilmadi: {group_name} ❌')
        return

    # 5️⃣ Hafta turi aniqlash
    try:
        start_date = date(2025, 9, 3)
        today = date.today()
        delta_days = (today - start_date).days
        week_number = delta_days // 7 + 1
        week_type_uz = "juft" if week_number % 2 == 0 else "toq"
    except Exception as e:
        query.message.reply_text(f"Hafta turi aniqlashda xatolik: {e} ❌")
        return

    # 6️⃣ Hafta kunini qisqartma formatga o'tkazish
    day_mapping = {
        "Dushanba": "du",
        "Seshanba": "se", 
        "Chorshanba": "ch",
        "Payshanba": "pa",
        "Juma": "ju",
        "Shanba": "sh"
    }
    
    weekday_short = day_mapping.get(day)
    if not weekday_short:
        query.message.reply_text(f'Noto‘g‘ri hafta kuni: {day} ❌')
        return

    # 7️⃣ Darslarni olish
    try:
        lessons = Lesson.objects.filter(
            group=group_data,
            weekday=weekday_short,
            week_type__in=[week_type_uz, "all"]
        ).order_by('time_pair')
    except Exception as e:
        query.message.reply_text(f'Darslarni olishda xatolik: {e} ❌')
        return

    # 8️⃣ Darslarni ko'rsatish
    if lessons:
        # Vaqt mapping
        time_mapping = {
            "1": "08:30–09:50",
            "2": "10:00–11:20", 
            "3": "11:30–12:50",
            "4": "13:30–14:50",
            "5": "15:00–16:20",
            "6": "16:30–17:50"
        }
        
        # Kun nomini o'zbekchaga o'tkazish
        day_names = {
            "du": "Dushanba",
            "se": "Seshanba",
            "ch": "Chorshanba", 
            "pa": "Payshanba",
            "ju": "Juma",
            "sh": "Shanba"
        }
        
        day_name_uz = day_names.get(weekday_short, day)
        week_type_text = "juft" if week_type_uz == "juft" else "toq"
        
        # Sarlavha
        query.message.reply_text(
            f"📅 *{day_name_uz} kuni dars jadvali*\n"
            f"👥 *Guruh:* {group_name}\n"
            f"🔁 *Hafta turi:* {week_type_text}\n"
            f"━━━━━━━━━━━━━━━━━━━━",
            parse_mode="Markdown"
        )
        
        # Har bir darsni ko'rsatish
        for lesson in lessons:
            time_display = time_mapping.get(lesson.time_pair, lesson.time_pair)
            
            text = (
                f"📘 *{lesson.name}*\n"
                f"👨‍🏫 {lesson.teacher}\n"
                f"🏫 {lesson.room}\n"
                f"⏰ {time_display}\n"
                f"━━━━━━━━━━━━━━━━━━━━"
            )
            query.message.reply_text(text, parse_mode="Markdown")
            
    else:
        query.message.reply_text(
            f"📅 *{day} kuni darslar topilmadi* ❌\n"
            f"👥 *Guruh:* {group_name}\n"
            f"🔁 *Hafta turi:* {'juft' if week_type_uz == 'juft' else 'toq'}",
            parse_mode="Markdown"
        )