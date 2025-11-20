import os
import json
import sys
from datetime import date

from telegram import Update
from telegram.ext import CallbackContext
import django

# Django sozlamalari
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from app.models import Course, Lesson, Group

def send_lesson(update: Update, context: CallbackContext):
    # 1️⃣ Hozirgi hafta turi aniqlash
    start_date = date(2025, 9, 3)  # 3-sentyabr boshlanishi
    today = date.today()
    delta_days = (today - start_date).days
    week_number = delta_days // 7 + 1
    week_type = "even" if week_number % 2 == 0 else "odd"

    query = update.callback_query
    query.answer()

    # callback_data format: "uz:1:1:Dushanba"
    lang, course_id, direction, day = query.data.split(':')

    # Course obyektini olish
    course_data = f"{course_id}_{lang}"
    try:
        course_obj = Course.objects.get(name=course_data)
    except Course.DoesNotExist:
        query.message.reply_text('Kurs topilmadi ❌')
        return

    # JSON fayldan title olish
    try:
        with open("database/lessons.json", 'r', encoding='utf-8') as file:
            lessons_json = json.load(file)
            title = lessons_json[lang][course_id][direction]['title']
    except (KeyError, FileNotFoundError):
        query.message.reply_text('Lesson ma\'lumotlari topilmadi ❌')
        return

    # Group obyektini olish
    group_data = Group.objects.filter(name=title, course=course_obj).first()
    if not group_data:
        query.message.reply_text('Guruh topilmadi ❌')
        return

    # Lesson obyektini olish
    lessons = Lesson.objects.filter(group=group_data,weekday = day.lower()[:2], week_type__in=[week_type, "all"]).all()
    if lessons:
        for lesson in lessons:

            text = (
                    f"📘 *Fan:* {lesson.name}\n"
                    f"👨‍🏫 *O‘qituvchi:* {lesson.teacher}\n"
                    f"🏫 *Xona:* {lesson.room}\n"
                    f"⏰ *Para:* {lesson.time_pair}"
                    )
            query.message.reply_text(text, parse_mode="Markdown")
  # kerak bo'lsa lessonning text atributini yozish mumkin
    else:
        query.message.reply_text('Dars topilmadi ❌')
