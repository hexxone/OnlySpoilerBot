import logging
import sys

from telegram.ext import Updater, CommandHandler

from bot.bot_token_provider import get_token
from bot.workout_state_dialog import handle_user_input

print("starting bot!")
updater = Updater(token=get_token(), use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def location(update, context):
    from bot.gmaps_api import locations
    all_locations = str(list(locations.keys()))
    context.bot.send_message(chat_id=update.effective_chat.id, text=all_locations)


def workout_state(update, context):
    # command template: wievoll [jetzt/Wochentag Uhrzeit] [Standort]
    try:
        response = handle_user_input(context.args)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        response = "Versteh ich nicht"

    context.bot.send_message(chat_id=update.effective_chat.id, text=response)


workout_state_handler = CommandHandler('wievoll', workout_state)
location_handler = CommandHandler('locations', location)
dispatcher.add_handler(workout_state_handler)
dispatcher.add_handler(location_handler)
updater.start_polling()
