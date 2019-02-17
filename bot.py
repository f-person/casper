from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import keys, apiai, json

updater = Updater(token=keys.telegramToken)
dispatcher = updater.dispatcher

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="hi, i'm casper, let's talk")

def textMessage(bot, update):
    request = apiai.ApiAI(keys.apiaiToken).text_request()
    request.lang = 'en'
    request.session_id = 'casper'
    request.query= update.message.text
    response_json =json.loads(request.getresponse().read().decode('utf-8'))
    response = response_json['result']['fulfillment']['speech']
    if response:
        bot.send_message(chat_id = update.message.chat_id, text =response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text = "sorry, i didn't understand you correctly :(")

start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)
updater.idle()