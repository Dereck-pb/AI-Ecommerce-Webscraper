import streamlit as st
import psycopg2
import pandas as pd
from ai.predict import predict_price

st.title("AI E-Commerce Dashboard")

conn = psycopg2.connect(
    host="localhost",
    database="ecommerce",
    user="postgres",
    password="YOUR_PASSWORD"
)

df = pd.read_sql("SELECT * FROM products", conn)
st.dataframe(df)

rating = st.slider("Rating", 0.0, 5.0, 4.0)
st.write("Predicted Price:", predict_price(rating))
