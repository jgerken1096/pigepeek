# csv_helpers.py
import pandas as pd


# Function called at bot startup
def verify_and_create_csv_file():
    # If file has no header, add file header
    try:
        df = pd.read_csv("../emoji_counter.csv")
    except (pd.errors.EmptyDataError, FileNotFoundError):
        print('File was empty. New CSV file created')
        df = pd.DataFrame(columns=['user_id', 'emoji_count'])
        df.to_csv(r'emoji_counter.csv', index=False)
        return

    # Confirming columns are appropriately named
    df = pd.read_csv("../emoji_counter.csv")
    columns = list(df.columns)
    if columns != ['user_id', 'emoji_count']:
        print('Header was changed. Rewriting header')
        df = pd.DataFrame(columns=['user_id', 'emoji_count'])
        df.to_csv(r'emoji_counter.csv', index=False)
        return
