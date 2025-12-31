import pandas as pd
import psycopg2
from model import build_model

conn = psycopg2.connect(
    host="localhost",
    database="ecommerce",
    user="postgres",
    password="YOUR_PASSWORD"
)

df = pd.read_sql("SELECT rating, price FROM products", conn)
X = df[["rating"]].fillna(0)
y = df["price"]

model = build_model()
model.fit(X, y, epochs=10)
model.save("price_model.h5")
