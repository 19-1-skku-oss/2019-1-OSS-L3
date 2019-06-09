from chatterbot import ChatBot as ChatterBot
from chatterbot.conversation import Statement


class ChatBot:
    def __init__(self, name='', chatbot=None):
        self.name = name
        self.chatbot = self.default_bot(name) if chatbot is None else chatbot

    def get_name(self):
        return self.name

    def learn(self, ask_text, response_text):
        input_statement = Statement(ask_text)
        correct_response = Statement(response_text)
        bot.learn_response(correct_response, input_statement)

    def response(self, input_text):
        return self.chatbot.get_response(input_text).text

    def default_bot(self, name):
        bot = ChatterBot(
            name,
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch'
                },
                {
                    'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                },
                {
                    'import_path': 'chatterbot.logic.MathematicalEvaluation',
                },
                {
                    'import_path': 'chatterbot.logic.TimeLogicAdapter',
                },
                {
                    'import_path': 'chatterbot.logic.UnitConversion',
                }
            ]
        )

        return bot