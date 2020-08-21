import logging
import re

import telegram as tg
import telegram.ext as tg_ext
from telegram import CallbackQuery

import spoiler.spoiler as spoiler

logger = logging.getLogger(__name__)


def handle_inline_query(update: tg.Update, context: tg_ext.CallbackContext):
    logger.info('handling inline spoiler..')
    spoiler.handle_inline_spoiler(update, context)

def handle_inline_callback(update: tg.Update, context: tg_ext.CallbackContext):
    query: CallbackQuery = update.callback_query
    callback_data = query.data

    logger.info('Handling spoiler callback')
    spoiler_text = callback_data
    update.callback_query.answer(spoiler_text, show_alert=True)
