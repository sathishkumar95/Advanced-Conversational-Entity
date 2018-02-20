from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


bot = ChatBot(
    "Jarvis"

    )


bot.set_trainer(ChatterBotCorpusTrainer)

bot.train(
    "chatterbot.corpus.english.greetings"
)

print("\nGreetings Human..... \nType In your query \n:")

while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(input())
        print(bot_input)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break