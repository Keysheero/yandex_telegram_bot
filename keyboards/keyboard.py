from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import  ReplyKeyboardBuilder


def get_phone_kb() -> ReplyKeyboardMarkup:
    kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    kb_builder.row(KeyboardButton(text='📞Отправить номер телефона📞', request_contact=True), width=1)
    return kb_builder.as_markup()


