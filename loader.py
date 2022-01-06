from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import config
bot = Bot(token=config.BOT_TOKEN)
storage = MemoryStorage()
db = Dispatcher(bot, storage=storage)