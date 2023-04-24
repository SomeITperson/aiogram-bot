from aiogram import Router, F
from aiogram.filters import Text, Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboards.keyboards import  cancel_button, exit_button
from api.api import convert
from keyboards.keyboards_config import converter_message

router = Router()

class GetConverter(StatesGroup):
    chose_first_currency = State()
    chose_second_currency = State()
    chose_quantity = State()

@router.callback_query(Text("converter"))
async def ask_currency_first(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Введите валюту, которую хотите перевести\nНапример, <b>EUR</b>",
        reply_markup=cancel_button()
    )
    await state.set_state(GetConverter.chose_first_currency)
    await callback.answer(show_alert=False)

@router.message(GetConverter.chose_first_currency)
async def ask_currency_second(message: Message, state: FSMContext):
    await state.update_data(first_currency=message.text)
    await message.answer(
        text="Введите валюту, в которую хотите перевести\nНапример, <b>RUB</b>",
        reply_markup=cancel_button()
    )
    await state.set_state(GetConverter.chose_second_currency)

@router.message(GetConverter.chose_second_currency)
async def ask_quantity(message: Message, state: FSMContext):
    await state.update_data(second_currency=message.text)
    data = await state.get_data()
    await message.answer(
        text=f"Введите количество <b>{data['first_currency'].upper()}</b>",
        reply_markup=cancel_button()
    )
    await state.set_state(GetConverter.chose_quantity)

@router.message(GetConverter.chose_quantity)
async def send_result(message: Message, state: FSMContext):
    await state.update_data(quantity=message.text)
    data = await state.get_data()
    try:
        if type(int(message.text)) == int:
            result = await convert(data['first_currency'], data['second_currency'], data['quantity'])
            await message.answer(
                text=converter_message.format(result['query']['amount'], result['query']['from'], result['result'], result['query']['to']),
                reply_markup=exit_button()
            )
            await state.clear()
    except ValueError:
        await message.answer(
                text=f"{message.text} не явлется числом, попробуйте снова",
                reply_markup=cancel_button()
            )