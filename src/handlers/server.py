from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from src.api.cpanel import CPANELClient
from src.middleware.auth import get_user_from_ctx

router = Router()

@router.message(Command("servers"))
async def cmd_servers(message: Message):
    user = await get_user_from_ctx(message)
    if not user:
        return await message.answer("❌ Not authenticated")
    
    servers = [
        "🌐 Server1: server1.example.com (Online)",
        "🌐 Server2: server2.example.com (High Load)"
    ]
    
    await message.answer("\n".join(servers))

@router.message(Command("status"))
async def cmd_status(message: Message):
    # Real API call
    client = CPANELClient(host="server1.example.com")
    status = await client.get_status()
    
    await message.answer(f"💻 *Server Status*\nCPU: {status['cpu']}%\nRAM: {status['ram']}%\nUptime: {status['uptime']}", 
                        parse_mode="Markdown")
