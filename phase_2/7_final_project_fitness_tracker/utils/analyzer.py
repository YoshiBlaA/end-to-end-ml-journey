from models.workout import StrengthExercise
import numpy as np

def analyze(exercises: list[StrengthExercise], *args):
    
    """
    Take a list of exercise volumes and use NumPy to find the performance metrics.
    Filter exercises that are above average.
    
    Args:
        exercises (list[StrengthExercise]): list of StrenghtExercise objects.
        *args: optional extra volumes to include in analysis.
    """

    exercises_volume_list = list(map(lambda ex: ex.volume(), exercises))
    volumes_np = np.array(list(exercises_volume_list))
    max_volume = np.max(volumes_np)
    min_volume = np.min(volumes_np)
    avg_volume = np.mean(volumes_np)
        
    above_avg = list(filter(lambda ex: ex.volume() > avg_volume, exercises))
    above_avg_names = [ex.name for ex in above_avg]
    print("=== Analysis ===")
    print(f"Max Volume: {max_volume} kg")
    print(f"Min Volume: {min_volume} kg")
    print(f"Mean volume: {avg_volume:.2f} kg")
    print(f'Above average: {above_avg_names} \n')


if __name__ == "__main__":
    
    data = [
        ("Bench Press",    "chest",     3, 8,  80),
        ("Squat",          "legs",      4, 6,  100),
        ("Overhead Press", "shoulders", 3, 10, 50),
    ]
    exercises = [StrengthExercise(name, muscle_group, sets, reps, weight) for name, muscle_group, sets, reps, weight in data]
    
    analyze(exercises)