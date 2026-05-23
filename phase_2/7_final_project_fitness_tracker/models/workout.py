# models/workout.py

from models.exercise import StrengthExercise

class Workout:
    
    """Represents a workout session, containing multiple exercises performed on a specific date."""
    
    def __init__(self,  date:str):
        
        """
        Initialize a workout with a date and an empty list of exercises.
        Args:
            date (str): The date of the workout session in YYYY-MM-DD format.
        Static:
            exercises (list): A list to store the exercises performed during the workout.
        """
        
        self.date = date
        self.exercises = []
        
    def add_exercise(self, *args):
        
        """
        Add one or more exercises to the workout.
        Args:
            *args: Variable length argument list of StrengthExercise objects to add to the workout.
        """
        
        self.exercises.extend(args)
        
    def total_volume(self):
        
        """
        Calculate the total volume of all exercises in the workout.
        Returns:
            int: The total volume lifted across all exercises in the workout.
        """
        
        volume_per_exercise = map(lambda ex: ex.volume(), self.exercises)
        
        return sum(list(volume_per_exercise))
    
    def summary(self):
        
        """Print a summary of the workout, including date, exercises performed, and total volume."""
        
        print("=== Workout Summary ===")
        print(f"Date: {self.date}")
        
        #Use i only for debugging purposes
        #i = 1
        for ex in self.exercises:
            print(ex)
            #print(i, ex)
            #i+=1
        print(f"\nTotal Volume: {self.total_volume()} kg \n")
        
if __name__ == "__main__":
    bench = StrengthExercise("Bench Press", "chest", sets=3, reps=8, weight=80)
    squat = StrengthExercise("Squat", "legs", sets=4, reps=6, weight=100)
    ohp = StrengthExercise("Overhead Press", "shoulders", sets=3, reps=10, weight=50)
    w = Workout("2026-05-22")
    w.add_exercise(bench, squat, ohp)  # *args: receives all three at once
    w.summary()