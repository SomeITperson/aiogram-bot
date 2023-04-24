from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup, CallbackQuery
from keyboards.keyboards import make_inline_keyboard
from keyboards.keyboards_config import main_buttons, start_msg

router = Router()

@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="<i>👋 Здравствуйте</i>!\n"+start_msg,
        reply_markup=make_inline_keyboard(main_buttons, placeholder="Выберите действие").as_markup(),
    )

@router.callback_query(Text("cancel"))
async def start(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text(
        text=start_msg,
        reply_markup=make_inline_keyboard(main_buttons, placeholder="Выберите действие").as_markup()
    )
    await callback.answer(
        show_alert=False
    )