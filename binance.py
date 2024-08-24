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

def binance(directory):
    
    current_time = datetime.now()
    date_30_days_ago = current_time - timedelta(days=30)

    current_time = int(current_time.timestamp()*1000)
    date_30_days_ago = int(date_30_days_ago.timestamp()*1000)

    url = "https://www.binance.com/bapi/margin/v1/public/margin/vip/spec/history-interest-rate"

    params_USDT = {
        'asset' : 'USDT',
        'vipLevel' : 0,
        'size' : 90,
        'startTime' : date_30_days_ago,
        'endTime' : current_time
    }

    response_USDT = requests.get(url, params = params_USDT)

    df_USDT = pd.DataFrame(response_USDT.json()['data'])

    df_USDT['date'] = df_USDT['timestamp'].apply(lambda x : datetime.fromtimestamp(int(x)/1000).strftime("%Y-%m-%d"))

    df_USDT['daily_interest'] = df_USDT['dailyInterestRate'].apply(lambda x : float(x)*365*100)

    df_USDT = df_USDT.drop(columns = ['vipLevel','dailyInterestRate','timestamp'])
    
    params_USDC = {
        'asset' : 'USDC',
        'vipLevel' : 0,
        'size' : 90,
        'startTime' : date_30_days_ago,
        'endTime' : current_time
    }
    response_USDC = requests.get(url, params = params_USDC)

    df_USDC = pd.DataFrame(response_USDC.json()['data'])

    df_USDC['date'] = df_USDC['timestamp'].apply(lambda x : datetime.fromtimestamp(int(x)/1000).strftime("%Y-%m-%d"))

    df_USDC['daily_interest'] = df_USDC['dailyInterestRate'].apply(lambda x : float(x)*365*100)

    df_USDC = df_USDC.drop(columns = ['vipLevel','dailyInterestRate','timestamp'])
    
    df = pd.concat([df_USDT,df_USDC])
    
    csv_file = os.path.join(directory,"binance.csv")
    
    if os.path.exists(csv_file):
        os.remove(csv_file)
    
    df.to_csv(csv_file)    
    
    return csv_file