from loader import PAYMENTS_TABLE, CATEGORY_TABLE, COSTS_TABLE
from utils.mailing.kwork import KWorkParser


async def send_result_of_parse(result_of_parse: list, chat_id: int, dp):
    """Отправка резулатата парсинга пользователю"""

    if result_of_parse != 'error':
        for data in result_of_parse:
            await dp.bot.send_message(
                chat_id=chat_id,
                text=f'{data["title"]}\n'
                     f'Описание: {data["description"]}\n'
                     f'Бюджет: {data["price"]}\n'
                     f'Ссылка: {data["link"]}'
            )


async def mailing_manager(dp):
    """Мэнеджер по рассылкам"""

    paying_users = PAYMENTS_TABLE.get_payment_users()
    for paying_user in paying_users:
        categories = CATEGORY_TABLE.get_category(chat_id=paying_user[1])
        costs_categories = COSTS_TABLE.get_costs(chat_id=paying_user[1])
        for category in categories:
            for cost in costs_categories:
                await send_result_of_parse(
                    result_of_parse=KWorkParser(category=category[-1], cost=cost[-1]).parse(),
                    chat_id=category[0],
                    dp=dp
                )
