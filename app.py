from loader import db
from aiogram import executor
from main.main import *
if __name__ == "__main__":
    executor.start_polling(db)