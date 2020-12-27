from datetime import datetime

from aiogram import types
from aiogram.types import ContentType

from data.config import PAYMENTS_PROVIDER_TOKEN
from loader import dp, PAYMENTS_TABLE


PRICES_FOR_NEW_USER = [
    types.LabeledPrice(label='Подписка на месяц, как новому пользователю', amount=9900)
]

PRICES = [
    types.LabeledPrice(label='Подписка на месяц', amount=19700)
]


@dp.message_handler(commands=['buy'])
async def payment_process(message: types.Message):
    """Процесс оплаты при помощи команды buy, отправка соотвествующего invoice"""

    if not PAYMENTS_TABLE.exist_user(chat_id=message.from_user.id):
        await dp.bot.send_invoice(message.from_user.id,
                                  title='Новому пользователю',
                                  description='Для новых пользователей первый месяц скидка',
                                  provider_token=PAYMENTS_PROVIDER_TOKEN,
                                  currency='rub',
                                  need_email=True,
                                  need_phone_number=True,
                                  is_flexible=False,
                                  prices=PRICES_FOR_NEW_USER,
                                  start_parameter='time-machine-example',
                                  payload='some-invoice-payload-for-our-internal-use')
    else:
        await dp.bot.send_invoice(message.from_user.id,
                                  title='Рад что вы остаетесь с нами',
                                  description='197 рублей, как обычно)',
                                  provider_token=PAYMENTS_PROVIDER_TOKEN,
                                  currency='rub',
                                  need_email=True,
                                  need_phone_number=True,
                                  is_flexible=False,
                                  prices=PRICES,
                                  start_parameter='time-machine-example',
                                  payload='some-invoice-payload-for-our-internal-use')


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    """В случае успешной оплаты добавляем пользователя в базу таблицу payment"""

    if PAYMENTS_TABLE.exist_user(chat_id=message.from_user.id):
        PAYMENTS_TABLE.add_new_subscriber(chat_id=message.from_user.id,
                                          payment_date=datetime.now().strftime('%m.%d'))
        await dp.bot.send_message(chat_id=message.from_user.id,
                                  text='Я рад что вы воспользовались моими услугами')
    else:
        await dp.bot.send_message(chat_id=message.from_user.id,
                                  text='Я очень рад что ты остаешься)')
