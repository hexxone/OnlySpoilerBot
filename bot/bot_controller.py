import logging
from telegram.ext import MessageHandler, Filters, Updater, CommandHandler
from bot.token_provider import get_token
from bot.attendance_information import CrowdedInfo

# Boilerplate

updater = Updater(token=get_token(), use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def caps(update, context):
    print(update)
    print(context)
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


def workout_state(update, context):
    try:
        param1: str = context.args[0]
        information = CrowdedInfo()
        if param1 == "jetzt":
            response = information.get_current_attendence()
        else:
            day = param1
            hour: int = int(context.args[1])
            response = information.get_attendence(day, hour)
    except:
        response = "Versteh ich nicht"

    context.bot.send_message(chat_id=update.effective_chat.id, text=response)


echo_handler = MessageHandler(Filters.text, echo)
start_handler = CommandHandler('start', start)
caps_handler = CommandHandler('caps', caps)
workout_state_handler = CommandHandler('wievoll', workout_state)
# dispatcher.add_handler(caps_handler)
# dispatcher.add_handler(start_handler)
# dispatcher.add_handler(echo_handler)
dispatcher.add_handler(workout_state_handler)
updater.start_polling()
