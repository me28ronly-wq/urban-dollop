# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 19:10:16 2026

@author: pc
"""
# reading data
import pandas as pd
df = pd.read_csv(r"C:\Users\pc\Documents\Mercedes.file.csv", encoding="UTF-8")
df.head()
df.describe()
df.info()
print(df["fuel_type"].unique())
print(df["transmission"].unique())
df.columns = df.columns.str.strip()
df["model"] = df["model"].str.strip()
print(df.info(memory_usage='deep'))
print(df.describe(include='all'))

# analyzing
import sqlite3
conn = sqlite3.connect(':memory:')
df.to_sql('cars', conn, index= False)

# Average price vs. Average Mileage for the fuel type

query1 = """
   SELECT
      fuel_type,
      ROUND(AVG(price), 2) AS average_price,
      ROUND(AVG(mileage), 2) AS average_mileage,
      COUNT(model) AS no_of_cars
   FROM cars
   GROUP BY fuel_type
   HAVING no_of_cars > 100
   ORDER BY average_price DESC
"""
results_df = pd.read_sql_query(query1, conn)
print(results_df.head())

#plots
print(df.columns)

import matplotlib.pyplot as plt
plt.bar(results_df['fuel_type'], results_df['average_price'])
plt.xlabel("Fuel Type")
plt.ylabel("Average Price ($)")
plt.title("Average cars price by the Fuel Type")
plt.show

plt.bar(results_df['fuel_type'], results_df['average_mileage'])
plt.xlabel("Fuel Type")
plt.ylabel("Average Mileage (miles)")
plt.title("Average car mileage by Fuel Type")
plt.show



















