"""
Exercise 5 — pivot_table
    data = {
        "region":   ["North", "North", "South", "South", "East", "East"],
        "quarter":  ["Q1", "Q2", "Q1", "Q2", "Q1", "Q2"],
        "revenue":  [30000, 45000, 28000, 33000, 51000, 47000]
    }
Create a pivot table showing the total revenue per region and quarter.
"""

import pandas as pd

data = {
        "region":   ["North", "North", "South", "South", "East", "East"],
        "quarter":  ["Q1", "Q2", "Q1", "Q2", "Q1", "Q2"],
        "revenue":  [30000, 45000, 28000, 33000, 51000, 47000]
    }

df = pd.DataFrame(data)

pivoted = df.pivot_table(
                        index = "region",
                        columns= "quarter",
                        values= "revenue",
                        aggfunc= 'sum'
                        )

print(pivoted)