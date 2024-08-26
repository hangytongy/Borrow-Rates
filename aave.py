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

def query_():
    query = """
query ($reserve: String!, $timestamp_gt_1: Int!, $timestamp_lt_1: Int!, $timestamp_gt_2: Int!, $timestamp_lt_2: Int!, $timestamp_gt_3: Int!, $timestamp_lt_3: Int!, $timestamp_gt_4: Int!, $timestamp_lt_4: Int!,
 $timestamp_gt_5: Int!, $timestamp_lt_5: Int!, $timestamp_gt_6: Int!, $timestamp_lt_6: Int!, $timestamp_gt_7: Int!, $timestamp_lt_7: Int!, $timestamp_gt_8: Int!, $timestamp_lt_8: Int!, $timestamp_gt_9: Int!, $timestamp_lt_9: Int!,
  $timestamp_gt_10: Int!, $timestamp_lt_10: Int!, $timestamp_gt_11: Int!, $timestamp_lt_11: Int!, $timestamp_gt_12: Int!, $timestamp_lt_12: Int!, $timestamp_gt_13: Int!, $timestamp_lt_13: Int!, $timestamp_gt_14: Int!, $timestamp_lt_14: Int!,
   $timestamp_gt_15: Int!, $timestamp_lt_15: Int!, $timestamp_gt_16: Int!, $timestamp_lt_16: Int!, $timestamp_gt_17: Int!, $timestamp_lt_17: Int!, $timestamp_gt_18: Int!, $timestamp_lt_18: Int!, $timestamp_gt_19: Int!, $timestamp_lt_19: Int!,
   $timestamp_gt_20: Int!, $timestamp_lt_20: Int!, $timestamp_gt_21: Int!, $timestamp_lt_21: Int!, $timestamp_gt_22: Int!, $timestamp_lt_22: Int!, $timestamp_gt_23: Int!, $timestamp_lt_23: Int!, $timestamp_gt_24: Int!, $timestamp_lt_24: Int!,
   $timestamp_gt_25: Int!, $timestamp_lt_25: Int!, $timestamp_gt_26: Int!, $timestamp_lt_26: Int!, $timestamp_gt_27: Int!, $timestamp_lt_27: Int!, $timestamp_gt_28: Int!, $timestamp_lt_28: Int!, $timestamp_gt_29: Int!, $timestamp_lt_29: Int!,
   $timestamp_gt_30: Int!, $timestamp_lt_30: Int!, $timestamp_gt_31: Int!, $timestamp_lt_31: Int!) {
  t1: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_1, timestamp_lt: $timestamp_lt_1 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t2: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_2, timestamp_lt: $timestamp_lt_2 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t3: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_3, timestamp_lt: $timestamp_lt_3 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t4: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_4, timestamp_lt: $timestamp_lt_4 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t5: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_5, timestamp_lt: $timestamp_lt_5 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t6: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_6, timestamp_lt: $timestamp_lt_6 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t7: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_7, timestamp_lt: $timestamp_lt_7 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t8: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_8, timestamp_lt: $timestamp_lt_8 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t9: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_9, timestamp_lt: $timestamp_lt_9 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t10: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_10, timestamp_lt: $timestamp_lt_10 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t11: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_11, timestamp_lt: $timestamp_lt_11 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t12: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_12, timestamp_lt: $timestamp_lt_12 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t13: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_13, timestamp_lt: $timestamp_lt_13 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t14: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_14, timestamp_lt: $timestamp_lt_14 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t15: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_15, timestamp_lt: $timestamp_lt_15 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t16: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_16, timestamp_lt: $timestamp_lt_16 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t17: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_17, timestamp_lt: $timestamp_lt_17 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t18: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_18, timestamp_lt: $timestamp_lt_18 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t19: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_19, timestamp_lt: $timestamp_lt_19 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t20: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_20, timestamp_lt: $timestamp_lt_20 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t21: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_21, timestamp_lt: $timestamp_lt_21 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t22: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_22, timestamp_lt: $timestamp_lt_22 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t23: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_23, timestamp_lt: $timestamp_lt_23 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t24: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_24, timestamp_lt: $timestamp_lt_24 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t25: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_25, timestamp_lt: $timestamp_lt_25 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t26: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_26, timestamp_lt: $timestamp_lt_26 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t27: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_27, timestamp_lt: $timestamp_lt_27 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t28: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_28, timestamp_lt: $timestamp_lt_28 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t29: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_29, timestamp_lt: $timestamp_lt_29 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t30: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_30, timestamp_lt: $timestamp_lt_30 } ) { variableBorrowRate priceInUsd timestamp __typename }
  t31: reserveParamsHistoryItems( first: 1 where: { reserve: $reserve, timestamp_gt: $timestamp_gt_31, timestamp_lt: $timestamp_lt_31 } ) { variableBorrowRate priceInUsd timestamp __typename }
}
"""
    return query

