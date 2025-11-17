-- ==========================================================
-- Snowflake Schema & KPI View: Tenant Credit Risk Analytics
-- ==========================================================

-- 1️⃣ Create database and schema
CREATE OR REPLACE DATABASE REALTY_PORTFOLIO;
USE DATABASE REALTY_PORTFOLIO;

CREATE OR REPLACE SCHEMA PUBLIC;
USE SCHEMA PUBLIC;

-- 2️⃣ Create base tables
-- ----------------------------------------------------------

CREATE OR REPLACE TABLE TENANTS (
    TENANT_ID STRING PRIMARY KEY,
    TENANT_NAME STRING,
    INDUSTRY STRING
);

CREATE OR REPLACE TABLE PROPERTIES (
    PROPERTY_ID STRING PRIMARY KEY,
    TENANT_ID STRING,
    PROPERTY_TYPE STRING,
    LOCATION STRING,
    MONTHLY_RENT FLOAT
);

CREATE OR REPLACE TABLE PAYMENTS (
    PAYMENT_ID STRING PRIMARY KEY,
    TENANT_ID STRING,
    PAYMENT_DATE DATE,
    AMOUNT_PAID FLOAT,
    DUE_DATE DATE
);

-- 3️⃣ Analytical KPI View
-- ----------------------------------------------------------

CREATE OR REPLACE VIEW TENANT_KPI_SUMMARY AS
SELECT
    t.TENANT_ID,
    t.TENANT_NAME,
    t.INDUSTRY,
    ROUND(AVG((p.AMOUNT_PAID / pr.MONTHLY_RENT) * 100), 2) AS AVG_RENT_COLLECTION_PCT,
    ROUND(AVG(DATEDIFF('day', p.DUE_DATE, p.PAYMENT_DATE)), 2) AS AVG_PAYMENT_DELAY_DAYS,
    ROUND(AVG(p.AMOUNT_PAID / (pr.MONTHLY_RENT + 1)), 2) AS AVG_CASHFLOW_COVERAGE_RATIO
FROM TENANTS t
JOIN PROPERTIES pr ON t.TENANT_ID = pr.TENANT_ID
JOIN PAYMENTS p ON t.TENANT_ID = p.TENANT_ID
GROUP BY t.TENANT_ID, t.TENANT_NAME, t.INDUSTRY;

-- 4️⃣ Preview Data
-- ----------------------------------------------------------
SELECT * FROM TENANT_KPI_SUMMARY
LIMIT 10;
