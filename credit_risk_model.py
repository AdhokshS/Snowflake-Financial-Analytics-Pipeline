import pandas as pd
import snowflake.connector
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# --- Connect to Snowflake ---
conn = snowflake.connector.connect(
    user='ADHOKSH',
    password='SherlockAdhoksh@8699',
    account='wgc80663.us-east-1',     
    warehouse='COMPUTE_WH',
    database='REALTY_PORTFOLIO',
    schema='PUBLIC'
)

# --- Pull data again (just for safety) ---
query = "SELECT * FROM tenant_kpi_summary;"
df = pd.read_sql(query, conn)
df.columns = df.columns.str.lower()

# --- Create target & model ---
df['delayed_flag'] = np.where(df['avg_payment_delay_days'] > 3, 1, 0)
features = ['avg_rent_collection_pct', 'avg_cashflow_coverage_ratio']

X = df[features]
y = df['delayed_flag']

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# --- Add predictions & export ---
df['predicted_delay_flag'] = model.predict(X)
df.to_csv(r"d:\Snowflake Tenant Project\Tenant_Credit_Risk_Scored.csv", index=False)

print("✅ File successfully created at d:\\Snowflake Tenant Project\\Tenant_Credit_Risk_Scored.csv")

conn.close()
