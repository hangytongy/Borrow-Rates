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

def get_data(asset,asset_id,end_date,tmr):
    url = f"https://api.kamino.finance/kamino-market/7u3HeHxYDLhnCoErrtycNokbQYbWGzLs6JSDqGAv5PfF/reserves/{asset_id}/metrics/history?env=mainnet-beta&start={end_date}&end={tmr}"
    response = requests.get(url)
    dates = []
    borrow_apy = []

    for data in response.json()['history']:
        timestamp = data['timestamp']
        timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
        formatted_date = timestamp.strftime('%Y-%m-%d')
        dates.append(formatted_date)
        borrow = data['metrics']['borrowInterestAPY']*100
        borrow_apy.append(borrow)
    df = pd.DataFrame({
        'time': dates,
        'daily_interest': borrow_apy
    })
    df = df.groupby('time').mean()
    df['asset'] = asset
    df = df.reset_index()
    df['daily_interest'] = df['daily_interest'].apply(lambda x : round(x,1))
    
    return df

def kamino(directory):
    today = datetime.today()
    end_date = today - timedelta(days = 30)
    tmr = today + timedelta(days = 30)

    tmr = tmr.strftime('%Y-%m-%d')
    end_date = end_date.strftime('%Y-%m-%d')

    assets = {
            'USDC' : "D6q6wuQSrifJKZYpR1M8R4YawnLDtDsMmWM1NbBmgJ59" , 
              'USDT' : "H3t6qZ1JkguCNTi9uzVKqQ7dvt2cum4XiXWom6Gn5e5S"
             }
    df_overall = pd.DataFrame(columns=['time', 'daily_interest', 'asset'])
    
    for asset in assets:
        print(asset)
        df = get_data(asset, assets[asset],end_date,tmr)
        df_overall = pd.concat([df_overall, df], axis=0, ignore_index=True)

    csv_file = os.path.join(directory,"kamino.csv")

    if os.path.exists(csv_file):
        os.remove(csv_file)

    df_overall.to_csv(csv_file) 
    
    return csv_file