def create_variables(no_of_days,reserve_id):
    now = datetime.now()
    days_ago_30_gt = now - timedelta(days = no_of_days)
    days_ago_30_lt = days_ago_30_gt + timedelta(hours = 5)
    
    variables = {f'timestamp_gt_{day}': int((days_ago_30_gt + timedelta(days = day)).timestamp())  for day in range(1,no_of_days+1) }
    variables2 = {f'timestamp_lt_{day}': int((days_ago_30_lt + timedelta(days = day)).timestamp())  for day in range(1,no_of_days+1) }
    for i in variables2.keys():
        variables[i] = variables2[i]
    
    variables["reserve"] = reserve_id
    
    return variables

def aave_query(asset):
    # Define the GraphQL endpoint
    url = "https://gateway-arbitrum.network.thegraph.com/api/a820147ae9eec25fbfa2f206671706b8/subgraphs/id/Cd2gEDVeqnjBn1hSeqFMitw8Q1iiyV9FYUZkLNRcL87g"


    # Define the GraphQL query as a string
    query = query_()

    # Set up the variables for the query
    if asset == "USDC":
        reserve_id = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb480x2f39d218133afab8f2b819b1066c7e434ad94e9e" #USDC
    else:
        reserve_id = "0xdac17f958d2ee523a2206206994597c13d831ec70x2f39d218133afab8f2b819b1066c7e434ad94e9e" #USDT
    no_of_days = 31
    variables = create_variables(no_of_days,reserve_id)

    # Send the POST request with the query and variables
    response = requests.post(url, json={'query': query, 'variables': variables})
    print(response.status_code)

    return response.json()

def data_xform(data,asset):
    timestamp = []
    rate = []
    for i in range(1,len(data)+1):
        timestamp.append(data[f't{i}'][0]['timestamp'])
        rate.append(int(data[f't{i}'][0]['variableBorrowRate'][:3])/100)

    df = {}
    df['timestamp'] = timestamp
    df['daily_interest'] = rate
    df = pd.DataFrame(df)
    df = df.sort_values(by='timestamp',ascending=True)
    df['time'] = df['timestamp'].apply(lambda x : datetime.fromtimestamp(x).strftime("%Y-%m-%d") )
    df.index = df.time
    df.drop(columns = ['timestamp','time'], inplace = True)
    df['asset'] = asset

    print(df.head(1))
    
    return df

def aave(directory):
    assets = ['USDC','USDT']

    df_overall = []

    for asset in assets:
        response = aave_query(asset)
        data = {k: v for k,v in response['data'].items() if v}
        df = data_xform(data,asset)
        df_overall.append(df)

    df_overall = pd.concat([df_overall[0],df_overall[1]])

    csv_file = os.path.join(directory,"aave.csv")

    if os.path.exists(csv_file):
        os.remove(csv_file)

    df_overall.to_csv(csv_file) 
    
    return csv_file