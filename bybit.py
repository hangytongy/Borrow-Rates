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

def genSignature(current_time,api_key,secret_key,recv_window,payload):
    print(payload)
    param_str= str(current_time) + api_key + recv_window + str(payload)
    print(param_str)
    hash = hmac.new(bytes(secret_key, "utf-8"), param_str.encode("utf-8"),hashlib.sha256)
    signature = hash.hexdigest()
    return signature

def param_to_str(params):
    param_str = ''
    for key in params.keys():
        if param_str == '':
            param_str = param_str + key + "=" + str(params[key]) 
        else:
            param_str = param_str + "&" + key + "=" + str(params[key]) 
            
    return param_str

def bybit(directory):

    api_key='' #key here
    secret_key='' #key here
    recv_window=str(10000)
    url="https://api.bybit.com/v5/spot-margin-trade/interest-rate-history" # endpoint

    current_time = datetime.now()
    date_30_days_ago = current_time - timedelta(days=30)

    current_time = int(current_time.timestamp()*1000)
    date_30_days_ago = int(date_30_days_ago.timestamp()*1000)


    params_USDT = {
        'currency' : 'USDT',
        'startTime' : date_30_days_ago,
        'endTime' : current_time,
    }

    param_str = param_to_str(params_USDT)

    signature_USDT = genSignature(current_time,api_key,secret_key,recv_window,param_str)

    headers_USDT = {
        'X-BAPI-SIGN': signature_USDT,  # Replace with your actual signature
        'X-BAPI-API-KEY': api_key,  # Replace with your actual API key
        'X-BAPI-TIMESTAMP': str(current_time),  # Replace with your actual timestamp
        'X-BAPI-RECV-WINDOW': recv_window,
    }

    response_USDT = requests.get(url,headers=headers_USDT,params = params_USDT)

    df_USDT = pd.DataFrame(response_USDT.json()['result']['list'])
    df_USDT['date'] = df_USDT['timestamp'].apply(lambda x : datetime.fromtimestamp(int(x)/1000).strftime("%Y-%m-%d") )
    df_USDT['daily_interest'] = df_USDT['hourlyBorrowRate'].apply(lambda x : float(x)*24*365*100)
    df_USDT = df_USDT.drop(columns = ['timestamp','hourlyBorrowRate','vipLevel'])


    params_USDC = {
        'currency' : 'USDC',
        'startTime' : date_30_days_ago,
        'endTime' : current_time,
    }

    param_str = param_to_str(params_USDC)

    signature_USDC = genSignature(current_time,api_key,secret_key,recv_window,param_str)

    headers_USDC = {
        'X-BAPI-SIGN': signature_USDC,  # Replace with your actual signature
        'X-BAPI-API-KEY': api_key,  # Replace with your actual API key
        'X-BAPI-TIMESTAMP': str(current_time),  # Replace with your actual timestamp
        'X-BAPI-RECV-WINDOW': recv_window,
    }

    response_USDC = requests.get(url,headers=headers_USDC,params = params_USDC)

    df_USDC = pd.DataFrame(response_USDC.json()['result']['list'])
    df_USDC['date'] = df_USDC['timestamp'].apply(lambda x : datetime.fromtimestamp(int(x)/1000).strftime("%Y-%m-%d") )
    df_USDC['daily_interest'] = df_USDC['hourlyBorrowRate'].apply(lambda x : float(x)*24*365*100)
    df_USDC = df_USDC.drop(columns = ['timestamp','hourlyBorrowRate','vipLevel'])

    df = pd.concat([df_USDT,df_USDC])

    df.rename(columns = {'currency' : 'asset'}, inplace = True)

    csv_file = os.path.join(directory,"bybit.csv")
    
    if os.path.exists(csv_file):
        os.remove(csv_file)
    
    df.to_csv(csv_file)    
    
    return csv_file