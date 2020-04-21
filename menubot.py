from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token='1090905300:AAF0VNYborDgw0xNzP9jxUtq2309QKNORk0', use_context=True)
dispatcher = updater.dispatcher

menu = [['ℹBiz kimmiz?', '✅Nima uchun biz?'],
        ['🎓Kurslarimiz', '👨🏻‍💻Kursga yozilish'],
        ['📍Manzilimiz', '📞Biz bilan bog\'lanish'],
        ['🔗Ijtimoiy tarmoqlardagi sahifalarimiz']]
markup = ReplyKeyboardMarkup(menu, resize_keyboard=True)

ortga = [['Ortga']]
markap = ReplyKeyboardMarkup(ortga, resize_keyboard=True)

BUTTON1_BIZ = 'ℹBiz kimmiz?'
BUTTON2_WHY = '✅Nima uchun biz?'
BUTTON3_KURS = '🎓Kurslarimiz'
BUTTON4_YOZILISH = '👨🏻‍💻Kursga yozilish'
BUTTON5_MANZIL = '📍Manzilimiz'
BUTTON6_ALOQA = '📞Biz bilan bog\'lanish'
BUTTON7_IJTIMOIY = '🔗Ijtimoiy tarmoqlardagi sahifalarimiz'
BUTTON8_ORTGA = 'Ortga'


def do_echo(update, context):
    text = update.message.text
    if text == BUTTON1_BIZ:
        return biz(update, context)
    elif text == BUTTON2_WHY:
        return why(update, context)
    elif text == BUTTON3_KURS:
        return kurslar(update, context)
    elif text == BUTTON5_MANZIL:
        return manzil(update, context)
    elif text == BUTTON6_ALOQA:
        return aloqa(update, context)
    elif text == BUTTON7_IJTIMOIY:
        return ijtmoiy(update, context)
    elif text == BUTTON8_ORTGA:
        return ortga(update, context)


def biz(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Bu yerda kompaniya haqida ma'lumot bo'ladi.",
                             reply_markup=markap
                             )


def why(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Bu yerda nima uchun biz degan savolga javob beriladi.",
                             reply_markup=markap
                             )


def kurslar(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Quyidagi knopkalrdan kurslarimiz haqida ma'lumot olishingiz mumkin.",
                             reply_markup=markap
                             )


def manzil(update, context):
    context.bot.send_location(chat_id=update.effective_chat.id,
                              longitude=40.4673788, latitude=70.213328,
                              reply_markup=markup
                              )
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="",
                             reply_markup=markup
                             )


def aloqa(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Biz bilan bog'lanish uchun +998977342299 raqamiga qo'ng'iroq qiling!",
                             reply_markup=markup
                             )


def ijtmoiy(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Quyidagi linklar orqali ijtimoiy tarmoqlardagi sahifalarimizga kirishingiz mumkin",
        reply_markup=get_base_inline_keyboard()
    )


def ortga(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Siz asosiy sahifaga qaytingiz!",
                             reply_markup=markup
                             )


CALLBACK_BUTTON1_LEFT = "callback_button1_left"
CALLBACK_BUTTON2_RIGHT = "callback_button2_right"
CALLBACK_BUTTON3 = "callback_button3"
CALLBACK_BUTTON4 = "callback_button4"
CALLBACK_BUTTON5_ORTGA = "callback_button5_ortga"

TITLES = {
    CALLBACK_BUTTON1_LEFT: "Facebook",
    CALLBACK_BUTTON2_RIGHT: "Instagram",
    CALLBACK_BUTTON3: "Youtube",
    CALLBACK_BUTTON4: "Telegram",
    CALLBACK_BUTTON5_ORTGA: "Ortga"
}


def get_base_inline_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_LEFT], callback_data=CALLBACK_BUTTON1_LEFT),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON2_RIGHT], callback_data=CALLBACK_BUTTON2_RIGHT),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON3], callback_data=CALLBACK_BUTTON3),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON4], callback_data=CALLBACK_BUTTON4),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON5_ORTGA], callback_data=CALLBACK_BUTTON5_ORTGA)
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def keyboard_callback_handler(update, context):
    query = update.callback_query
    data = query.data
    if data == CALLBACK_BUTTON1_LEFT:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="[Facebook sahifamizga kirish](https://www.facebook.com/elyorjon08)",
            reply_markup=ReplyKeyboardRemove(get_base_inline_keyboard),
            parse_mode='Markdown'
        )
        return CALLBACK_BUTTON5_ORTGA
    elif data == CALLBACK_BUTTON2_RIGHT:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="[Instagram](https://www.instagram.com/oqjariy)",
            reply_markup=ReplyKeyboardRemove(get_base_inline_keyboard),
            parse_mode='Markdown'
        )
        return CALLBACK_BUTTON5_ORTGA
    elif data == CALLBACK_BUTTON3:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="[Youtube sahifamiz](https://www.youtube.com/elyorjon08)",
            reply_markup=ReplyKeyboardRemove(get_base_inline_keyboard),
            parse_mode='Markdown'
        )
    elif data == CALLBACK_BUTTON4:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            url='t.me/oqjariy',
            reply_markup=get_base_inline_keyboard(),
        )

    elif data == CALLBACK_BUTTON5_ORTGA:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Bosh sahifamizga qaytingiz!",
            reply_markup=markup,
        )


def start(update, context):
    update.message.reply_text(
        'Assalomu alaykum, {}'.format(update.message.from_user.first_name))

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Qolam ta'lim markazining rasmiy botiga xush kelibsiz!"
                                  "Bizning xizmatimizdan foydalanayotganinggizdan xursandmiz."
                                  "Umid qilamizki,siz izlagan ma\'lumotingizni,albatta, topasiz.",
                             reply_markup=markup
                             )


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
buttons_handler = CallbackQueryHandler(callback=keyboard_callback_handler, pass_chat_data=True)
dispatcher.add_handler(buttons_handler)

message_handler = MessageHandler(Filters.text, do_echo)
dispatcher.add_handler(message_handler)
updater.start_polling()
updater.idle()
