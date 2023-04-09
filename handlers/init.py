from aiogram.bot import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config

bot = Bot(token=config.API_KEY)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
