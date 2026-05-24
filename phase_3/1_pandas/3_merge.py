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
Merge both DataFrames so that all orders appear, even if they have no delivery status.
"""

