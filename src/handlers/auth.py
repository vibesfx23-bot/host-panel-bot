from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from src.middleware.auth import get_user_from_ctx

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "🔐 *Host Panel Bot*\n\n"
        "Use `/login <api_key>` to authenticate\n"
        "Available commands: `/servers`, `/status`, `/restart`",
        parse_mode="Markdown"
    )

@router.message(Command("login"))
async def cmd_login(message: Message):
    api_key = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else None
    if not api_key:
        return await message.answer("❌ Please provide API key: `/login YOUR_KEY`")
    
    # TODO: Validate API key against DB/WHMCS
    user_id = message.from_user.id
    # Store session...
    
    await message.answer("✅ Logged in successfully!")
