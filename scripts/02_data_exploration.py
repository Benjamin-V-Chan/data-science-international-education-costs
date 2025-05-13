import pandas as pd

def load_clean_data(path):
    return pd.read_csv(path)

def summary_stats(df):
    return df.describe()

def category_counts(df, col):
    return df[col].value_counts()

def correlation(df):
    return df.corr()

if __name__ == '__main__':
    path = '../data/processed/cleaned_data.csv'
    df = load_clean_data(path)
    stats = summary_stats(df)
    stats.to_csv('../outputs/summary_statistics.csv')
    country_counts = category_counts(df, 'Country')
    country_counts.to_csv('../outputs/country_counts.csv')
    level_counts = category_counts(df, 'Level')
    level_counts.to_csv('../outputs/level_counts.csv')
    corr = correlation(df)
    corr.to_csv('../outputs/correlation_matrix.csv')