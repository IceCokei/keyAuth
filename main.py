import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import datetime

from key import *  
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
TG_USER_ID = config.get('telegram', 'TG_USER_ID')
TOKEN = config.get('telegram', 'TOKEN')
GROUP_ID = config.get('telegram', 'GROUP_ID')
ADMIN_IDS = [int(x) for x in config.get('telegram', 'ADMIN_IDS').split(',')]
data_dir = config.get('telegram', 'data_dir')

updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('key', handle_command))
updater.dispatcher.add_handler(CommandHandler('info', handle_command))
updater.dispatcher.add_handler(CommandHandler('get', handle_command))
updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_key_input))

updater.start_polling()
