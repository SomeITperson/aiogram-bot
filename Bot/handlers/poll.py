from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from keyboards.keyboards import cancel_button, make_inline_keyboard
from keyboards.keyboards_config import cancel_button_list
from aiogram.fsm.state import State, StatesGroup

router = Router()

class PollState(StatesGroup):
    set_question = State()
    set_answers = State()
    set_true_answer = State()

@router.callback_query(Text("poll"))
async def poll_menu(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Создайте опрос",
        reply_markup=make_inline_keyboard([
            {"text": "Создать опрос", "callback": "create_poll"},
            {"text": "Назад", "callback": "cancel"}
        ]).as_markup())
    await state.set_state(PollState.set_question)
    await callback.answer(show_alert=False)

@router.callback_query(Text("create_poll"), PollState.set_question)
async def add_question(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Введите вопрос",
        reply_markup=cancel_button()
    )
    await state.set_state(PollState.set_answers)

@router.message(Text, PollState.set_answers)
async def add_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    btn_group = cancel_button_list.copy()

    if "question" not in data:
        await state.update_data(question=message.text, answers=[])

    if "answers" in data:
        if len(data['answers']) > 0:
            new_data = [d for d in data['answers']]
            new_data.append(message.text)
            await state.update_data(answers=new_data)
        else:
            await state.update_data(answers=[message.text])

    if "answer_index" not in data:
        btn_group.append({"text": "Выбрать правильный ответ", "callback": "chose_true_answer"})
    else:
        btn_group.append({"text": "Создать", "callback": "start_poll"})

    await message.answer(
        text=f"Добавление ответа-введите нужное количество ответов новыми сообщениями, а после добавьте правильынй ответ",
        reply_markup=make_inline_keyboard(btn_group).as_markup()
    )


@router.callback_query(Text("chose_true_answer"))
async def add_true_value(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Введите номер правильного ответа"
    )
    await state.set_state(PollState.set_true_answer)

@router.message(PollState.set_true_answer)
async def set_answer(message: Message, state: FSMContext):
    try:
        if type(int(message.text)) == int:
            await state.update_data(answer_index=int(message.text)-1)
            await state.set_state(PollState.set_answers)
            await message.answer(
                text="Нажмите 'Создать'",
                reply_markup=make_inline_keyboard([{"text": "Создать", "callback": "start_poll"}]).as_markup()
            )
    except:
        await state.set_state(PollState.set_answers)


@router.callback_query(Text("start_poll"))
async def cancel_poll(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await callback.message.answer_poll(
        question=data['question'],
        options=[answer for answer in data['answers']],
        type='quiz',
        correct_option_id=data['answer_index'],
        is_anonymous=False
    )
    await state.clear()