from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# inline конпки для категорий
categories_murk_up = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Создание сайтов', callback_data="website_development"),
        InlineKeyboardButton(text='Контекстная реклама', callback_data="contextual_advertising")
    ],
    [
        InlineKeyboardButton(text='Таргетированная реклама', callback_data="targeted_advertising"),
        InlineKeyboardButton(text='Ведение сообществ в социальных сетях', callback_data="maintaining_communities")
    ],
    [
        InlineKeyboardButton(text='SEO продвижение сайтов', callback_data="website_promotion"),
        InlineKeyboardButton(text='Копирайтинг и контент-менеджмент', callback_data="content_management")
    ],
    [
        InlineKeyboardButton(text='Графический дизайн', callback_data="graphic_design"),
        InlineKeyboardButton(text='3D графика и анимация', callback_data="graphics_animation")
    ],
    [
        InlineKeyboardButton(text='Программирование front-end', callback_data="front_programming"),
        InlineKeyboardButton(text='Программирование back-end', callback_data="back_programming")
    ],
    [
        InlineKeyboardButton(text='Чат-боты', callback_data="chat_bots"),
        InlineKeyboardButton(text='Аудио / Видео', callback_data="audio_video")
    ],
    [
        InlineKeyboardButton(text='Бухгалтерия и юриспруденция', callback_data="accounting_jurisprudence"),
        InlineKeyboardButton(text='Бизнес ассистент / помощник', callback_data="business_assistant")
    ],
    [
        InlineKeyboardButton(text='Менеджер по продажам', callback_data="sales_manager"),
        InlineKeyboardButton(text='Указать ключевую фразу', callback_data="key_phrase")
    ],
    [
        InlineKeyboardButton(text='Мобильные приложения и игры', callback_data="mobile_apps")
    ],
])

costs_murk_up = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Показывать объявления без цены', callback_data='no_price'),
        InlineKeyboardButton(text='До 10 000р', callback_data='up_to_10000')
    ],
    [
        InlineKeyboardButton(text='От 10 000р до 50 000р', callback_data='up_to_50000'),
        InlineKeyboardButton(text='От 100 000р и больше', callback_data='up_to_100000')
    ],
])

next_murk_up = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Далее', callback_data='next')
    ]
])
