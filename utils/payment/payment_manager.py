import asyncio
from datetime import datetime

from loader import PAYMENTS_TABLE


def check_unpaid_days(unpaid_day: int) -> bool:
    """Проверка колличества не оплаченных дней для смены рассылки"""

    day = 10
    while True:
        if day == unpaid_day:
            return True
        if day > unpaid_day:
            return False
        day += 3


async def payment_manager(dp):
    """Мэнеджер по статусе оплаты"""

    # present_date_1 = datetime.now().strftime('%m.%d')
    present_date = datetime.now().strftime('%M')
    unpaid_users = PAYMENTS_TABLE.get_un_payment_users()
    if len(unpaid_users) > 0:
        while int(datetime.now().strftime('%M')) == int(present_date.split('.')[-1]):
            unpaid_users = PAYMENTS_TABLE.get_un_payment_users()
            if len(unpaid_users) == 0:
                break
            for unpaid_user in unpaid_users:
                if int(unpaid_user[3] <= 7):
                    await dp.bot.send_message(
                        chat_id=unpaid_user[1],
                        text='Вы не оплатили подписку. Пожалуйста исправьте это!)'
                    )
            await asyncio.sleep(10)
        unpaid_users = PAYMENTS_TABLE.get_un_payment_users()
        for unpaid_user in unpaid_users:
            PAYMENTS_TABLE.update_un_payment_days(chat_id=unpaid_user[1],
                                                  unpaid_days=(unpaid_user[3] + 1))
            if check_unpaid_days(unpaid_day=unpaid_user[3] + 1):
                await dp.bot.send_message(
                    chat_id=unpaid_user[1],
                    text=f'Вы не оплатили подписку.'
                         f'Количество неоплаченных дней {unpaid_user[3]} и это грустно(.'
                         f'Пожалуйста исправьте это!)'
                )
    payments_users = PAYMENTS_TABLE.get_payment_users()
    for payments_user in payments_users:
        if int(payments_user[2].split('.')[0]) == (int(present_date.split('.')[0]) - 1) and int(
                payments_user[2].split('.')[-1]) == (int(present_date.split('.')[-1])):
            PAYMENTS_TABLE.edit_payment_state_and_time(payment_state=False,
                                                       chat_id=payments_user[1])
