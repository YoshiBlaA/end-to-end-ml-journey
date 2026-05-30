"""
Tasks
Pandas:

    1. Select all Electronics orders from CDMX using loc
    2. Calculate total revenue, average units sold, and number of orders per city using groupby
    3. Create a pivot table showing average revenue per category and quarter

Matplotlib + Seaborn:

    4. Histogram of revenue distribution
    5. Boxplot of units sold per city
    6. Bar chart of total revenue per category
    7. Heatmap of average revenue per city and quarter
    8. Pair plot of units_sold, price, discount and revenue
"""

import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    "order_id":   range(1, 101),
    "city":       np.random.choice(["CDMX", "MTY", "GDL", "QRO", "PUE"], size=100),
    "category":   np.random.choice(["Electronics", "Clothing", "Food", "Furniture"], size=100),
    "quarter":    np.random.choice(["Q1", "Q2", "Q3", "Q4"], size=100),
    "units_sold": np.random.randint(1, 50, size=100),
    "price":      np.random.randint(100, 5000, size=100),
    "discount":   np.random.choice([0, 0.05, 0.10, 0.15, 0.20], size=100)
}

df = pd.DataFrame(data)
df["revenue"] = df["units_sold"] * df["price"] * (1 - df["discount"])

electronics_only = df["category"] == "Electronics"
cdmx_only = df["city"] == "CDMX"
filter_condition = electronics_only & cdmx_only

print(df.loc[filter_condition], "\n")

#print(filter_condition[filter_condition].count()) # For ensuring purposes

groupby_city = df.groupby("city")
result = groupby_city.agg(
                                                    total_revenue = ("revenue", "sum"),
                                                    average_units_sold = ('units_sold', 'mean'),
                                                    number_of_orders = ('order_id', 'count')
                                                )
print(result)