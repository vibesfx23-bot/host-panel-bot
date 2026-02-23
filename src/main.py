import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from src.config import settings
from src.handlers import auth, server, hosting
from src.middleware.auth import AuthMiddleware
from src.utils.logger import setup_logger

logger = setup_logger()

async def main():
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    
    # Middleware
    dp.message.middleware(AuthMiddleware())
    
    # Register handlers
    dp.include_router(auth.router)
    dp.include_router(server.router)
    dp.include_router(hosting.router)
    
    logger.info("🚀 Host Panel Bot starting...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
