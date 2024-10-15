from datetime import datetime, timedelta
import requests
import os
import pandas as pd
import seaborn as sns
import time
import hashlib
import hmac
import uuid
import matplotlib.pyplot as plt
from telegram_push import send_photo_telegram
from binance.error import ParameterRequiredError
from binance.spot import Spot as Client
from urllib.parse import urlencode

import binance_
import bybit
import aave
import plotting
import recurring_data

def main():
    if not os.path.exists("./data"):
        os.makedirs("./data")
    directory = os.getcwd() + "\\data" # in linux put "/data"
    now = datetime.now().strftime("%Y-%m-%d")
    print(f"query date: {now}")
    print("--binance--")
    binance_directory = binance_.binance(directory)
    print("--bybit--")
    bybit_directory = bybit.bybit(directory) # need keys in bybit code
    print("--aave--")
    aave_directory = aave.aave(directory)

    recurring_data.main(binance_directory, bybit_directory, aave_directory)
        
    chart_file = plotting.plotting(binance_directory, bybit_directory, aave_directory)

    files = [f for f in os.listdir(chart_file) if os.path.isfile(os.path.join(chart_file, f))]

    for file in files:
        print(file)

        if 'USDT' in file:
            send_photo_telegram(os.path.join(chart_file,file), "Borrow Rate CEX & Dex USDT")
        else:
            send_photo_telegram(os.path.join(chart_file,file), "Borrow Rate CEX & Dex USDC")
