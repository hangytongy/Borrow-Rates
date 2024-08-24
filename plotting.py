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

def plotting(binance_directory, bybit_directory, aave_directory):
    #Binance
    nance = pd.read_csv(binance_directory)
    nance.index = pd.to_datetime(nance['date'])
    nance = nance.drop(columns = ["Unnamed: 0","date"])
    nance['asset'] = nance['asset'].apply(lambda x : x + "-binance")

    #Bybit
    bybit = pd.read_csv(bybit_directory)
    bybit.index = pd.to_datetime(bybit['date'])
    bybit = bybit.drop(columns = ["Unnamed: 0","date"])
    bybit['asset'] = bybit['asset'].apply(lambda x : x + "-bybit")

    #All Cex
    cex = pd.concat([nance,bybit])
    cex_USDT = cex[cex['asset'].isin(["USDT-bybit", "USDT-binance"])]
    cex_USDC = cex[cex['asset'].isin(["USDC-bybit", "USDC-binance"])]

    #Aave
    aave = pd.read_csv(aave_directory)
    aave = aave.rename(columns={'time':'date'})
    aave.index = pd.to_datetime(aave['date'])
    aave = aave.drop(columns = ['date'])
    aave['asset'] = aave['asset'].apply(lambda x: x+"-aave")

    #All dex
    dex = pd.concat([aave])
    dex_USDT = dex[dex['asset'].isin(['USDT-aave'])]
    dex_USDC = dex[dex['asset'].isin(['USDC-aave'])]

    dex_palette = {'USDT-aave': 'green', 'USDC-aave' : 'green'}
    chart_file = os.path.join(os.getcwd(),"charts")
    if not os.path.exists(chart_file):
        os.makedirs(chart_file)

    #USDT
    sns.set()

    plt.figure(figsize = (12,6))

    sns.lineplot(x = cex_USDT.index, y = 'daily_interest', hue = 'asset', data = cex_USDT, 
                 marker = "o",markers=True, errorbar = None, linewidth = 5)
    sns.lineplot(x = dex_USDT.index, y = 'daily_interest', hue = 'asset', data = dex_USDT,
                marker = "o", markers=True, errorbar = None, linewidth = 1, palette=dex_palette)

    plt.xlabel('time')
    plt.ylabel('interest rate')
    plt.title('Borrowing Interest Rate USDT')

    chart_file_USDT = os.path.join(chart_file,'int_rate_USDT.png')
    plt.savefig(chart_file_USDT)

    #USDC
    sns.set()

    plt.figure(figsize = (12,6))

    sns.lineplot(x = cex_USDC.index, y = 'daily_interest', hue = 'asset', data = cex_USDC,
                 marker = "o",markers=True, errorbar = None, linewidth = 5)
    sns.lineplot(x = dex_USDC.index, y = 'daily_interest', hue = 'asset', data = dex_USDC,
                marker = "o", markers=True, errorbar = None, linewidth = 1, palette=dex_palette)

    plt.xlabel('time')
    plt.ylabel('interest rate')
    plt.title('Borrowing Interest Rate USDC')

    chart_file_USDC = os.path.join(chart_file,'int_rate_USDC.png')
    plt.savefig(chart_file_USDC)

    return chart_file