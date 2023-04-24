from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import common, weather, converter, animal, poll
import asyncio
import os
from dotenv import load_dotenv
from aiogram.fsm.strategy import FSMStrategy

async def main():
    dp = Dispatcher(storage=MemoryStorage())
    # fsm_strategy=FSMStrategy.CHAT)
    bot = Bot(token=os.environ.get('token_bot'), parse_mode='HTML')
    dp.include_routers(common.router, weather.router, converter.router, animal.router, poll.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    asyncio.run(main())