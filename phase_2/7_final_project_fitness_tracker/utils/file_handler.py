# utils/file_handler.py

from models.workout import Workout
from models.exercise import StrengthExercise

def save_workout(workout: Workout, filename: str):

    """
    Save a workout to a text file in CSV format.
    Args:
        workout (Workout): The workout object to save.
        filename (str): The name of the file to save the workout to.
    """
    try:
        with open(filename, "w") as f:
            for ex in workout.exercises:
                f.write(f'{ex.name},{ex.muscle_group},{ex.sets},{ex.reps},{ex.weight}\n')
    except Exception as e:
        print(f"Error occurred while saving workout: {e}")
    finally:
        print(f"Workout saved to {filename} ✅")
            
def load_workout(filename: str):
    
    """
    Load a workout from a text file and print its contents.
    Args:
        filename (str): The name of the file to load the workout from.
    """
    print("Workout loaded successfully ✅")
    with open(filename, "r") as f:
        print(f'--- {filename}  content ---')
        for line in f:
            print(line.strip())
             
if __name__ == "__main__":
    f_name = "workout_log.txt"
    bench = StrengthExercise("Bench Press", "chest", sets=3, reps=8, weight=80)
    squat = StrengthExercise("Squat", "legs", sets=4, reps=6, weight=100)
    ohp = StrengthExercise("Overhead Press", "shoulders", sets=3, reps=10, weight=50)
    w = Workout("2026-05-22")
    w.add_exercise(bench, squat, ohp)  # *args: receives all three at once
    save_workout(w, f_name)
    load_workout(f_name)