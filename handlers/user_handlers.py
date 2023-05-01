from aiogram import Router, F
from aiogram.filters import CommandStart, Text, Command, StateFilter
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.memory import MemoryStorage

from database.db_config import DATABASE_URL, get_async_engine, get_async_sessionmaker
from keyboards.inline_keyboards import inline_access_keyboard
from keyboards.keyboard import get_phone_kb
from lexicon.lexicon import LEXICON_RU
from utils.bd_requests import insert_into_db, is_phone_valid

storage: MemoryStorage = MemoryStorage()

router: Router = Router()

engine = get_async_engine(DATABASE_URL)
async_session = get_async_sessionmaker(engine)

class FSMuserstatus(StatesGroup):
    is_valid_person = State()



class FSMfillform(StatesGroup):
    fill_phone: State = State()
    want_work_mode: State = State()
    work_mode: State = State()


@router.message(CommandStart(), StateFilter(default_state))
async def command_start(message: Message, state: FSMContext):
    await message.answer(LEXICON_RU['/start'], reply_markup=get_phone_kb())
    await state.set_state(FSMfillform.fill_phone)


@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def command_cancel(message: Message, state: FSMContext):
    await message.answer('❌Вы отменили регистрацию❌')
    await state.clear()


@router.message(F.contact, StateFilter(FSMfillform.fill_phone))
async def command_phone(message: Message, state: FSMContext):
    print(message.contact.phone_number)
    if is_phone_valid(f'+{message.contact.phone_number}'):
        await message.answer('Верно вы являетесь водителем Данного таксопарка!', reply_markup=ReplyKeyboardRemove())
        res = await insert_into_db(str(message.from_user.id), message.contact.phone_number)
        if isinstance(res, str):
            await message.answer(res)
            await state.clear()
        else:
            await state.set_state(FSMfillform.want_work_mode)
            keyboard = inline_access_keyboard()
            await message.answer('Хотите ли вы начать поиск активных заказов?',
                                 reply_markup=keyboard)
    else:
        await message.answer('Вы не водитель этого таксопарка!')
        await state.clear()


@router.message(StateFilter(FSMfillform.fill_phone))
async def wrong_command_phone(message: Message):
    await message.answer('🔽Отправьте номер через кнопку снизу🔽')


@router.callback_query(StateFilter(FSMfillform.want_work_mode), Text(text='YES_WORK'))
async def command_yes_work(callback: CallbackQuery, state: FSMContext):
    pass


@router.callback_query(StateFilter(FSMfillform.want_work_mode), Text(text='NO_WORK'))
async def command_no_work(callback: CallbackQuery, state: FSMContext):
    await