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


import binance
import bybit
import aave
import plotting

def main():
    if not os.path.exists("./data"):
        os.makedirs("./data")
    directory = os.getcwd() + "\\data"
    now = datetime.now().strftime("%Y-%m-%d")
    print(f"query date: {now}")
    print("--binance--")
    binance_directory = binance.binance(directory)
    print("--bybit--")
    bybit_directory = bybit.bybit(directory) # need keys in bybit code
    print("--aave--")
    aave_directory = aave.aave(directory)
        
    chart_file = plotting.plotting(binance_directory, bybit_directory, aave_directory)

    files = [f for f in os.listdir(chart_file) if os.path.isfile(os.path.join(chart_file, f))]

    for file in files:
        print(file)
        
        send_photo_telegram(os.path.join(chart_file,file), "Borrow Rate CEX & Dex")
