import logging
import uuid
import random

import telegram as tg
import telegram.ext as tg_ext

logger = logging.getLogger(__name__)


def handle_inline_spoiler(update: tg.Update, context: tg_ext.CallbackContext):
    query = update.inline_query.query

    if(len(query) < 1):
        return

    quotes = [
        "That's not a prediction. That's a Spoiler...",
        "Spoiler, we die in the end...",
        "Is it a Spoiler? I don't know... Im not a car guy.",
        "How do I Spoil?",
        "Random quote? Nope - just a Spoiler.",
        "Experience is a gread Spoiler of pleasures.",
        "You see, but you do not observe. The Spoiler is clear.",
        "Chewbacca dies, but the real Spoiler is below.",
        "Spoiler ahead, everyone aboard!",
        "Spoiler warning"
    ]

    results = [
        tg.InlineQueryResultArticle(
            id=uuid.uuid4(),
            title="Send",
            input_message_content=tg.InputTextMessageContent(message_text=random.choice(quotes)),
            reply_markup=tg.InlineKeyboardMarkup(
                inline_keyboard=[[tg.InlineKeyboardButton(
                    text='Show me',
                    callback_data=query)]])
        )
    ]
    update.inline_query.answer(results=results)
