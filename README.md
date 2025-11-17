This repository is part of my personal data analytics portfolio. Please do not reproduce or distribute content without credit.

# End-to-End Snowflake Data Analytics Project: Tenant Credit Risk Dashboard

🏗️ **Project Overview**  
An end-to-end data analytics and automation project designed to demonstrate how Snowflake, Python, and Power BI can work together to analyze and predict tenant-level credit risk.  
The solution simulates a financial operations workflow—from raw data ingestion to machine learning and interactive reporting.

---

## 🔧 Tech Stack
- **Snowflake** – Cloud data warehouse for data storage and transformation  
- **Python (Pandas, scikit-learn)** – Data preparation and machine learning  
- **SQL** – KPI aggregation and risk metric computation  
- **Power BI** – Visualization and interactive dashboarding  

---

## ⚙️ Workflow Summary
1. **Data Generation:** Synthetic data simulating tenant payments, rent, and cashflow trends created in Python.  
2. **Snowflake Data Modeling:** Tables and analytical views created to calculate payment delays, rent collection %, and coverage ratios.  
3. **Risk Modeling:** Random Forest classifier used to label tenants as *High* or *Low Risk* based on KPIs.  
4. **Power BI Visualization:** Interactive dashboard built to monitor rent efficiency, payment discipline, and portfolio health.

---

## 📊 Key Insights
- Identified tenants with delayed payments and low coverage ratios.  
- Segmented portfolio by industry and risk profile.  
- Demonstrated scalable Snowflake–Python integration for financial analytics.

---

## 📂 Repository Contents
| File | Description |
|------|--------------|
| `generate_portfolio_data.py` | Generates synthetic tenant, property, and payment data |
| `credit_risk_model.py` | Connects Python to Snowflake and trains the ML model |
| `schema_and_view.sql` | SQL scripts for database, schema, and KPI view creation |
| `Tenant_Risk_Dashboard.pbix` | Power BI dashboard file |
| `Tenant_Risk_Scored.csv` | Final dataset with risk predictions |
| `project_summary.pdf` | One-page business summary of the project |

---

## 🧠 Business Context
This project reflects how modern financial analytics teams integrate **data warehousing, automation, and visualization** to drive insights.  
The same pipeline can be adapted for:
- Credit performance tracking  
- Rent/lease management  
- Portfolio performance analytics  
- Predictive finance dashboards

---
