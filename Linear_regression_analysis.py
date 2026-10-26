from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Correctly select multiple columns as a DataFrame (100,000 rows, 5 columns)
x = df[['avg_order_value_usd', 'avg_session_duration_min', 'cart_abandonment_rate', 'Total_money_spend', 'Total_money_spend_for_each_customer']]
y = df['Profit_earned_from_customer']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
regression = LinearRegression()
regression.fit(x_train, y_train)
y_pred = regression.predict(x_test)

# Safely assign the test predictions to the DataFrame matching the split indices
df['y_pred'] = np.nan
df.loc[x_test.index, 'y_pred'] = y_pred

print("Predictions successfully aligned and stored!")
display(df.loc[x_test.index, ['Total_money_spend', 'y_pred']].head())
print(df.head(10))

from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test,y_pred)
print("mean square error",mse)
print("r2 score",r2)

import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Fix: Use the correct features dataset (lowercase x) which matches y (100,000 samples)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the models
ridge = Ridge(alpha=1.0)
ridge.fit(X_train_scaled, y_train)
lasso = Lasso(alpha=100.0) # Note: High alpha may zero out many coefficients
lasso.fit(X_train_scaled, y_train)

# Inspect the calculated coefficients and intercept
print("--- Calculated Coefficients ---")
coeff_df = pd.DataFrame({
    'Feature': x.columns,
    'Ridge Coefficient': ridge.coef_,
    'Lasso Coefficient': lasso.coef_
})
print(coeff_df)
print(f"\nRidge Intercept: {ridge.intercept_:.2f}")
print(f"Lasso Intercept: {lasso.intercept_:.2f}\n")

ridge_preds = ridge.predict(X_test_scaled)
lasso_preds = lasso.predict(X_test_scaled)

mse_ridge = mean_squared_error(y_test, ridge_preds)
mse_lasso = mean_squared_error(y_test, lasso_preds)
r2_ridge = r2_score(y_test, ridge_preds)
r2_lasso = r2_score(y_test, lasso_preds)

print(f"Ridge MSE: {mse_ridge:.2f}, R2: {r2_ridge:.2f}")
print(f"Lasso MSE: {mse_lasso:.2f}, R2: {r2_lasso:.2f}")

# Fix: Assign predictions to their specific columns
df['ridge_pred'] = np.nan
df.loc[X_test.index, 'ridge_pred'] = ridge_preds

df['lasso_pred'] = np.nan
df.loc[X_test.index, 'lasso_pred'] = lasso_preds

print(df.loc[X_test.index, ['Total_money_spend', 'Profit_earned_from_customer', 'ridge_pred', 'lasso_pred']].head(10))
print(df.head(10))
