import logging
import sys

import telegram.ext as tg_ext
from telegram.ext import CommandHandler, InlineQueryHandler, CallbackQueryHandler

from bot.api_tokens import TokenNotFoundError
from bot.dialogs.popularity_dialog import start_popularity_dialog
from bot.inline import inline


def start():
    # configure logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("logger initialized. starting bot..")

    # get bot token
    try:
        from bot.api_tokens import get_bot_token
        bot_token = get_bot_token()
    except TokenNotFoundError:
        sys.exit()

    tg_updater = tg_ext.Updater(token=bot_token, use_context=True)
    dispatcher = tg_updater.dispatcher

    # inline
    inline_query_handler = InlineQueryHandler(inline.handle_inline_query)
    dispatcher.add_handler(inline_query_handler)

    callback_handler = CallbackQueryHandler(inline.handle_inline_callback)
    dispatcher.add_handler(callback_handler)
    tg_updater.start_polling()


