from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.inline_murk_up import categories_murk_up, costs_murk_up, next_murk_up
from loader import dp, CATEGORY_TABLE, COSTS_TABLE
from utils.db_api.costs_commands import CostsCommands


def _validate_category(base_table: CATEGORY_TABLE, chat_id: int, category: str) -> None:
    """Validate category and add to database"""

    if base_table.get_count_category(chat_id=chat_id) < 3:
        if not base_table.exist_category(chat_id=chat_id, category=category):
            base_table.add_new_category_and_chat_id(chat_id=chat_id, category=category)


def _validate_cost(base_table: CostsCommands, chat_id: int, cost: int) -> None:
    """validate category of cost"""

    if base_table.get_count_cost(chat_id=chat_id) < 3:
        if not base_table.exist_cost(chat_id=chat_id, cost=cost):
            base_table.add_new_costs(chat_id=chat_id, cost=cost)


@dp.message_handler(lambda message: message.text == 'старт' or message.text == 'Старт')
async def bot_message_start(message: types.Message) -> None:
    """processing message 'start'"""

    await message.answer(text='Выберите категории услуг, на которые Вы хотите получать заявки.'
                              'Вы можете указать до 3х категорий.', reply_markup=categories_murk_up)
    await message.answer(text='Укажите ценовую категорию.'
                              'Вы можете указать до 3х ценовых категорий.', reply_markup=costs_murk_up)
    await message.answer(text='Что бы продолжить нажмите далее.', reply_markup=next_murk_up)


@dp.callback_query_handler(text="website_development")
async def call_back_website_development(call: CallbackQuery) -> None:
    """processing button website development"""

    _validate_category(CATEGORY_TABLE, call.from_user.id, 'Создание сайтов')


@dp.callback_query_handler(text="contextual_advertising")
async def call_back_contextual_advertising(call: CallbackQuery) -> None:
    """processing button contextual_advertising"""

    _validate_category(CATEGORY_TABLE, call.from_user.id, 'Контекстная реклама')


@dp.callback_query_handler(text="targeted_advertising")
async def call_back_targeted_advertising(call: CallbackQuery) -> None:
    """processing button targeted_advertising"""

    _validate_category(CATEGORY_TABLE, call.from_user.id, 'Таргетированная реклама')


@dp.callback_query_handler(text="maintaining_communities")
async def call_back_maintaining_communities(call: CallbackQuery) -> None:
    """processing button maintaining_communities"""

    _validate_category(CATEGORY_TABLE, call.from_user.id, 'Ведение сообществ в социальных сетях')


@dp.callback_query_handler(text="website_promotion")
async def call_back_website_promotion(call: CallbackQuery) -> None:
    """processing button website_promotion"""

    _validate_category(CATEGORY_TABLE, call.from_user.id, 'SEO продвижение сайтов')


@dp.callback_query_handler(text="content_management")
async def call_back_content_management(call: CallbackQuery) -> None:
    """processing button content_management"""

    _validate_category(CATEGORY_TABLE, call.from_user.id, 'Копирайтинг и контент-менеджмент')


@dp.callback_query_handler(text="graphic_design")
async def call_back_graphic_design(call: CallbackQuery) -> None:
    """processing button graphic_design"""

    _validate_category(CATEGORY_TABLE, call.from_user.id, 'Графический дизайн')


@dp.callback_query_handler(text="graphics_animation")
async def call_back_graphics_animation(call: CallbackQuery) -> None:
    """processing button graphics_animation"""

    _validate_category(CATEGORY_TABLE, call.from_user.id, '3D графика и анимация')


@dp.callback_query_handler(text="front_programming")
async def call_back_front_programming(call: CallbackQuery) -> None:
    """processing button front_programming"""

    _validate_category(CATEGORY_TABLE, call.from_user.id, 'Программирование front-end')


