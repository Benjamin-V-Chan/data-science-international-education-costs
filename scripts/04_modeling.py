import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

if __name__ == '__main__':
    df = pd.read_csv('../data/processed/cleaned_data.csv')
    features = ['Living_Cost_Index', 'Rent_USD', 'Visa_Fee_USD', 'Insurance_USD']
    X = df[features]
    kmeans = KMeans(n_clusters=5, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X)
    df.to_csv('../outputs/clustered_data.csv', index=False)
    X_reg = X
    y = df['Tuition_USD']
    model = LinearRegression()
    model.fit(X_reg, y)
    y_pred = model.predict(X_reg)
    rmse = mean_squared_error(y, y_pred, squared=False)
    r2 = r2_score(y, y_pred)
    metrics = pd.DataFrame({'RMSE': [rmse], 'R2': [r2]})
    metrics.to_csv('../outputs/regression_metrics.csv', index=False)
    coef = pd.DataFrame({'Feature': features, 'Coefficient': model.coef_})
    coef.to_csv('../outputs/regression_coefficients.csv', index=False)