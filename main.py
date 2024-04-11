""" Module to write telegram bot logic """

import os
from dotenv import load_dotenv

import telebot

from gpt import db_agent_toolkit

load_dotenv()

bot = telebot.TeleBot(os.getenv("BOT_API_KEY"))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """ Send welcome message """

    reply_msg = "Im a financial bot, send me expenses and I will save them in the database."
    bot.reply_to(message, reply_msg)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """ Save transaction in database """

    instructions = """
    You are a financial bot and have access to a database.
    Schemas and database structure you can query by yourself.
    
    Cases:
    1) Client sends you expenses, you should save them in the database.
    2) Client asks you to show all transactions, you should show them.
    """

    msg = db_agent_toolkit.invoke({"input": instructions + "\n" + message.text})
    bot.send_message(message.chat.id, str(msg['output']))

def main() -> None:
    """ Main function """
    bot.infinity_polling()

if __name__ == "__main__":
    main()
