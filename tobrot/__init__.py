#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | gautamajay52 | MaxxRider

import logging
import os
import time
from logging.handlers import RotatingFileHandler
from collections import defaultdict
from sys import exit

import dotenv

if os.path.exists("TorrentLeech-Gdrive.txt"):
    with open("Torrentleech-Gdrive.txt", "r+") as f_d:
        f_d.truncate(0)

# the logging things
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "Torrentleech-Gdrive.txt", maxBytes=50000000, backupCount=10
        ),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("PIL").setLevel(logging.WARNING)

LOGGER = logging.getLogger(__name__)

user_specific_config=dict()

dotenv.load_dotenv("config.env")

# checking compulsory variable
for imp in ["TG_BOT_TOKEN", "APP_ID", "API_HASH", "OWNER_ID", "AUTH_CHANNEL"]:
    try:
        value = os.environ[imp]
        if not value:
            raise KeyError
    except KeyError:
        LOGGER.critical(f"Oh...{imp} is missing from config.env ... fill that")
        exit()

# The Telegram API things
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1855947262:AAEnLpZIwkexN51ACZcHGEP5h_p2bF-z26g")
APP_ID = int(os.environ.get("APP_ID", "5999444"))
API_HASH = os.environ.get("API_HASH", "51b58a93d88a55565ff048c7a143eb4e")
OWNER_ID = int(os.environ.get("OWNER_ID", "821190684"))

# Get these values from my.telegram.org
# to store the channel ID who are authorized to use the bot
AUTH_CHANNEL = [int(x) for x in os.environ.get("AUTH_CHANNEL", "-1001374445001 -1001554287360").split()]

