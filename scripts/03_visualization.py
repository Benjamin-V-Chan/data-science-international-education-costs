import pandas as pd
import matplotlib.pyplot as plt

def load_data(path):
    return pd.read_csv(path)

if __name__ == '__main__':
    df = load_data('../data/processed/cleaned_data.csv')
    plt.hist(df['Tuition_USD'], bins=30)
    plt.title('Distribution of Tuition USD')
    plt.savefig('../outputs/tuition_histogram.png')
    plt.clf()
    plt.hist(df['Rent_USD'], bins=30)
    plt.title('Distribution of Rent USD')
    plt.savefig('../outputs/rent_histogram.png')
    plt.clf()
    top_countries = df['Country'].value_counts().nlargest(10).index
    df_top = df[df['Country'].isin(top_countries)]
    df_top.boxplot(column='Living_Cost_Index', by='Country', rot=45)
    plt.title('Living Cost Index by Country')
    plt.suptitle('')
    plt.savefig('../outputs/living_cost_boxplot.png')
    plt.clf()
    avg_tuition = df.groupby('Level')['Tuition_USD'].mean()
    avg_tuition.plot(kind='bar')
    plt.title('Average Tuition by Level')
    plt.ylabel('USD')
    plt.savefig('../outputs/avg_tuition_by_level.png')