@dp.callback_query_handler(text="back_programming")
async def call_back_back_programming(call: CallbackQuery) -> None:
    """processing button back_programming"""

    _validate_category(CATEGORY_TABLE, call.from_user.id, 'Программирование back-end')


@dp.callback_query_handler(text="mobile_apps")
async def call_back_mobile_apps(call: CallbackQuery) -> None:
    """processing button mobile_apps"""

    _validate_category(CATEGORY_TABLE, call.from_user.id, 'Мобильные приложения и игры')


@dp.callback_query_handler(text="chat_bots")
async def call_back_chat_bots(call: CallbackQuery) -> None:
    """processing button chat_bots"""

    _validate_category(CATEGORY_TABLE, call.from_user.id, 'Чат-боты')


@dp.callback_query_handler(text="audio_video")
async def call_back_audio_video(call: CallbackQuery) -> None:
    """processing button audio_video"""

    _validate_category(CATEGORY_TABLE, call.from_user.id, 'Аудио / Видео')


@dp.callback_query_handler(text="accounting_jurisprudence")
async def call_back_accounting_jurisprudence(call: CallbackQuery) -> None:
    """processing button accounting_jurisprudence"""

    _validate_category(CATEGORY_TABLE, call.from_user.id, 'Бухгалтерия и юриспруденция')


@dp.callback_query_handler(text="business_assistant")
async def call_back_business_assistant(call: CallbackQuery) -> None:
    """processing button business_assistant"""

    _validate_category(CATEGORY_TABLE, call.from_user.id, 'Бизнес ассистент / помощник')


@dp.callback_query_handler(text="sales_manager")
async def call_back_sales_manager(call: CallbackQuery) -> None:
    """processing button sales_manage"""

    _validate_category(base_table=CATEGORY_TABLE, chat_id=call.from_user.id, category='Менеджер по продажам')


@dp.callback_query_handler(text="key_phrase")
async def call_back_key_phrase(call: CallbackQuery) -> None:
    """processing button key_phrase"""

    _validate_category(base_table=CATEGORY_TABLE, chat_id=call.from_user.id, category='Указать ключевую фразу')


@dp.callback_query_handler(text="no_price")
async def call_back_no_price(call: CallbackQuery) -> None:
    """processing button no_price"""

    _validate_cost(base_table=COSTS_TABLE, chat_id=call.from_user.id, cost=0)


@dp.callback_query_handler(text="up_to_10000")
async def call_back_up_to_10000(call: CallbackQuery) -> None:
    """processing button up_to_10000"""

    _validate_cost(base_table=COSTS_TABLE, chat_id=call.from_user.id, cost=10000)


@dp.callback_query_handler(text="up_to_50000")
async def call_back_up_to_50000(call: CallbackQuery) -> None:
    """processing button up_to_50000"""

    _validate_cost(base_table=COSTS_TABLE, chat_id=call.from_user.id, cost=50000)


@dp.callback_query_handler(text="up_to_100000")
async def call_back_up_to_100000(call: CallbackQuery) -> None:
    """processing button up_to_100000"""

    _validate_cost(base_table=COSTS_TABLE, chat_id=call.from_user.id, cost=100000)


@dp.callback_query_handler(text="next")
async def call_back_next(call: CallbackQuery) -> None:
    """processing button next"""

    await dp.bot.send_message(chat_id=call.from_user.id,
                              text='\nОтлично! Я уже начал подбирать самые подходящие заявки для Вас. '
                                   '\nОднако осталось всего лишь оформить подписку. Цена - 199р в месяц. '
                                   '\nСогласитесь врядли где-то ещё можно получать '
                                   'сотни заявок в месяц за 7 рублей в день.'
                                   '\nОднако для Вас супер предложение!Первый месяц подписки всего 99 рублей. '
                                   '\nПосле подписки Вы получите уже 30 заявок '
                                   'в течении 10 минут и десятки заявок каждый день.'
                                   '\n Для оплаты напишите команду /buy')
