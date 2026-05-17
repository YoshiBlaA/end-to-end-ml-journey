"""
Extend your Food class with two subclasses for different types of food.

- Requirements
    - Food base class — make one small change: replace total_protein() and total_calories() with:
        - def total_protein(self):
            raise NotImplementedError("Subclasses must implement total_protein()")
        - def total_calories(self):
           raise NotImplementedError("Subclasses must implement total_calories()")

- WholeFood(Food) — whole ingredients (chicken, rice, eggs)

    - Same behavior as your original Food class
    - total_protein() → sum(registry) * protein
    - total_calories() → sum(registry) * calories
    - __str__ → same format as before

- ProcessedFood(Food) — packaged food with fixed macros per unit

    - Extra attribute: sodium (mg per serving)
    - total_protein() and total_calories() — same logic as WholeFood
    - __str__ → adds sodium to the output:
        - Protein Bar — Protein: 40g | Calories: 380 kcal | Sodium: 600mg
        
- Expected behavior
    chicken = WholeFood("Chicken", protein=30, calories=165)
    rice    = WholeFood("Rice",    protein=4,  calories=130)
    bar     = ProcessedFood("Protein Bar", protein=20, calories=190, sodium=300)

    chicken.consume(3)
    rice.consume(2)
    bar.consume(2)

    print(chicken)
    print(rice)
    print(bar)
    
- Expected output:
    ✅ Consumed 3 servings of Chicken
    ✅ Consumed 2 servings of Rice
    ✅ Consumed 2 servings of Protein Bar
    Chicken — Protein: 90g | Calories: 495 kcal
    Rice — Protein: 8g | Calories: 260 kcal
    Protein Bar — Protein: 40g | Calories: 380 kcal | Sodium: 600mg
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
         
    def total_calories(self):
        return sum(self.registry) * self.calories
    
    def total_protein(self):
        return sum(self.registry) * self.protein
    
    def __str__(self):
        return f'{self.name} — Protein: {self.total_protein()}g | Calories: {self.total_calories()} kcal'
    
class WholeFood(Food):
    def __init__(self, name:str, protein:int, calories:int):
        super().__init__(name, protein, calories)
    
class ProcessedFood(Food):
    def __init__(self, name:str, protein:int, calories:int, sodium:int):
        super().__init__(name, protein, calories)
        self.sodium = sodium
    
    def __str__(self):
        return f'{super().__str__()} | Sodium: {self.sodium*sum(self.registry)}mg'    
    
chicken = WholeFood("Chicken", protein=30, calories=165)
rice    = WholeFood("Rice",    protein=4,  calories=130)
bar     = ProcessedFood("Protein Bar", protein=20, calories=190, sodium=300)

chicken.consume(3)
rice.consume(2)
bar.consume(2)

print(chicken)
print(rice)
print(bar)