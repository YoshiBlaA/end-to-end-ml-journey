from models.exercise import StrengthExercise
from models.workout import Workout
from utils.file_handler import save_workout, load_workout
from utils.analyzer import analyze

if __name__ == "__main__":

    f_name = "workout_log.txt"

    data = [
        ("Bench Press",    "chest",     3, 8,  80),
        ("Squat",          "legs",      4, 6,  100),
        ("Overhead Press", "shoulders", 3, 10, 50),
    ]
    exercises = [StrengthExercise(n, m, s, r, w) for n, m, s, r, w in data]

    w = Workout("2026-05-22")
    
    # Remember to unpack the list, or Workout will extend an object, not a list
    w.add_exercise(*exercises)
    
    w.summary()
    
    analyze(exercises)
    
    print("=== File ===")
    save_workout(w, f_name)
    load_workout(f_name)
    
    