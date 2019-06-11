from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

userinput = "hi"
while not userinput == "exit":
  print("chatterbot: ", end = "")
  print(chatbot.get_response(userinput))
  print("input (enter \"exit\" to exit): ",end = "")
  userinput = input()

