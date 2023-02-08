from telebot import types
from Bd.libraries.lib import create_button


# keyboards
help_keyboard = types.ReplyKeyboardMarkup(row_width=1).add(*[
    create_button('Бакалавриат/Специалитет', 'basic-bach'),
    create_button('Магистратура', 'basic-magi'),
    create_button('Аспирантура', 'basic-inter'),
])

bach_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('   Какие документы необходимы для подачи?', 'bach-ask_1'),
    create_button('   На сколько направлений Я могу подать документы?', 'bach-ask_2'),
    create_button('   Что такое очна-заочная форма обучения?', 'bach-ask_3'),
    create_button('   Перевод из другого ВУЗа', 'bach-ask_4'),
    create_button('   Кто может сдавать внутренние вступительные испытания?', 'bach-ask_5'),
    create_button('   Особая квота', 'bach-ask_6'),
    create_button('   Справка 086-У', 'bach-ask_7'),
    create_button('   Если не нашли искомую информацию', 'bach-ask_8'),
])

magi_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('   Какие документы необходимы для подачи?', 'magi-ask_1'),
    create_button('   На сколько направлений Я могу подать документы?', 'magi-ask_2'),
    create_button('   Перевод из другого ВУЗа', 'magi-ask_3'),
    create_button('   Справка 086-У', 'magi-ask_4'),
    create_button('   Внутренние вступительные испытания', 'magi-ask_5'),
    create_button('   Если не нашли искомую информацию', 'magi-ask_6'),
])

inter_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('   Подробнее об уровне образования', 'inter-ask_1'),
])