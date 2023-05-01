import asyncio

from aiogram import Bot, Dispatcher
from handlers.user_handlers import router as user_router
from config import BOT_TOKEN

async def main() -> None:

    bot: Bot = Bot(token=BOT_TOKEN)
    dp: Dispatcher = Dispatcher()

    dp.include_router(user_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())