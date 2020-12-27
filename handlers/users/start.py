from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    me = await bot.get_me()
    await message.answer(f'Здравствуйте, я {me["username"]}.\nКаждый час я анализирую тысячи сайтов,\n'
                         f'телеграмм каналов и подбираю для Вас самые интересные заказы на услуги фрилансеров.\n'
                         f'Работать со мной крайне просто. \nУкажите на какие виды услуг вы хотите получать заказы,\n'
                         f'поставьте фильтр по бюджету и каждый день \nВы будете получать десятки заказов по'
                         f'Вашим критериям. \nЧто бы начать напишите слово "Старт"')
