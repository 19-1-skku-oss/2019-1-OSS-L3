from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from chatterbot.ext.telegram_chatterbot import conf
from chatterbot.ext.telegram_chatterbot.bothandler import BotHandler


class TelegramBot:
    def __init__(self, token=conf.TOKEN, name=conf.NAME, handlers=None):
        self.bot_token = token
        self.bot_name = name
        self.updater = Updater(token)
        self.add_handler(handlers)

    def add_handler(self, handlers=None):
        if handlers is None:
            bot_handler = BotHandler()
            handlers = bot_handler.get_lists()

        for handler in handlers:
            self.updater.dispatcher.add_handler(handler)

    def start(self):
        self.updater.start_polling(timeout=3, clean=True)
        self.updater.idle()
