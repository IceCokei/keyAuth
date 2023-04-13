from multiprocessing import context
from sched import scheduler
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext import CallbackContext
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, JobQueue
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import datetime
import random
import string
import json
import os
import threading
import requests
import sys
import configparser
from key import * 

config = configparser.ConfigParser()
config.read('config.ini')

TOKEN = config.get('telegram', 'TOKEN')
GROUP_ID = config.getint('telegram', 'GROUP_ID')
ADMIN_IDS = [int(admin_id) for admin_id in config.get('telegram', 'ADMIN_IDS').split(',')]
DATA_DIR = config.get('telegram', 'data_dir')  # Make sure this line exists
TG_USER_ID = config.getint('telegram', 'TG_USER_ID')



updater = Updater(TOKEN, use_context=True)

# 授权2.0
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('key', handle_command))
updater.dispatcher.add_handler(CommandHandler('info', handle_command))
updater.dispatcher.add_handler(CommandHandler('get', handle_command))
updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_key_input))

scheduler = BackgroundScheduler()
scheduler.start()

scheduler.add_job(
    check_users_and_kick,
    "interval",
    hours=24,
    start_date=datetime.datetime.now() + datetime.timedelta(hours=1),  # 第一次运行在1小时后
)

updater.start_polling()
updater.idle()
