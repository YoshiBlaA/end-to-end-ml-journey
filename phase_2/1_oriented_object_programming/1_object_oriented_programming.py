"""
Create a Food class to track what you eat throughout the day.

- Requirements

    Attributes (defined in __init__):

    - name — e.g. "Chicken"
    - protein — grams of protein per serving
    - calories — calories per serving
    - registry — empty list where consumed servings will be stored
    
- Methods:

    - consume(servings) — appends an int n to the log and prints a message
    - total_protein() — returns the total protein from all logged entries
    - total_calories() — returns the total calories from all logged entries
    - __str__ — should display something like:
          Chicken — Protein: {self.total_protein()}g | Calories: {self.total_calories()} kcal
          
- Expected behavior

    chicken = Food("Chicken", protein=30, calories=165)
    rice    = Food("Rice",    protein=4,  calories=130)

    chicken.consume(2)
    chicken.consume(3)
    rice.consume(1)

    print(chicken)
    print(rice)
    print(f"Total daily protein: {chicken.total_protein() + rice.total_protein()}g")

- Expected output:
    ✅ Consumed 2 servings of Chicken
    ✅ Consumed 3 servings of Chicken
    ✅ Consumed 1 servings of Rice
    Chicken — Protein: 150g | Calories: 825 kcal
    Rice — Protein: 4g | Calories: 130 kcal
    Total daily protein: 154g
"""

class Food:
    def __init__(self, name:str, protein:int, calories:int):
        self.name = name
        self.protein = protein
        self.calories = calories
        self.registry = []
        
    def consume(self, servings:int):
        if servings <= 0:
            print("❌ Invalid number of servings. Please enter a positive integer.")
            return
        self.registry.append(servings)
        print(f'✅ Consumed {servings} servings of {self.name}')
         
    def total_protein(self):
        return sum(self.registry)*self.protein
    
    def total_calories(self):
        return sum(self.registry)*self.calories
    
    def __str__(self):
        return f'{self.name} — Protein: {self.total_protein()}g | Calories: {self.total_calories()} kcal'
    
chicken = Food("Chicken", protein=30, calories=165)
rice = Food("Rice", protein=4, calories=130)

chicken.consume(2)
chicken.consume(3)
rice.consume(1)
rice.consume(0)  # Testing invalid input

print(chicken)
print(rice)
print(f"Total daily protein: {chicken.total_protein() + rice.total_protein()}g")