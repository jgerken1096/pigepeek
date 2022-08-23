# csv_helpers.py
import pandas as pd


# Function called at bot startup
def verify_and_create_csv_file():
    # If file has no header, add file header
    try:
        df = pd.read_csv("emoji_counter.csv")
    except (pd.errors.EmptyDataError, FileNotFoundError):
        print('File was empty. New CSV file created')
        df = pd.DataFrame(columns=['user_id', 'emoji_count'])
        df.to_csv(r'emoji_counter.csv', index=False)
        return

    # Confirming columns are appropriately named
    df = pd.read_csv("emoji_counter.csv")
    columns = list(df.columns)
    if columns != ['user_id', 'emoji_count']:
        print('Header was changed. Rewriting header')
        df = pd.DataFrame(columns=['user_id', 'emoji_count'])
        df.to_csv(r'emoji_counter.csv', index=False)
        return


# Increases the user's emoji count by one
def increase_emoji_count(user_id):
    df = pd.read_csv("emoji_counter.csv")

    if user_id not in df.user_id.values:
        # New User
        df_new_user = pd.DataFrame(data=[[user_id, 1]],
                                   columns=['user_id', 'emoji_count']).convert_dtypes(convert_integer=True)
        df = pd.concat([df, df_new_user])
        df.to_csv(r'emoji_counter.csv', index=False)
    else:
        # Existing User
        query = df.where(df.user_id == user_id).convert_dtypes(convert_integer=True).emoji_count

        df.update(query + 1)
        df.to_csv(r'emoji_counter.csv', index=False)

