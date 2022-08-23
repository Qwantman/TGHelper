import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import chat

bot = Bot(token=f"{open('token', 'r').read()}")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands='ping')
async def ping(message: types.Message):
    msg = await message.reply('Pong!')
    await asyncio.sleep(3)
    await msg.delete()
    await message.delete()

@dp.message_handler()
async def reply(message: types.Message):
    if(message.chat.id == -1001525927634):
        await bot.send_message(-1001687186942, f'@{message.from_user.username}:')
        await message.send_copy(-1001687186942, disable_notification=True)
    else:
        print(message)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)