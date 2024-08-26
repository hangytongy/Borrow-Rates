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
from binance.error import ParameterRequiredError
from binance.spot import Spot as Client
from urllib.parse import urlencode

def binance(directory):
    
    key = ""
    secret = ""
    
    def test_margin_interest_rate_history(params):
        """Tests the API endpoint to query margin interest rate history"""

        client = Client(key, secret)
        response = client.margin_interest_rate_history(**params)
        return response

    current_time = datetime.now()
    date_30_days_ago = current_time - timedelta(days=30)

    current_time = int(current_time.timestamp()*1000)
    date_30_days_ago = int(date_30_days_ago.timestamp()*1000)

    params = {
        'asset' : 'USDT',
        'size' : 90,
        'startTime' : date_30_days_ago,
        'endTime' : current_time,
        'recvWindow': 20000,
        "timestamp": current_time
    }


    response_USDT = test_margin_interest_rate_history(params)

    df_USDT = pd.DataFrame(response_USDT)
    print(df_USDT.head(1))

    df_USDT['date'] = df_USDT['timestamp'].apply(lambda x : datetime.fromtimestamp(int(x)/1000).strftime("%Y-%m-%d"))

    df_USDT['daily_interest'] = df_USDT['dailyInterestRate'].apply(lambda x : float(x)*365*100)

    df_USDT = df_USDT.drop(columns = ['vipLevel','dailyInterestRate','timestamp'])
    
    params = {
        'asset' : 'USDC',
        'size' : 90,
        'startTime' : date_30_days_ago,
        'endTime' : current_time,
        'recvWindow': 20000,
        "timestamp": current_time
    }
    response_USDC = test_margin_interest_rate_history(params)

    df_USDC = pd.DataFrame(response_USDC)
    print(df_USDC.head(1))

    df_USDC['date'] = df_USDC['timestamp'].apply(lambda x : datetime.fromtimestamp(int(x)/1000).strftime("%Y-%m-%d"))

    df_USDC['daily_interest'] = df_USDC['dailyInterestRate'].apply(lambda x : float(x)*365*100)

    df_USDC = df_USDC.drop(columns = ['vipLevel','dailyInterestRate','timestamp'])
    
    df = pd.concat([df_USDT,df_USDC])
    
    csv_file = os.path.join(directory,"binance.csv")
    
    if os.path.exists(csv_file):
        os.remove(csv_file)
    
    df.to_csv(csv_file)    
    
    return csv_file