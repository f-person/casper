from token import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater(token=token)
dispatcher = updater.dispatcher