# models/exercise.py

class Exercise:
    
    """Base class for exercises."""
    
    def __init__(self, name: str, muscle_group: str):
        
        """
        Initialize an exercise with a name and muscle group.
        Args:
            name (str): The name of the exercise.
            muscle_group (str): The primary muscle group targeted by the exercise.
        """
        
        self.name = name
        self.muscle_group = muscle_group
        
    def __str__(self):
        
        """
        String representation of the exercise.
        Returns:
            str: A string describing the exercise.
        """
        return f"{self.name.ljust(15)} | {self.muscle_group.ljust(10)}"
    
class StrengthExercise(Exercise):
    
    """Represents a strength training exercise, inheriting from Exercise."""
    
    def __init__(self, name: str, muscle_group: str, sets: int, reps: int, weight: int):
        
        """
        Initialize a strength exercise with sets, reps, and weight.
        Args:
            name (str): The name of the exercise.
            muscle_group (str): The primary muscle group targeted by the exercise.
            sets (int): The number of sets performed.
            reps (int): The number of repetitions per set.
            weight (int): The weight lifted in kilograms.
        
        """
        
        super().__init__(name, muscle_group)
        self.sets = sets
        self.reps = reps
        self.weight = weight
       
    def volume(self):
        
        """
        Calculate the total volume of the exercise (sets x reps x weight). 
        Returns:
            int: The total volume lifted for the exercise.
        """
        
        return self.sets * self.reps * self.weight
        
    def __str__(self):
        
        """
        String representation of the strength exercise, including volume.
        Returns:
            str: A string describing the strength exercise with volume.
        """
        
        return f"{super().__str__()} | {self.sets} x {self.reps} @ {self.weight} kg {"".ljust(3)} | volume: {self.volume()}"

if __name__ == "__main__":
    ex = StrengthExercise("Bench Press", "chest", sets=3, reps=8, weight=80)
    print(ex)