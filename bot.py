from token import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater(token=token)
dispatcher = updater.dispatcher

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="hi, i'm casper, let's be friends")

def textMessage(bot, update):
    response = update.message.text
    bot.send_message(chat_id=update.message.chat_id, text="your message: "+response)

start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)