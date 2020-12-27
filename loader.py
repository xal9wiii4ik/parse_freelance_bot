import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from data.config import PARSER_DB
from utils.db_api.categories_command import CategoriesCommands
from utils.db_api.costs_commands import CostsCommands
from utils.db_api.payments_commands import PaymentsCommands

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage, loop=asyncio.get_event_loop())

PAYMENTS_TABLE = PaymentsCommands(PARSER_DB)
CATEGORY_TABLE = CategoriesCommands(PARSER_DB)
COSTS_TABLE = CostsCommands(PARSER_DB)
