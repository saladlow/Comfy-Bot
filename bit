import telegram
import random
import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Beep boop, soy un robot.")

def yesno(bot, update):
    answer = ""
    op = random.randint(1,3)
    if(op == 1):
        answer = "Sí"
    if(op == 2):
        answer = "No"
    if(op == 3):
        answer = "Mámame el güevo"
    bot.send_message(chat_id=update.message.chat_id, text=answer)

def dice6(bot, update):
    answer = ""
    op = random.randint(1,6)
    answer = str(op)
    bot.send_message(chat_id=update.message.chat_id, text=answer)

def dice64(bot, update):
    answer = ""
    results = []
    results.append(random.randint(1,6))
    results.append(random.randint(1,6))
    results.append(random.randint(1,6))
    results.append(random.randint(1,6))
    answer = str(results[0]) + " - " + str(results[1])+ " - " + str(results[2]) + " - " + str(results[3])
    bot.send_message(chat_id=update.message.chat_id, text=answer)

def dice20(bot, update):
    answer = ""
    op = random.randint(1,20)
    answer = str(op)
    bot.send_message(chat_id=update.message.chat_id, text=answer)

def thanks(bot, update):
    answer = ""
    op = random.randint(1,3)
    if(op == 1):
        answer = "De nada, pendeja"
    if(op == 2):
        answer = "De nada, puto"
    if(op == 3):
        answer = "Chí <3"
    bot.send_message(chat_id=update.message.chat_id, text=answer)

def sticker(bot, update):
    if update.message.from_user.id == 242873312:
        bot.send_sticker(update.message.chat_id, sticker="CAADAgADYAEAAuE14wgMEbPhxlsTlgI", timeout=50)
        bot.send_sticker(update.message.chat_id, sticker="CAADAgADWQEAAuE14whTTraKPKbqkQI", timeout=50)
        bot.send_sticker(update.message.chat_id, sticker="CAADAgADiAEAAuE14wj5CO0XsEg-jQI", timeout=50)
        bot.send_sticker(update.message.chat_id, sticker="CAADAgADXwEAAuE14wjDFNIiJclsTwI", timeout=50)
        bot.send_sticker(update.message.chat_id, sticker="CAADAgADVwEAAuE14wjWPdJLvlX1EwI", timeout=50)
        bot.send_sticker(update.message.chat_id, sticker="CAADAgADWAEAAuE14wi75Br2a7gqLgI", timeout=50)
        bot.send_sticker(update.message.chat_id, sticker="CAADAgADbgEAAuE14wjiC6Ue5K706QI", timeout=50)
        bot.send_sticker(update.message.chat_id, sticker="CAADAgADxwEAAuE14wg9QEPLqmUv1wI", timeout=50)
        bot.send_sticker(update.message.chat_id, sticker="CAADAgADeAEAAuE14whNiA-ELg9zTwI", timeout=50)
        bot.send_sticker(update.message.chat_id, sticker="CAADAgADXQEAAuE14wimPBqGcpeu4gI", timeout=50)
        bot.send_sticker(update.message.chat_id, sticker="CAADAgADWwEAAuE14wjU1o-VM3YkXwI", timeout=50)
        bot.send_sticker(update.message.chat_id, sticker="CAADAgADVgEAAuE14wgGIHzTr-YddQI", timeout=50)

    else:
        bot.send_message(chat_id=update.message.chat_id, text="Tú no me mandas")


def pick(bot, update, args):
    options = args
    if(len(options) < 2):
        answer = "Dame por lo menos dos opciones, subnormal"
    else:
        options.append("Mámame el güevo")
        op = random.randint(0,len(options)-1)
        answer = options[op]

    bot.send_message(chat_id=update.message.chat_id, text=answer)

def halim(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="ese no es peo tuyo")

def ephi(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Disculpa es que me dió un AC🅱️")

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Eso está fuera de mis capacidades (en realidad ni si quiera entendí lo que dijiste).")

def main():

    updater = Updater(token='469191961:AAErQ0JCehPomyQW2LFdjvs5b3SB6EzBm0c')
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    caps_handler = CommandHandler('sn', yesno)
    dispatcher.add_handler(caps_handler)

    dice6_handler = CommandHandler('dado6', dice6)
    dispatcher.add_handler(dice6_handler)

    dice64_handler = CommandHandler('4dado6', dice64)
    dispatcher.add_handler(dice64_handler)

    dice20_handler = CommandHandler('dado20', dice20)
    dispatcher.add_handler(dice20_handler)

    thanks_handler = CommandHandler('gracias', thanks)
    dispatcher.add_handler(thanks_handler)

    sticker_handler = CommandHandler('sticker', sticker)
    dispatcher.add_handler(sticker_handler)

    halim_handler = CommandHandler('halim', halim)
    dispatcher.add_handler(halim_handler)

    ephi_handler = CommandHandler('ephi', ephi)
    dispatcher.add_handler(ephi_handler)

    pick_handler = CommandHandler('elige', pick, pass_args=True)
    dispatcher.add_handler(pick_handler)

    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
