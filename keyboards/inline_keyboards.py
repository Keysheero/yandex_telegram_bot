from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def inline_access_keyboard() -> InlineKeyboardMarkup:
    ikb: InlineKeyboardBuilder = InlineKeyboardBuilder()
    ikb.row(InlineKeyboardButton(text='ДА', callback_data='YES_WORK'), width=1)
    ikb.row(InlineKeyboardButton(text='НЕТ', callback_data='NO_WORK'), width=1)
    return ikb.as_markup()