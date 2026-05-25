"""
Exercise 3 — merge
    orders = pd.DataFrame({
        "order_id":   [1, 2, 3, 4],
        "customer":   ["Alice", "Bob", "Charlie", "Diana"]
    })

    deliveries = pd.DataFrame({
        "order_id": [1, 2, 5],
        "status":   ["delivered", "pending", "delivered"]
    })
Merge both DataFrames so that all orders appear.
"""

import pandas as pd

orders = pd.DataFrame({
        "order_id":   [1, 2, 3, 4],
        "customer":   ["Alice", "Bob", "Charlie", "Diana"]
    })

deliveries = pd.DataFrame({
        "order_id": [1, 2, 5],
        "status":   ["delivered", "pending", "delivered"]
    })

values = {"customer": "Unknown customer", "status": "no orders / pending"}
merged = pd.merge(orders, deliveries, how="outer").fillna(value = values)

print(merged)