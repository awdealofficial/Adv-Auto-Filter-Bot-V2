#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("11729920"))

API_HASH = os.environ.get("03432a86848f16962c2f12e01e32de0c")

BOT_TOKEN = os.environ.get("5619245951:AAE0TGD1oLD2fTYtPKVca3ghN84WsAXgAXc")

DB_URI = os.environ.get("mongodb+srv://tiher75183:amanmongodb@1@cluster0.vgtqk3b.mongodb.net/?retryWrites=true&w=majority")

USER_SESSION = os.environ.get("BQC8mix125qduN3BVp6PZ7uRQNTB9Kc0KD7Be8wiX-R5p4qqxt5-qqM2JGF9xuQgmiL0um79vXWssQtJR2o_T9BSbF_cbLFsBrG_o1BBKxJBm5EVQOH3hccTFE8qQzWAU2Po-UAATJ_sgD0ZK-xGn_Qcgsb8TPIpC-3EdRRdoWn5jUoAUePuJKnbRw-IGQQrKs6yDSdyhfbqWqEQmxMtHSRsqiOu44ThXGQoxTVLSETaGOI3tm5kG6Jp0B1h-p48Q3IgSTKfiFrYU9t6g8h_BKBqmMiNYD2UUcBF11TB-dFICPhtlXZnjt3cHhFw4uLsAk2qbP1plTc_4zaRLTxdUK0OAAAAAUcWu58A")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
