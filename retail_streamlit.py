#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# ------------------------ DATABASE CONNECTION ------------------------
def get_connection():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Mahe@1970",
        database="retail_orders"
    )
    return connection

# ------------------------ EXECUTE QUERY ------------------------
def execute_query(query):
    connection = get_connection()
    cursor = connection.cursor()
    query = query.strip().replace('\n', ' ')
    cursor.execute(query)
    result = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    df = pd.DataFrame(result, columns=columns)
    connection.close()
    return df

# ------------------------ LOAD QUERIES ------------------------
def load_queries(file_path):
    query_dict = {}
    with open(file_path, 'r') as file:
        raw_queries = file.read().strip().split(';')
        for query in raw_queries:
            lines = query.strip().split('\n')
            title = None
            query_body = []
            for line in lines:
                if line.startswith('--'):
                    title = line.replace('--', '').strip()
                else:
                    query_body.append(line.strip())
            if title and query_body:
                query_dict[title] = ' '.join(query_body).strip()
    return query_dict

# Load queries from the file
queries = load_queries('C:\\Users\\pmdar\\retail_orders.sql')

# ------------------------ STREAMLIT UI ------------------------
st.title("📊 Retail Order Data Analysis")

# Dropdown to select the query
selected_query = st.selectbox("Select a Query", list(queries.keys()))
query = queries[selected_query]

# Option to display as Table or Chart
display_option = st.radio("Display as:", ("Table", "Chart"))

# Run button
if st.button("Run Query"):
    df = execute_query(query)

    if not df.empty:
        if display_option == "Table":
            st.write("### Results as Table")
            st.dataframe(df)

        elif display_option == "Chart":
            st.write("### Results as Chart")

            # 🔥 Improved Chart Matching Logic:
            if 'year' in df.columns and len(df.columns) == 2:
                st.line_chart(df.set_index('year'))  # Line Chart for Time Series

            elif 'product_id' in df.columns and 'total_revenue' in df.columns:
                st.bar_chart(df.set_index('product_id')['total_revenue'])  # Bar Chart for Revenue by Product

            elif 'category' in df.columns and 'percentage_contribution' in df.columns:
                # Pie Chart for Contribution
                fig, ax = plt.subplots()
                df.set_index('category')['percentage_contribution'].plot.pie(
                    autopct='%1.1f%%', startangle=90, ax=ax)
                st.pyplot(fig)

            elif 'City' in df.columns and 'total_profit' in df.columns:
                st.area_chart(df.set_index('City')['total_profit'])  # Area Chart for Profit by City

            elif len(df.columns) == 2 and df.dtypes[0] != 'object' and df.dtypes[1] != 'object':
                st.scatter_chart(df)  # Scatter Plot for numeric comparisons

            elif len(df.columns) == 1 and df.dtypes[0] != 'object':
                st.bar_chart(df)  # Single Column Data Bar Chart

            elif len(df.columns) == 2 and df.dtypes[0] == 'object':
                # Line Chart for Category or Region based data
                st.line_chart(df.set_index(df.columns[0]))

            else:
                st.write("⚠️ Chart format not available for this data.")

    else:
        st.write("⚠️ No data available for this query.")



# In[ ]:




