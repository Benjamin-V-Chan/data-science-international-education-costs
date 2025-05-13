import pandas as pd
import json

if __name__ == '__main__':
    summary = pd.read_csv('../outputs/summary_statistics.csv', index_col=0)
    clusters = pd.read_csv('../outputs/clustered_data.csv')
    metrics = pd.read_csv('../outputs/regression_metrics.csv')
    report = {
        'SummaryStatistics': summary.loc['mean'].to_dict(),
        'ClusterCounts': clusters['Cluster'].value_counts().to_dict(),
        'Regression': metrics.to_dict(orient='records')[0]
    }
    with open('../outputs/final_report.json', 'w') as f:
        json.dump(report, f, indent=4)
