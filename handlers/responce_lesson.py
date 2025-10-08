from telegram import Update
from telegram.ext import CallbackContext
from database import LocalSession
from database.models import Courses, Directions, Lesson
import re

def clean_text(text: str) -> str:
    """Matndagi ortiqcha bo'sh joylarni olib tashlash"""
    if not text:
        return ""
    return re.sub(r'\s+', ' ', text).strip()

def send_schedule_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    try:
        # callback_data: "uz:KI25-01:Dushanba"
        lang, course_name, day = query.data.split(":")
    except ValueError:
        query.answer()
        query.message.reply_text("❌ Xato callback_data!")
        return

    db = LocalSession()

    # 1️⃣ Course nomidan id olish
    course_obj = db.query(Courses).filter(Courses.name == course_name).first()
    if not course_obj:
        query.message.reply_text(f"❌ {course_name} kursi topilmadi.")
        db.close()
        query.answer()
        return

    # 2️⃣ Shu course_id bilan Direction id olish
    direction_obj = db.query(Directions).filter(Directions.course_id == course_obj.id).first()
    if not direction_obj:
        query.message.reply_text(f"❌ {course_name} kursiga tegishli yo‘nalish topilmadi.")
        db.close()
        query.answer()
        return

    # 3️⃣ Lesson jadvalidan faqat shu kun va direction_id bo‘yicha olish
    lessons = db.query(Lesson).filter(
        Lesson.direction_id == direction_obj.id,
        Lesson.day == day
    ).order_by(Lesson.time).all()
    db.close()

    if not lessons:
        text = f"❌ {day} kuni uchun darslar topilmadi."
    else:
        text = f"📅 *{day} kuni dars jadvali* ({course_name}):\n\n"
        for idx, lesson in enumerate(lessons, start=1):
            time = clean_text(lesson.time)
            title = clean_text(lesson.title)
            teacher = clean_text(lesson.teacher)
            aud = clean_text(lesson.aud)
            text += f"⏰ {time} | 📚 {title} | 👨‍🏫 {teacher} | 🏫 {aud}\n"

    query.message.reply_text(text, parse_mode="Markdown")
    query.answer()
