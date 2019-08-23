import random
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename='comy-bot.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    context.bot.send_message("Beep boop, soy un robot.")

def yesno(update, context):
    answer = ""
    op = random.randint(1,3)
    if(op == 1):
        answer = "Sí"
    if(op == 2):
        answer = "No"
    if(op == 3):
        answer = "Mámame el güevo"
    update.message.reply_text(answer)

def dice6(update, context):
    answer = ""
    op = random.randint(1,6)
    answer = str(op)
    update.message.reply_text(answer)

def dice64(update, context):
    answer = ""
    results = []
    results.append(random.randint(1,6))
    results.append(random.randint(1,6))
    results.append(random.randint(1,6))
    results.append(random.randint(1,6))
    answer = str(results[0]) + " - " + str(results[1])+ " - " + str(results[2]) + " - " + str(results[3])
    update.message.reply_text(answer)

def dice20(update, context):
    answer = ""
    op = random.randint(1,20)
    answer = str(op)
    update.message.reply_text(answer)

def thanks(update, context):
    answer = ""
    op = random.randint(1,3)
    if(op == 1):
        answer = "De nada, pendeja"
    if(op == 2):
        answer = "De nada, puto"
    if(op == 3):
        answer = "Chí <3"
    update.message.reply_text(answer)

def pick(update, context):
    options = context.pass_args
    if(len(options) < 2):
        answer = "Dame por lo menos dos opciones, subnormal"
    else:
        options.append("Mámame el güevo")
        op = random.randint(0,len(options)-1)
        answer = options[op]

    context.bot.send_message(chat_id=update.message.chat_id, text=answer)

def halim(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="ese no es peo tuyo")

def ephi(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Disculpa es que me dió un AC🅱️")

def jex(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Mardito país")

def unknown(update, context):
    update.message.reply_text("Eso está fuera de mis capacidades (en realidad ni si quiera entendí lo que dijiste).")

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():

    updater = Updater("469191961:AAErQ0JCehPomyQW2LFdjvs5b3SB6EzBm0c", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('sn', yesno))
    dp.add_handler(CommandHandler('dado6', dice6))
    dp.add_handler(CommandHandler('4dado6', dice64))
    dp.add_handler(CommandHandler('dado20', dice20))
    dp.add_handler(CommandHandler('gracias', thanks))
    dp.add_handler(CommandHandler('halim', halim))
    dp.add_handler(CommandHandler('ephi', ephi))
    dp.add_handler(CommandHandler('jex', jex))
    dp.add_handler(CommandHandler('elige', pick, pass_args=True))
    dp.add_handler(MessageHandler(Filters.command, unknown))

    dp.add_error_handler(error)
    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
