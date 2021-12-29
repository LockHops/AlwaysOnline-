# -*- coding: utf-8 -*-

import logging
from login import *
from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateStatusRequest
import time
from data import delay

if client.is_user_authorized():
    logging.info("You are now AlwaysOffline™, Yah!")
    while True:
        client(UpdateStatusRequest(offline = True))
        time.sleep(delay)
        logging.debug("Sleep for 1 min")
else:
    logging.fatal("Login Fails, please retry...")
