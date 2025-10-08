from telegram import InlineKeyboardMarkup,InlineKeyboardButton
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def one_button():
    keyboard = [
        # 1-kurs O'zbek guruhlari
        [InlineKeyboardButton("KI25-01 (o'zb, maxsus)", callback_data="uz:1:1")],
        [InlineKeyboardButton("KI25-02 (o'zb)", callback_data="uz:1:2")],
        [InlineKeyboardButton("KI25-03 (o'zb)", callback_data="uz:1:3")],
        [InlineKeyboardButton("KI25-04 (o'zb)", callback_data="uz:1:4")],
        [InlineKeyboardButton("KI25-05 (o'zb)", callback_data="uz:1:5")],
        
        [InlineKeyboardButton("DI25-07 (o'zb, maxsus)", callback_data="uz:1:6")],
        [InlineKeyboardButton("DI25-08 (o'zb)", callback_data="uz:1:7")],
        [InlineKeyboardButton("DI25-09 (o'zb)", callback_data="uz:1:8")],
        [InlineKeyboardButton("DI25-10 (o'zb)", callback_data="uz:1:9")],

        [InlineKeyboardButton("SI25-12 (o'zb)", callback_data="uz:1:10")],
        [InlineKeyboardButton("SI25-13 (o'zb)", callback_data="uz:1:11")],

        # 1-kurs Rus guruhlari (o‘zbekcha xabar)
        [InlineKeyboardButton("KI25-06 (rus)", callback_data="uz:1:12")],
        [InlineKeyboardButton("DI25-11 (rus)", callback_data="uz:1:13")],
        [InlineKeyboardButton("SI25-14 (rus)", callback_data="uz:1:14")],

        # Orqaga tugmasi
        [InlineKeyboardButton("⬅️ Orqaga", callback_data="uz:back:1")]
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def two_button():
    keyboard = [
        # 2-kurs O'zbek guruhlari
        [InlineKeyboardButton("KI24-01 (o'zb, maxsus)", callback_data="uz:2:15")],
        [InlineKeyboardButton("KI24-02 (o'zb)", callback_data="uz:2:16")],
        [InlineKeyboardButton("KI24-03 (o'zb)", callback_data="uz:2:17")],
        [InlineKeyboardButton("KI24-04 (o'zb)", callback_data="uz:2:18")],
        [InlineKeyboardButton("KI24-05 (o'zb)", callback_data="uz:2:19")],
        [InlineKeyboardButton("DI24-07 (o'zb, maxsus)", callback_data="uz:2:20")],
        [InlineKeyboardButton("DI24-08 (o'zb)", callback_data="uz:2:21")],
        [InlineKeyboardButton("DI24-09 (o'zb)", callback_data="uz:2:22")],
        [InlineKeyboardButton("DI24-10 (o'zb)", callback_data="uz:2:23")],
        [InlineKeyboardButton("SI24-12 (o'zb)", callback_data="uz:2:24")],
        [InlineKeyboardButton("SI24-13 (o'zb)", callback_data="uz:2:25")],

        # 2-kurs Rus guruhlari (o‘zbekcha xabar)
        [InlineKeyboardButton("KI24-06 (rus)", callback_data="uz:2:26")],
        [InlineKeyboardButton("DI24-11 (rus)", callback_data="uz:2:27")],
        [InlineKeyboardButton("SI24-14 (rus)", callback_data="uz:2:28")],

        # Orqaga tugmasi
        [InlineKeyboardButton("⬅️ Orqaga", callback_data="uz:back:1")]
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def tree_button():
    keyboard = [
        # O'zbek guruhlari
        [InlineKeyboardButton("KI23-01(o'zb,maxsus)", callback_data="uz:3:29")],
        [InlineKeyboardButton("KI23-02(o'zb)", callback_data="uz:3:30")],
        [InlineKeyboardButton("KI23-03(o'zb)", callback_data="uz:3:31")],
        [InlineKeyboardButton("KI23-04(o'zb)", callback_data="uz:3:32")],
        [InlineKeyboardButton("ATS23-06(o'zb)", callback_data="uz:3:33")],
        [InlineKeyboardButton("ATS23-07(o'zb)", callback_data="uz:3:34")],
        [InlineKeyboardButton("ATS23-09(o'zb)", callback_data="uz:3:35")],
        [InlineKeyboardButton("MT23-10(o'zb)", callback_data="uz:3:36")],
        [InlineKeyboardButton("SI23-18(o'zb)", callback_data="uz:3:37")],
        [InlineKeyboardButton("DI23-13(o'zb)", callback_data="uz:3:38")],
        [InlineKeyboardButton("DI23-14(o'zb)", callback_data="uz:3:39")],
        [InlineKeyboardButton("DI23-15(o'zb)", callback_data="uz:3:40")],

        # Rus guruhlari ham uz prefiksi bilan
        [InlineKeyboardButton("KI23-05(rus)", callback_data="uz:3:41")],
        [InlineKeyboardButton("MT23-12(rus)", callback_data="uz:3:42")],
        [InlineKeyboardButton("DI23-17(rus)", callback_data="uz:3:43")],

        # Orqaga tugmasi
        [InlineKeyboardButton("⬅️ Orqaga", callback_data="uz:back:1")]
    ]
    return InlineKeyboardMarkup(keyboard)


def four_button():
    keyboard = [
        [InlineKeyboardButton("KI22-01(o'zb)", callback_data="uz:4:44")],
        [InlineKeyboardButton("KI22-02(o'zb)", callback_data="uz:4:45")],
        [InlineKeyboardButton("KI22-03(o'zb)", callback_data="uz:4:46")],
        [InlineKeyboardButton("KI22-05 A(rus)", callback_data="uz:4:47")],
        [InlineKeyboardButton("KI22-05 B(rus)", callback_data="uz:4:48")],

        [InlineKeyboardButton("ATS22-06(o'zb)", callback_data="uz:4:49")],
        [InlineKeyboardButton("ATS22-07(o'zb)", callback_data="uz:4:50")],
        [InlineKeyboardButton("ATS22-08 A(rus)", callback_data="uz:4:51")],
        [InlineKeyboardButton("ATS22-08 B(rus)", callback_data="uz:4:52")],

        [InlineKeyboardButton("MT22-09(o'zb)", callback_data="uz:4:53")],
        [InlineKeyboardButton("MT22-10(rus)", callback_data="uz:4:54")],

        [InlineKeyboardButton("DI22-11(o'zb)", callback_data="uz:4:55")],
        [InlineKeyboardButton("DI22-12(o'zb)", callback_data="uz:4:56")],
        [InlineKeyboardButton("DI22-14 A(rus)", callback_data="uz:4:57")],
        [InlineKeyboardButton("DI22-14 B(rus)", callback_data="uz:4:58")],

        [InlineKeyboardButton("⬅️ orqaga", callback_data="uz:back:1")],
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)



def one_button_ru():
    keyboard = [
        # 1 курс узбекские группы
        [InlineKeyboardButton("KI25-01 (узб, спец)", callback_data="ru:1:1")],
        [InlineKeyboardButton("KI25-02 (узб)", callback_data="ru:1:2")],
        [InlineKeyboardButton("KI25-03 (узб)", callback_data="ru:1:3")],
        [InlineKeyboardButton("KI25-04 (узб)", callback_data="ru:1:4")],
        [InlineKeyboardButton("KI25-05 (узб)", callback_data="ru:1:5")],
        
        [InlineKeyboardButton("DI25-07 (узб, спец)", callback_data="ru:1:6")],
        [InlineKeyboardButton("DI25-08 (узб)", callback_data="ru:1:7")],
        [InlineKeyboardButton("DI25-09 (узб)", callback_data="ru:1:8")],
        [InlineKeyboardButton("DI25-10 (узб)", callback_data="ru:1:9")],

        [InlineKeyboardButton("SI25-12 (узб)", callback_data="ru:1:10")],
        [InlineKeyboardButton("SI25-13 (узб)", callback_data="ru:1:11")],

        # 1 курс русские группы
        [InlineKeyboardButton("KI25-06 (рус)", callback_data="ru:1:12")],
        [InlineKeyboardButton("DI25-11 (рус)", callback_data="ru:1:13")],
        [InlineKeyboardButton("SI25-14 (рус)", callback_data="ru:1:14")],

        # Кнопка назад
        [InlineKeyboardButton("⬅️ Назад", callback_data="ru:back:1")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def two_button_ru():
    keyboard = [
        # 2 курс узбекские группы
        [InlineKeyboardButton("KI24-01 (узб, спец)", callback_data="ru:2:15")],
        [InlineKeyboardButton("KI24-02 (узб)", callback_data="ru:2:16")],
        [InlineKeyboardButton("KI24-03 (узб)", callback_data="ru:2:17")],
        [InlineKeyboardButton("KI24-04 (узб)", callback_data="ru:2:18")],
        [InlineKeyboardButton("KI24-05 (узб)", callback_data="ru:2:19")],
        [InlineKeyboardButton("DI24-07 (узб, спец)", callback_data="ru:2:20")],
        [InlineKeyboardButton("DI24-08 (узб)", callback_data="ru:2:21")],
        [InlineKeyboardButton("DI24-09 (узб)", callback_data="ru:2:22")],
        [InlineKeyboardButton("DI24-10 (узб)", callback_data="ru:2:23")],
        [InlineKeyboardButton("SI24-12 (узб)", callback_data="ru:2:24")],
        [InlineKeyboardButton("SI24-13 (узб)", callback_data="ru:2:25")],

        # 2 курс русские группы
        [InlineKeyboardButton("KI24-06 (рус)", callback_data="ru:2:26")],
        [InlineKeyboardButton("DI24-11 (рус)", callback_data="ru:2:27")],
        [InlineKeyboardButton("SI24-14 (рус)", callback_data="ru:2:28")],

        # Кнопка назад
        [InlineKeyboardButton("⬅️ Назад", callback_data="ru:back:1")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def tree_button_ru():
    keyboard = [
        # Узбекские группы
        [InlineKeyboardButton("KI23-01(узб, спец)", callback_data="ru:3:29")],
        [InlineKeyboardButton("KI23-02(узб)", callback_data="ru:3:30")],
        [InlineKeyboardButton("KI23-03(узб)", callback_data="ru:3:31")],
        [InlineKeyboardButton("KI23-04(узб)", callback_data="ru:3:32")],
        [InlineKeyboardButton("ATS23-06(узб)", callback_data="ru:3:33")],
        [InlineKeyboardButton("ATS23-07(узб)", callback_data="ru:3:34")],
        [InlineKeyboardButton("ATS23-09(узб)", callback_data="ru:3:35")],
        [InlineKeyboardButton("MT23-10(узб)", callback_data="ru:3:36")],
        [InlineKeyboardButton("SI23-18(узб)", callback_data="ru:3:37")],
        [InlineKeyboardButton("DI23-13(узб)", callback_data="ru:3:38")],
        [InlineKeyboardButton("DI23-14(узб)", callback_data="ru:3:39")],
        [InlineKeyboardButton("DI23-15(узб)", callback_data="ru:3:40")],

        # Русские группы
        [InlineKeyboardButton("KI23-05(рус)", callback_data="ru:3:41")],
        [InlineKeyboardButton("MT23-12(рус)", callback_data="ru:3:42")],
        [InlineKeyboardButton("DI23-17(рус)", callback_data="ru:3:43")],

        # Кнопка назад
        [InlineKeyboardButton("⬅️ Назад", callback_data="ru:back:1")]
    ]
    return InlineKeyboardMarkup(keyboard)

def four_button_ru():
    keyboard = [
        [InlineKeyboardButton("KI22-01(узб)", callback_data="ru:4:44")],
        [InlineKeyboardButton("KI22-02(узб)", callback_data="ru:4:45")],
        [InlineKeyboardButton("KI22-03(узб)", callback_data="ru:4:46")],
        [InlineKeyboardButton("KI22-05 A(рус)", callback_data="ru:4:47")],
        [InlineKeyboardButton("KI22-05 B(рус)", callback_data="ru:4:48")],

        [InlineKeyboardButton("ATS22-06(узб)", callback_data="ru:4:49")],
        [InlineKeyboardButton("ATS22-07(узб)", callback_data="ru:4:50")],
        [InlineKeyboardButton("ATS22-08 A(рус)", callback_data="ru:4:51")],
        [InlineKeyboardButton("ATS22-08 B(рус)", callback_data="ru:4:52")],

        [InlineKeyboardButton("MT22-09(узб)", callback_data="ru:4:53")],
        [InlineKeyboardButton("MT22-10(рус)", callback_data="ru:4:54")],

        [InlineKeyboardButton("DI22-11(узб)", callback_data="ru:4:55")],
        [InlineKeyboardButton("DI22-12(узб)", callback_data="ru:4:56")],
        [InlineKeyboardButton("DI22-14 A(рус)", callback_data="ru:4:57")],
        [InlineKeyboardButton("DI22-14 B(рус)", callback_data="ru:4:58")],

        [InlineKeyboardButton("⬅️ Назад", callback_data="ru:back:1")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
