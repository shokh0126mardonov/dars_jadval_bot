from telegram.ext import Updater,CommandHandler,CallbackQueryHandler
from config import TOKEN
from handlers import start,get_language,one_course,two_course,uz_course_handler,ru_course_handler,tree_course,four_course,one_course_ru,two_course_ru,tree_course_ru,four_course_ru,days_uz,days_ru,back_direction,send_schedule_callback
from database import Base, engine
from database import Courses, Directions, Lesson 
from database import insert_course,insert_direction,insert_all_lessons,direction_map

Base.metadata.create_all(bind=engine)

insert_course()
insert_direction()
insert_all_lessons(r"C:\Users\М313\Desktop\1-kurs dars jadvali.docx",direction_map)



def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler('start',start))
    dispatcher.add_handler(CallbackQueryHandler(get_language,pattern=r'^lang:(uz|ru)$'))
    
    #Uzbek
    dispatcher.add_handler(CallbackQueryHandler(uz_course_handler,pattern=r"^course:uz$"))
    dispatcher.add_handler(CallbackQueryHandler(one_course,pattern=r"^uz:1$"))
    dispatcher.add_handler(CallbackQueryHandler(two_course,pattern=r"^uz:2$"))
    dispatcher.add_handler(CallbackQueryHandler(tree_course,pattern=r"^uz:3$"))
    dispatcher.add_handler(CallbackQueryHandler(four_course,pattern=r"^uz:4$"))
    dispatcher.add_handler(CallbackQueryHandler(days_uz, pattern=r"^uz:\d+:\d+$"))

    dispatcher.add_handler(
    CallbackQueryHandler(send_schedule_callback,pattern=r'^(uz|ru):[\w-]+:\d+:(Dushanba|Seshanba|Chorshanba|Payshanba|Juma|Shanba)$'))

    
    #Rus tili
    dispatcher.add_handler(CallbackQueryHandler(ru_course_handler,pattern=r"^course:ru$"))
    dispatcher.add_handler(CallbackQueryHandler(one_course_ru,pattern=r"^ru:1$"))
    dispatcher.add_handler(CallbackQueryHandler(two_course_ru,pattern=r"^ru:2$"))
    dispatcher.add_handler(CallbackQueryHandler(tree_course_ru,pattern=r"^ru:3$"))
    dispatcher.add_handler(CallbackQueryHandler(four_course_ru,pattern=r"^ru:4$"))
    dispatcher.add_handler(CallbackQueryHandler(days_ru, pattern=r"^ru:\d+:\d+$"))
    
    #Orqaga 
    dispatcher.add_handler(CallbackQueryHandler(start,pattern=r"^back:uz$"))
    dispatcher.add_handler(CallbackQueryHandler(start,pattern=r"^back:ru$"))
    dispatcher.add_handler(CallbackQueryHandler(uz_course_handler,pattern=r"^uz:back:1$"))
    dispatcher.add_handler(CallbackQueryHandler(ru_course_handler,pattern=r"^ru:back:1$"))
    dispatcher.add_handler(CallbackQueryHandler(back_direction, pattern=r"^(uz|ru):\d+:\d+:back$"))
    
    
    updater.start_polling()
    updater.idle()
    
if __name__ == "__main__":
    main()
    
