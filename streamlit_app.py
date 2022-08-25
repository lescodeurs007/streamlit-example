
# streamlit_app.py

import streamlit as st
import mysql.connector
# streamlit_app.py
\

# Initialize connection.
# Uses st.experimental_singleton to only run once.


conn = mysql.connector.connect(**st.secrets["mysql"])

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from STUDENTS")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
