from chatterbot.ext.telegram_chatterbot.telegrambot import TelegramBot

def run():
    telegrambot = TelegramBot()
    telegrambot.start()