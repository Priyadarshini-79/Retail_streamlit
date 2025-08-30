#🛒 Retail Order Data Analysis
##📌 Project Overview

This project analyzes a retail dataset to uncover insights about sales, revenue, discounts, and profitability.
The end-to-end pipeline includes:

📥 Data Extraction from Kaggle using the Kaggle API

🧹 Data Cleaning and feature engineering in Python (Pandas)

🗄️ Database Integration by loading cleaned data into MySQL

📊 SQL Analysis using 20 queries to answer key business questions

🌐 Interactive Dashboard built with Streamlit to visualize insights

The goal is to simulate how data analysts generate actionable insights that help businesses improve sales performance and profitability.

##⚙️ Tech Stack

Python: Pandas, Matplotlib, Seaborn

SQL (MySQL): Queries, Group By, Aggregations

Kaggle API: Data extraction

Streamlit: Dashboard & visualization

GitHub: Code versioning & sharing

##📊 SQL Insights (Examples)

Some of the analysis performed using SQL:

Top 10 revenue-generating products

Top 5 cities with the highest profit margins

Total discount given per category

Average sale price per product category

Region with the highest average sale price

Total profit per category

Top 3 segments with highest order quantities

Average discount % per region

Category with the highest total profit

Total revenue generated per year

##🚀 How to Run Locally

Clone the repository:

git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py


Open in browser:

http://localhost:8501

##📈 Key Business Insights

📌 Technology products had the highest profit margins

📌 Office Supplies drove high sales but low profits due to discounts

📌 South region showed highest average sales price

📌 Discounts above 20% reduced profitability significantly

📌 Year-over-year revenue showed consistent growth
