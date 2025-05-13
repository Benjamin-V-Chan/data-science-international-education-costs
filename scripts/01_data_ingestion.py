import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna(subset=['Tuition_USD', 'Living_Cost_Index'])
    df['Duration_Years'] = df['Duration_Years'].astype(int)
    return df

def save_clean_data(df, path):
    df.to_csv(path, index=False)

if __name__ == '__main__':
    raw_path = '../data/raw/International_Education_Costs.csv'
    processed_path = '../data/processed/cleaned_data.csv'
    df = load_data(raw_path)
    df_clean = clean_data(df)
    save_clean_data(df_clean, processed_path)