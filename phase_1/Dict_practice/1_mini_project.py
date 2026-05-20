"""
You have this dictionary:
    pythongastos = {
        "food": 3200,
        "transport": 850,
        "entertainment": 1500,
        "clothing": 2100,
        "services": 950
    }

Requirements:

    - Loop through all items and print each category with its amount
    - Calculate and print total, average, highest and lowest expense
    - Use .items(), sum(), len(), max(), min() with key=gastos.get

Expected output:
    === Expense Report ===
    food:          $3200
    transport:      $850
    entertainment: $1500
    clothing:       $2100
    services:       $950

    Total:           $8600
    Average:         $1720.0
    Highest expense: food ($3200)
    Lowest expense:  transport ($850)
"""

pythongastos = {
    "food": 3200,
    "transport": 850,
    "entertainment": 1500,
    "clothing": 2100,
    "services": 950
}

print("=== Expense Report ===")
for category, amount in pythongastos.items():
    print(f'{category.ljust(15)}: ${amount}')
    
total = sum(pythongastos.values())
average = round(total / len(pythongastos), 2)
highest_expense = max(pythongastos.items(), key = lambda item : item[1])
lowest_expense = min(pythongastos.items(), key = lambda item : item[1])

print(f'\nTotal: ${total}')
print(f'Average: ${average}')
print(f'Highest expense: {highest_expense[0]} (${highest_expense[1]})')
print(f'Lowest expense: {lowest_expense[0]} (${lowest_expense[1]})')