# bank-customer-risk-analytics
Data analytics project focused on customer behavior, transaction trends, and risk profiling in a banking environment. Includes Power BI dashboard, SQL analysis, and business insights.
# 🏦 Bank Customer Risk Analytics Dashboard

## 📊 Project Overview

This project focuses on analyzing banking data to uncover customer behavior, transaction trends, and financial risk. The goal is to support data-driven decision-making through interactive dashboards and analytical insights.

---

## 🎯 Objectives

* Identify high-value customers
* Analyze transaction patterns
* Detect high-risk customers using credit scores
* Monitor loan performance and default rates
* Highlight potential fraudulent transactions

---

## 🧰 Tools & Technologies

* Power BI (Dashboard & Visualization)
* SQL (Data Querying)
* Python (Data Cleaning & Processing)
* Excel (Data Handling)

---

## 📁 Dataset Description

The dataset consists of:

* **Customers:** Demographics, income, credit score
* **Transactions:** Amount, type, location, date
* **Loans:** Loan amount, status, interest rate

---

## 📊 Dashboard Structure

### 🔹 Page 1: Overview

* Total Customers
* Total Transactions
* Total Transaction Amount
* Transaction Trends Over Time

### 🔹 Page 2: Customer Insights

* Income vs Spending Analysis
* Top Customers by Transaction Value
* Customer Segmentation

### 🔹 Page 3: Risk Analysis

* Customer Risk Classification (High, Medium, Low)
* Loan Default Rate
* Credit Score Distribution

### 🔹 Page 4: Fraud Detection

* Suspicious Transactions (High-value transactions)
* Transaction Behavior Analysis
* Device & Location Insights

---

## 🧠 Key Insights

* Customers with low credit scores (<580) are high risk
* A small percentage of customers contribute most of the revenue
* High transaction spikes may indicate unusual activity
* Loan defaults are strongly linked to credit score and income level

---

## 🧮 Sample SQL Queries

```sql
SELECT Customer_ID, SUM(Amount) AS Total_Spend
FROM Transactions
GROUP BY Customer_ID;
```

---

## ⚙️ Data Processing (Python)

* Removed duplicates
* Converted date formats
* Handled missing values
* Prepared data for analysis

---

## 📈 Business Impact

This dashboard enables:

* Better risk management
* Improved customer targeting
* Detection of suspicious financial activity
* Data-driven strategic decisions

---

## 🚀 Project Status

✅ Completed
🔄 Future Improvements:

* Machine learning risk prediction
* Real-time data integration
* Advanced fraud detection models

---

## 👤 Author

**Rinae Charlene Mabasa**
Data Analyst | Data Scientist | BI Developer
