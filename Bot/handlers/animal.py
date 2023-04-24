from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from keyboards.keyboards import make_inline_keyboard
from aiogram.utils.markdown import hide_link
from keyboards.keyboards_config import animal_picture_urls
from random import randint

router = Router()


@router.callback_query(Text("animals"))
async def send_animal(callback: CallbackQuery, state: FSMContext):

    while True:
        rand_index = randint(0, len(animal_picture_urls) - 1)
        state_data = await state.get_data()
        if "current_id" not in state_data:
            break
        if rand_index != state_data['current_id']:
            state.update_data(current_id = rand_index)
            break

    await callback.message.edit_text(
        text=f"{hide_link(animal_picture_urls[rand_index])}"
            f"🐼",
        reply_markup=make_inline_keyboard([
            {"text": "🔄 Повторить", "callback": "animals"},
            {"text": "⬅️ Выход", "callback": "cancel"},
        ]).as_markup()
    )
    await callback.answer(show_alert=False)