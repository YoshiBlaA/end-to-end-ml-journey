"""
Exercise 2 — Filtering
    data = {
        "student":  ["Sofia", "Diego", "Valeria", "Miguel", "Fernanda"],
        "grade":    [85, 92, 78, 95, 88],
        "city":     ["CDMX", "MTY", "CDMX", "GDL", "MTY"]
    }
Select all students with a grade above 90. Then select only students from CDMX with a grade above 80.
"""

import pandas as pd

data = {
        "student":  ["Sofia", "Diego", "Valeria", "Miguel", "Fernanda"],
        "grade":    [85, 92, 78, 95, 88],
        "city":     ["CDMX", "MTY", "CDMX", "GDL", "MTY"]
    }

df = pd.DataFrame(data)

grade_abv90 = df["grade"] > 90
students_ab_90 = df.loc[grade_abv90, "student"]
print(students_ab_90)

grade_abv80 = df["grade"] > 80
cdmx_students = df["city"] == "CDMX"
students_cdmx_abv90 = df.loc[cdmx_students & grade_abv80]
print(students_cdmx_abv90)