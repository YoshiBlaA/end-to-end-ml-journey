"""
Build a MealPlan class that contains multiple Food objects (reuse your class from before).

- Requirements
    - Food class — same as before, no changes needed.
    - MealPlan class attributes:
        - name — e.g. "Bulk Day"
        - meals — empty list where Food objects will be stored

- MealPlan class methods:

    - add_food(food) — appends a Food object to meals and prints a message
    - total_protein() — returns combined protein across all foods
    - total_calories() — returns combined calories across all foods
    - summary() — prints a structured breakdown like below
    
Expected behavior
    pythonchicken = Food("Chicken", protein=30, calories=165)
    rice    = Food("Rice",    protein=4,  calories=130)
    eggs    = Food("Eggs",    protein=6,  calories=70)

    chicken.consume(4)
    rice.consume(3)
    eggs.consume(3)

    plan = MealPlan("Bulk Day")
    plan.add_food(chicken)
    plan.add_food(rice)
    plan.add_food(eggs)

    plan.summary()
    
Expected output:
    ➕ Chicken added to Bulk Day
    ➕ Rice added to Bulk Day
    ➕ Eggs added to Bulk Day

    📋 Bulk Day
    -----------------------------------
    Chicken — Protein: 120g | Calories: 660 kcal
    Rice — Protein: 12g | Calories: 390 kcal
    Eggs — Protein: 18g | Calories: 210 kcal
    -----------------------------------
    Total protein: 150g
    Total calories: 1260 kcal
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
    
class MealPlan:
    def __init__(self, name: str):
        self.name = name
        self.meals = []
        
    def add_food(self, food: Food):
        self.meals.append(food)
        print(f'➕ {food.name} added to {self.name}')
        
    def total_protein(self):
        return sum(food.total_protein() for food in self.meals)

    def total_calories(self):
        return sum(food.total_calories() for food in self.meals)

    def summary(self):
        print(f'\n📋 {self.name}')
        print('-----------------------------------')
        for food in self.meals:
            print(food)
        print('-----------------------------------')
        print(f'Total protein: {self.total_protein()}g')
        print(f'Total calories: {self.total_calories()} kcal')
        
chicken = Food("Chicken", protein=30, calories=165)
rice    = Food("Rice",    protein=4,  calories=130)
eggs    = Food("Eggs",    protein=6,  calories=70)

chicken.consume(4)
rice.consume(3)
eggs.consume(3)

plan = MealPlan("Bulk Day")
plan.add_food(chicken)
plan.add_food(rice)
plan.add_food(eggs)

plan.summary()