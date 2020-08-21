import logging
import os

logger = logging.getLogger(__name__)


class TokenNotFoundError(RuntimeError):
    def __init__(self, message):
        self.message = message

def get_bot_token():
    try:
        bot_token = os.environ['BOT_TOKEN']
        return bot_token
    except:
        msg = 'Bot token environment variable not set'
        logger.error(msg)
        raise TokenNotFoundError(msg)
