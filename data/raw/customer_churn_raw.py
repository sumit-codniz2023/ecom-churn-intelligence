import os
import numpy as np
import pandas as pd

# Create local directories
os.makedirs('data/raw', exist_ok=True)

# Generate dataset (100,000 rows)
np.random.seed(42)
n_samples = 100000

df = pd.DataFrame({
    'customer_id': [f'CUST-{1001 + i}' for i in range(n_samples)],
    'tenure_months': np.random.randint(1, 48, size=n_samples),
    'avg_session_duration_min': np.round(
        np.random.uniform(1.0, 30.0, size=n_samples), 1
    ),
    'support_tickets_raised': np.random.randint(0, 8, size=n_samples),
    'avg_order_value_usd': np.round(
        np.random.uniform(20.0, 300.0, size=n_samples), 2
    ),
    'cart_abandonment_rate': np.round(
        np.random.uniform(0.0, 1.0, size=n_samples), 2
    ),
    'device_category': np.random.choice(
        ['Mobile', 'Desktop', 'Tablet'], size=n_samples
    ),
    'churn': np.random.choice([0, 1], size=n_samples, p=[0.75, 0.25]),
})
df['Total_money_spend'] = np.random.randint(500, 1000, size=n_samples)

# Calculate the service cost for each customer based on support tickets and session duration
# Each support ticket costs $30, and each minute of session costs $0.50
base_cost = (df['support_tickets_raised'] * 30.0) + (df['avg_session_duration_min'] * 0.50)

# Ensure the company's cost to serve does not exceed the customer's spend (making it realistic)
df['Total_money_spend_for_each_customer'] = np.minimum(base_cost, df['Total_money_spend'] * 0.5)
print(df.head(10))
# Save as CSV
df.to_csv('customer_churn_raw_data.csv', index=False)
print('CSV file generated successfully on your machine!')
