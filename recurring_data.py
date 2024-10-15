import pandas as pd
import os

def check_folder():
    # Create the folder if it doesn't exist
    if not os.path.exists("./recurring_data"):
        os.makedirs("./recurring_data")

def get_directory():
    # Get the current working directory and append the folder
    directory = os.path.join(os.getcwd(), "recurring_data")
    return directory

def file_exists(directory, file, df):
    # Build the full path to the file
    get_path = os.path.join(directory, file)
    
    if not os.path.exists(get_path):
        # If the file doesn't exist, create it by saving the full DataFrame
        df.to_csv(get_path, index=False)
    else:
        # Filter for assets 'USDC' and 'USDT'
        USDC = df[df['asset'].isin(["USDC"])]
        USDT = df[df['asset'].isin(["USDT"])]
        
        # Check if filtered DataFrames are not empty before accessing rows
        if not USDT.empty:
            last_row_USDT = USDT.iloc[-1]
            last_row_USDT.to_csv(get_path, mode='a', header=False, index=False)
            
        if not USDC.empty:
            last_row_USDC = USDC.iloc[-1]
            last_row_USDC.to_csv(get_path, mode='a', header=False, index=False)

def add_data(path):
    # Read the CSV into a DataFrame
    df = pd.read_csv(path)
    
    try:
        # Get the latest date from the 'date' column
        latest_date = df['date'].iloc[-1]
        print(f"Latest date in {path} is: {latest_date}")
    except KeyError:
        print(f"Error: 'date' column not found in {path}")
    except IndexError:
        print(f"Error: The DataFrame for {path} is empty.")

def main(binance_path, bybit_path, aave_path):
    # Read CSV files
    binance_df = pd.read_csv(binance_path)
    bybit_df = pd.read_csv(bybit_path)
    aave_df = pd.read_csv(aave_path)

    # Check if the folder exists or create it
    check_folder()
    directory = get_directory()
    
    # File names
    binance_file = "binance_recurring.csv"
    bybit_file = "bybit_recurring.csv"
    aave_file = "aave_recurring.csv"

    # Check if files exist or append the latest data
    file_exists(directory, binance_file, binance_df)
    file_exists(directory, bybit_file, bybit_df)
    file_exists(directory, aave_file, aave_df)

    # Optionally, call add_data to check the latest date (if needed)
    add_data(os.path.join(directory, binance_file))
    add_data(os.path.join(directory, bybit_file))
    add_data(os.path.join(directory, aave_file))


