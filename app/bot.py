from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import json
import asyncio

with open('/config/config_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

TOKEN = data['token']

async def main() -> None:
    pass


if __name__ == '__main__':
    asyncio.run(main())
