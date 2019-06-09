from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from chatterbot.ext.telegram_chatterbot.chatterbot import ChatBot

def get_message(bot, update):
    chatbot = ChatBot()
    text = chatbot.response(update.message.text)
    update.message.reply_text(text)

def help_command(bot, update) :
    update.message.reply_text("May I help you?")

class BotHandler:
    def __init__(self, handlers=None):
        self.handler_list = self.default_handler() \
                            if handlers is None else \
                            handlers

    def get_lists(self):
        return self.handler_list

    def default_handler(self):
        return [
            MessageHandler(Filters.text, get_message),
            CommandHandler('help', help_command)
        ]