# the download location, where the HTTP Server runs
DOWNLOAD_LOCATION = "./DOWNLOADS"
# Telegram maximum file upload size
MAX_FILE_SIZE = 50000000
TG_MAX_FILE_SIZE = 2097152000
FREE_USER_MAX_FILE_SIZE = 50000000
AUTH_CHANNEL.append(539295917)
AUTH_CHANNEL.append(OWNER_ID)
# chunk size that should be used with requests
CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", "128"))
# default thumbnail to be used in the videos
DEF_THUMB_NAIL_VID_S = os.environ.get(
    "DEF_THUMB_NAIL_VID_S", "https://wallpapercave.com/wp/wp5187169.jpg"
)
# maximum message length in Telegram
MAX_MESSAGE_LENGTH = 4096
# set timeout for subprocess
PROCESS_MAX_TIMEOUT = 3600
#
SP_LIT_ALGO_RITH_M = os.environ.get("SP_LIT_ALGO_RITH_M", "hjs")
ARIA_TWO_STARTED_PORT = int(os.environ.get("ARIA_TWO_STARTED_PORT", "6800"))
EDIT_SLEEP_TIME_OUT = int(os.environ.get("EDIT_SLEEP_TIME_OUT", "15"))
MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(
    os.environ.get("MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START", 300)
)
MAX_TG_SPLIT_FILE_SIZE = int(os.environ.get("MAX_TG_SPLIT_FILE_SIZE", "2097152000"))
# add config vars for the display progress
FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "█")
UN_FINISHED_PROGRESS_STR = os.environ.get("UN_FINISHED_PROGRESS_STR", "░")
# add offensive API
TG_OFFENSIVE_API = os.environ.get("TG_OFFENSIVE_API", None)
CUSTOM_FILE_NAME = os.environ.get("CUSTOM_FILE_NAME", "")
LEECH_COMMAND = os.environ.get("LEECH_COMMAND", "leech@torrgsbot")
LEECH_UNZIP_COMMAND = os.environ.get("LEECH_UNZIP_COMMAND", "extract@torrgsbot")
LEECH_ZIP_COMMAND = os.environ.get("LEECH_ZIP_COMMAND", "archive@torrgsbot")
GLEECH_COMMAND = os.environ.get("GLEECH_COMMAND", "gleech@torrgsbot")
GLEECH_UNZIP_COMMAND = os.environ.get("GLEECH_UNZIP_COMMAND", "gleechunzip@torrgsbot")
GLEECH_ZIP_COMMAND = os.environ.get("GLEECH_ZIP_COMMAND", "gleechzip@torrgsbot")
YTDL_COMMAND = os.environ.get("YTDL_COMMAND", "ytdl@torrgsbot")
GYTDL_COMMAND = os.environ.get("GYTDL_COMMAND", "gytdl@torrgsbot")
RCLONE_CONFIG = os.environ.get("RCLONE_CONFIG", '[torrgsbot]\ntype = drive\nscope = drive\nroot_folder_id = 1FdiXKYkFKDW3yHqwdIa1MWPTycXwqYrV\ntoken = {"access_token":"ya29.a0ARrdaM9t11etcckgRlVuQlofOd_zRkcGIBkRKF4SGoVT3_hYzgPV13amRqyCCVtjLHPnFfML2fk5lCp5Og_zj4JBjRJ7yqC8Ywx3Bnork_IOSw_sbCPpro1Mc0IsKdLwLSNJvzaEO-1a7Wd4TaYFwU4REBEm","token_type":"Bearer","refresh_token":"1//0g-Ms0tWIsucdCgYIARAAGBASNwF-L9IrXnbZX1iVZUc9-B3bHx2k4QWzNmMVJ4IgCKQTDI0G-53dvCP8chJdys5XCU4kbx3XsZU","expiry":"2021-07-12T10:54:58.8451394+05:30"}')
DESTINATION_FOLDER = os.environ.get("DESTINATION_FOLDER", "torrgs")
INDEX_LINK = os.environ.get("INDEX_LINK", "https://torrgs.bmcgee.workers.dev")
TELEGRAM_LEECH_COMMAND = os.environ.get("TELEGRAM_LEECH_COMMAND", "tleech@torrgsbot")
TELEGRAM_LEECH_UNZIP_COMMAND = os.environ.get(
    "TELEGRAM_LEECH_UNZIP_COMMAND", "textract@torrgsbot"
)
CANCEL_COMMAND_G = os.environ.get("CANCEL_COMMAND_G", "cancel")
GET_SIZE_G = os.environ.get("GET_SIZE_G", "getsize")
STATUS_COMMAND = os.environ.get("STATUS_COMMAND", "status@torrgsbot")
SAVE_THUMBNAIL = os.environ.get("SAVE_THUMBNAIL", "savethumbnail@torrgsbot")
CLEAR_THUMBNAIL = os.environ.get("CLEAR_THUMBNAIL", "clearthumbnail@torrgsbot")
UPLOAD_AS_DOC = os.environ.get("UPLOAD_AS_DOC", "False")
PYTDL_COMMAND = os.environ.get("PYTDL_COMMAND", "pytdl@torrgsbot")
GPYTDL_COMMAND = os.environ.get("GPYTDL_COMMAND", "gpytdl@torrgsbot")
LOG_COMMAND = os.environ.get("LOG_COMMAND", "log")
CLONE_COMMAND_G = os.environ.get("CLONE_COMMAND_G", "gclone")
UPLOAD_COMMAND = os.environ.get("UPLOAD_COMMAND", "upload")
RENEWME_COMMAND = os.environ.get("RENEWME_COMMAND", "renewme")
RENAME_COMMAND = os.environ.get("RENAME_COMMAND", "rename")
TOGGLE_VID = os.environ.get("TOGGLE_VID", "upload_vid")
TOGGLE_DOC = os.environ.get("TOGGLE_DOC", "upload_doc")
HELP_COMMAND = os.environ.get("HELP_COMMAND", "help@torrgsbot")
BOT_START_TIME = time.time()
# dict to control uploading and downloading
gDict = defaultdict(lambda: [])
# user settings dict #ToDo
user_settings = defaultdict(lambda: {})


def multi_rclone_init():
    if RCLONE_CONFIG:
        LOGGER.warning("Don't use this var now, put your rclone.conf in root directory")
    if not os.path.exists("rclone.conf"):
        LOGGER.warning("Sed, No rclone.conf found in root directory")
        return
    if not os.path.exists("rclone_bak.conf"):  # backup rclone.conf file
        with open("rclone_bak.conf", "w+", newline="\n", encoding="utf-8") as fole:
            with open("rclone.conf", "r") as f:
                fole.write(f.read())
        LOGGER.info("rclone.conf backuped to rclone_bak.conf!")


multi_rclone_init()
