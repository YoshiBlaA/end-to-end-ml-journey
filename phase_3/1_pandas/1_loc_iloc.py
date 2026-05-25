"""
Exercise 1 — loc and iloc
    data = {
        "product":  ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
        "price":    [25000, 350, 800, 12000, 1500],
        "stock":    [10, 150, 80, 25, 60]
    }
Select the product name and price of items in positions 1 to 3 using iloc. Then select only the Monitor row using loc with a condition.
"""

import pandas as pd

data = {
        "product":  ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
        "price":    [25000, 350, 800, 12000, 1500],
        "stock":    [10, 150, 80, 25, 60]
    }

df = pd.DataFrame(data)

print(df.iloc[1:4, 0:2])

print("---------------------------------")

print(df.loc[df["product"] == "Monitor"])