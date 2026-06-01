"""
Tasks
Pandas:

    1. Select all Electronics orders from CDMX using loc
    2. Calculate total revenue, average units sold, and number of orders per city using groupby
    3. Create a pivot table showing average revenue per category and quarter

Matplotlib:

    4. Histogram of revenue distribution
    5. Boxplot of units sold per city
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# 1. Select all Electronics orders from CDMX using loc

electronics_only = df["category"] == "Electronics"
cdmx_only = df["city"] == "CDMX"
filter_condition = electronics_only & cdmx_only

print(df.loc[filter_condition], "\n")

#-----------------------------------------------------------------------

# 2. Calculate total revenue, average units sold, and number of orders per city using groupby

groupby_city = df.groupby("city")
result = groupby_city.agg(
                                                    total_revenue = ("revenue", "sum"),
                                                    average_units_sold = ('units_sold', 'mean'),
                                                    number_of_orders = ('order_id', 'count')
                                                )

print(result, "\n")

#-----------------------------------------------------------------------

# 3. Create a pivot table showing average revenue per category and quarter

pivot_table = df.pivot_table(
                                values="revenue",
                                index="category",
                                columns="quarter",
                                aggfunc="mean"
                            )

print(pivot_table, "\n")

#-----------------------------------------------------------------------

#4. Histogram of revenue distribution
plt.figure(figsize=(10, 6))
plt.hist(df["revenue"], bins=20, color='skyblue', edgecolor='black')
plt.xticks()
plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.show()

#-----------------------------------------------------------------------

# 5. Boxplot of units sold per city
fig, ax = plt.subplots()
ax.set_ylabel("Units Sold")
fig.suptitle("Units Sold per City")

# X labels for boxplot
cities = df["city"].unique()

# Y values for boxplot for each city in the same order as cities list
units_sold_per_city = [
                        df["units_sold"][df["city"] == city].tolist() for city in cities
                    ]
bplot = ax.boxplot(
                    x = units_sold_per_city,
                    patch_artist = True,
                    tick_labels = cities, # will be used to label x-ticks
                    #meanprops = dict(color = "black", linewidth=2.5, linestyle='--') # Didnt work as expected
                    )

# Set different colors for each box
for patch, color in zip(bplot['boxes'], ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'lightgray']):
    patch.set_facecolor(color)
    
plt.show()

