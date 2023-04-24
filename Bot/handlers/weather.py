from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboards.keyboards import make_inline_keyboard, cancel_button, exit_button
from api.api import get_weather
from keyboards.keyboards_config import weather_message, city_not_exists

router = Router()

class GetWeather(StatesGroup):
    chose_city = State()


@router.callback_query(Text("weather"))
async def ask_city(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="🌇 Напишите название города",
        reply_markup=cancel_button()
    )
    await state.set_state(GetWeather.chose_city)
    await callback.answer(show_alert=False)

@router.message(GetWeather.chose_city)
async def command_weather(message: Message, state: FSMContext):
    weather = await get_weather(message.text.lower())
    if not weather:
        await message.answer(
            text="Город не найден",
            reply_markup=make_inline_keyboard(city_not_exists).as_markup()
        )
    else:
        await message.answer(
            text=weather_message.format(
                weather[1]['ru'] if 'ru' in weather[1] else message.text,
                round(weather[0]['main']['temp']),
                weather[0]['wind']['speed'],
                weather[0]['weather'][0]['description']
            ),
            reply_markup=exit_button()
        )
        await state.set_state(GetWeather.chose_city)