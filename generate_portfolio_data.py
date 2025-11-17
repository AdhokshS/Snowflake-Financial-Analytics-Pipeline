
import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)
np.random.seed(42)
random.seed(42)

# ----------- CONFIGURATION ------------
NUM_TENANTS = 30         # number of tenants
MONTHS = ["2025-01", "2025-02", "2025-03", "2025-04", "2025-05", "2025-06"]
REGIONS = ["West", "East", "North", "South"]
INDUSTRIES = ["Retail", "Healthcare", "Manufacturing", "Restaurants", "Logistics", "Tech"]
CREDIT_RATINGS = ["AAA", "AA", "A", "BBB", "BB", "B"]

# ----------- GENERATE TENANTS ------------
tenants = []
for i in range(1, NUM_TENANTS + 1):
    tenants.append({
        "tenant_id": f"T{i:03d}",
        "tenant_name": fake.company(),
        "industry": random.choice(INDUSTRIES),
        "annual_revenue": random.randint(5_000_000, 50_000_000),
        "credit_rating": random.choice(CREDIT_RATINGS)
    })

tenants_df = pd.DataFrame(tenants)
tenants_df.to_csv("Tenants.csv", index=False)

# ----------- GENERATE PROPERTIES ------------
properties = []
for tenant in tenants_df["tenant_id"]:
    num_properties = random.randint(1, 3)
    for _ in range(num_properties):
        monthly_rent = random.randint(30_000, 150_000)
        properties.append({
            "property_id": f"P{len(properties)+1:03d}",
            "tenant_id": tenant,
            "region": random.choice(REGIONS),
            "property_value": monthly_rent * random.randint(40, 80),
            "monthly_rent": monthly_rent
        })

properties_df = pd.DataFrame(properties)
properties_df.to_csv("Properties.csv", index=False)

# ----------- GENERATE PAYMENTS ------------
payments = []
for month in MONTHS:
    for _, row in properties_df.iterrows():
        due_date = datetime.strptime(month + "-05", "%Y-%m-%d")
        delay = random.choice([0, 0, 1, 2, 5, 10])  # occasional delays
        rent_paid = row["monthly_rent"] if delay <= 2 else row["monthly_rent"] * 0.9  # partial payment if delayed
        payments.append({
            "payment_id": f"PAY{len(payments)+1:04d}",
            "tenant_id": row["tenant_id"],
            "month": month,
            "rent_due": row["monthly_rent"],
            "rent_paid": rent_paid,
            "payment_date": (due_date + timedelta(days=delay)).strftime("%Y-%m-%d")
        })

payments_df = pd.DataFrame(payments)
payments_df.to_csv("Payments.csv", index=False)

print("✅ Generated 3 CSV files: Tenants.csv, Properties.csv, and Payments.csv")
