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

def get_data(asset,asset_id,timestamp):
    
    # URL
    url = "https://aave-api-v2.aave.com/data/rates-history"

    # Query parameters
    params = {
        "reserveId": asset_id,
        "from":timestamp,
        "resolutionInHours": "24"
    }

    # Sending the GET request
    response = requests.get(url, params=params)

    # Handling the response
    if response.status_code == 200:
        print("Success!")
        data = transform_data(response.json(),asset)
        return data
    else:
        print(f"Failed! Status code: {response.status_code}")
        print(response.text)  # Prints error message if the request fails
        
def transform_data(data,ticker):

# Extracting time and variableBorrowRate_avg
    time_series = []
    variable_borrow_rate = []

    for entry in data:
        # Convert 'x' to a datetime object
        dt = datetime(entry['x']['year'], entry['x']['month']+1, entry['x']['date'], entry['x']['hours'])
        time_series.append(dt)
        variable_borrow_rate.append(round(entry['variableBorrowRate_avg']*100,2))

    # Create DataFrame
    df = pd.DataFrame({
        'time': time_series,
        'daily_interest': variable_borrow_rate,
        'asset' : ticker
    })

    return df

def aave(directory):
    current_date = datetime.now()
    one_month_before = current_date - timedelta(days = 30)
    timestamp = round(one_month_before.timestamp(),0)

    assets = {
            'USDC' : "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb480x2f39d218133AFaB8F2B819B1066c7E434Ad94E9e1" , 
              'USDT' : "0xdac17f958d2ee523a2206206994597c13d831ec70x2f39d218133AFaB8F2B819B1066c7E434Ad94E9e1"
             }
    df_overall = pd.DataFrame(columns=['time', 'daily_interest', 'asset'])
    
    for asset in assets:
        print(asset)
        df = get_data(asset, assets[asset],timestamp)
        df_overall = pd.concat([df_overall, df], axis=0, ignore_index=True)

    csv_file = os.path.join(directory,"aave.csv")

    if os.path.exists(csv_file):
        os.remove(csv_file)

    df_overall.to_csv(csv_file) 
    
    return csv_file