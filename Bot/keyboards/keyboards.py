from aiogram.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def make_inline_keyboard(items: list[dict], placeholder: str = ""):
    inline_builder = InlineKeyboardBuilder()
    for item in items:
        inline_builder.add(InlineKeyboardButton(
            text=item['text'],
            callback_data=item['callback'],
            placeholder=placeholder
        ))
    return inline_builder

def make_template_keyboard(items: list[str]):
    buttons = [[KeyboardButton(text=item) for item in items]]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def cancel_button():
    return make_inline_keyboard([{"text": "Отмена", "callback": "cancel"}]).as_markup()

def exit_button():
    return make_inline_keyboard([{"text": "⬅️ Выход", "callback": "cancel"}]).as_markup()