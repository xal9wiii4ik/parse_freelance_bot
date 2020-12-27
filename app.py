import asyncio

from utils.mailing.mailing_manager import mailing_manager
from utils.payment.payment_manager import payment_manager


async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)


async def on_shutdown(dp):
    from utils.notify_admins import on_shutdown_notify
    await on_shutdown_notify(dp)


async def mailing(dp, wait_for):
    """Рассылка сообщений"""

    while True:
        await mailing_manager(dp=dp)
        await asyncio.sleep(wait_for)


async def update_and_mailing_unpaid_status(wait_for) -> None:
    """Обновление и рассылка не оплаченного статуса"""

    while True:
        await payment_manager(dp=dp)
        await asyncio.sleep(delay=wait_for)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    from loader import PAYMENTS_TABLE, COSTS_TABLE, CATEGORY_TABLE

    dp.loop.create_task(update_and_mailing_unpaid_status(wait_for=5))
    dp.loop.create_task(mailing(dp=dp, wait_for=10))
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
    PAYMENTS_TABLE.close()
    COSTS_TABLE.close()
    CATEGORY_TABLE.close()
