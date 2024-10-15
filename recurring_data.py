import pandas as pd
import numpy as np
import datetime as datetime
import os


def check_folder():
  if not os.path.exists("./recurring_data"):
    os.makedirs("./recurring_data")

def get_directory():
  directory = os.getcwd() + "/recurring_data"
  return directory

def file_exits(directory,file,df):
  get_path = os.path.join(directory,file)
  if not os.path.exists(get_path):
    df.to_csv(get_path)
  else:
    USDC = df[df['asset'].isin(["USDC"])]
    USDT = df[df['asset'].isin(["USDT"])]
    last_row_USDT = USDT.iloc[-1]
    last_row_USDC = USDC.iloc[-1]
    last_row_USDT.to_csv(get_path, mode='a', header=False, index=False)
    last_row_USDC.to_csv(get_path, mode='a', header=False, index=False)

def add_data(path):
  df = pd.read_csv(path)
  try:
    latest_date = df['date'].iloc[-1]

def main(binance_path,bybit_path,aave_path):
  #get df
  binance_df = pd.read_csv(binance_path)
  bybit_df = pd.read_csv(bybit_path)
  aave_df = pd.read_csv(aave_path)

  #check if path exist else create path
  check_folder()
  directory = get_directory()
  
  #check if path to exchange exist else write into individual path
  binance_file = "binance_recurring.csv"
  bybit_file = "bybit_recurring.csv"
  aave_file = "aave_recurring.csv"

  file_exists(directory,binance_file,binance_df)
  file_exists(directory,bybit_file,bybit_df)
  file_exists(directory,aave_file,aave_df)
