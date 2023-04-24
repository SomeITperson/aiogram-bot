start_msg = "<b>Выберите действие</b>:" + \
            "\n📍<b>Погода</b>-укажите название города и узнайте текущую погоду" + \
            "\n📍<b>Конвертер</b>-конвертируйте одну валюту в другую" + \
            "\n📍<b>Животные</b>-получите картинку с милым животным" + \
            "\n📍<b>Опрос</b>-создайте опрос в своём чате"

main_buttons = [
    {"text": "🌥️ Погода", "callback": "weather"},
    {"text": "💱 Конвертер", "callback": "converter"},
    {"text": "🐼 Животные", "callback": "animals"},
    {"text": "📋 Опрос", "callback": "poll"}
]

city_not_exists = [
    {"text": "🌥️ Повторить", "callback": "weather"},
    {"text": "⬅️ Выйти", "callback": "cancel"},
]

converter_not_exists = [
    {"text": " Повторить", "callback": "weather"},
    {"text": "⬅️ Выйти", "callback": "cancel"},
]

cancel_button_list = [
    {"text": "Отмена", "callback": "cancel"},
]

weather_message = "<b>Погода в городе <i>{}</i></b>\n🌡 <i>Температура:</i> {}C°\n💨 <i>Ветер:</i> {}м/с\n☁️ <i>Небо:</i> {}"

converter_message = "<b>{} {}</b> = <b>{} {}</b>"

animal_picture_urls = [
    "https://n1s1.hsmedia.ru/a1/ec/ec/a1ececc48afd3c0c498fdbd47ba45dbe/728x542_1_f5b22481fc08917ff7584d523f52ed21@1000x745_0xac120003_3944844451633381523.jpeg",
    "https://cs12.pikabu.ru/post_img/2022/03/06/4/1646543211115955008.jpg",
    "https://wildlife.by/upload/medialibrary/fe9/fe996a19393587a1a7d744ba4fbb44e3.jpg",
    "https://pustunchik.ua/uploads/school/cache/9a7adb79dd800aa15c3cc0e482e004c8.jpg",
    "https://avatars.akamai.steamstatic.com/cfcfe9619e92d5e26a2a0249956ca0676b9c75d6_full.jpg",
]