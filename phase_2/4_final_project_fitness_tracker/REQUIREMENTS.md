# Mini project — Fitness Tracker CLI

A command-line fitness tracker that logs workouts, analyzes performance and saves/loads data from a file.

The user creates a workout, adds exercises to it, saves it to a `.txt` file, loads it back, and runs a performance analysis using NumPy.

---

## Structure

```
fitness_tracker/
|-- main.py           ← entry point, ties everything together
|-- models/
|   |-- __init__.py   ← makes models/ a package (can be empty)
|   |-- exercise.py   ← defines what an exercise IS
|   |-- workout.py    ← defines what a workout IS (contains exercises)
|-- utils/
|   |-- __init__.py   ← makes utils/ a package (can be empty)
|   |-- file_handler.py  ← handles saving and loading to .txt
|   |-- analyzer.py      ← analyzes workout performance with NumPy
```

---

## File by file

---

### `exercise.py`

**Purpose:** Define two types of exercises using OOP inheritance.

**What to build:**

```
Exercise (base class)
├── attributes: name, muscle_group
└── method: __str__ → prints basic info

StrengthExercise (inherits from Exercise)
├── extra attributes: sets, reps, weight
├── method: volume() → returns sets * reps * weight
└── method: __str__ → prints full info including volume
```

**Example behavior:**
```python
ex = StrengthExercise("Bench Press", "chest", sets=3, reps=8, weight=80)
print(ex)
# Bench Press | chest | 3x8 @ 80kg | volume: 1920
```

---

### `workout.py`

**Purpose:** A workout is a container that holds multiple exercises and can summarize them.

**What to build:**

```
Workout
├── attributes: date (string), exercises (empty list)
├── method: add_exercise(*args) → receives one or more StrengthExercise objects and adds them to the list
├── method: total_volume()     → uses map + lambda to get volume of each exercise, returns the sum
└── method: summary()          → prints date, all exercises, and total volume
```

**Example behavior:**
```python
w = Workout("2026-05-22")
w.add_exercise(bench, squat, ohp)  # *args: receives all three at once
w.summary()
# === Workout Summary ===
# Date: 2026-05-22
# Bench Press     | chest     | 3x8  @ 80kg  | volume: 1920
# Squat           | legs      | 4x6  @ 100kg | volume: 2400
# Overhead Press  | shoulders | 3x10 @ 50kg  | volume: 1500
# Total volume: 5820 kg
```

---

### `file_handler.py`

**Purpose:** Save a workout summary to a `.txt` file and load it back. Handle errors if the file doesn't exist or fails.

**What to build:**

```python
def save_workout(workout, filename):
    # opens filename in write mode
    # writes each exercise as a line: "name,muscle_group,sets,reps,weight"
    # uses try/except → prints "Workout saved to {filename} ✅" or the error

def load_workout(filename):
    # opens filename in read mode
    # reads and prints each line
    # uses try/except FileNotFoundError → prints error message
```

**Example behavior:**
```
Workout saved to workout_log.txt ✅
Workout loaded successfully ✅
--- workout_log.txt content ---
Bench Press,chest,3,8,80
Squat,legs,4,6,100
Overhead Press,shoulders,3,10,50
```

---

### `analyzer.py`

**Purpose:** Take a list of exercise volumes and use NumPy to find performance metrics. Filter exercises that are above average.

**What to build:**

```python
def analyze(exercises, *args):
    # *args: optional extra volumes to include in analysis
    # convert all volumes to a NumPy array
    # calculate max, min, mean using NumPy (vectorized)
    # use broadcasting to compare each volume against the mean
    # use filter + lambda to get names of exercises above average volume
    # print the full analysis report
```

**Example behavior:**
```
=== Analysis ===
Max volume:    2400
Min volume:    1500
Mean volume:   1940.0
Above average: ['Bench Press', 'Squat']
```

---

### `main.py`

**Purpose:** Entry point. Creates everything, connects all modules, and runs the full program.

**What to build:**
- Import `StrengthExercise` from `models.exercise`
- Import `Workout` from `models.workout`
- Import `save_workout`, `load_workout` from `utils.file_handler`
- Import `analyze` from `utils.analyzer`
- Use a **list comprehension** to create multiple exercises from raw data
- Create a `Workout`, add all exercises, print summary
- Save to file, load from file
- Run analyzer

**Example data to use:**
```python
data = [
    ("Bench Press",    "chest",     3, 8,  80),
    ("Squat",          "legs",      4, 6,  100),
    ("Overhead Press", "shoulders", 3, 10, 50),
]
exercises = [StrengthExercise(n, m, s, r, w) for n, m, s, r, w in data]
```

---

## Expected final output

```
=== Workout Summary ===
Date: 2026-05-22
Bench Press     | chest     | 3x8  @ 80kg  | volume: 1920
Squat           | legs      | 4x6  @ 100kg | volume: 2400
Overhead Press  | shoulders | 3x10 @ 50kg  | volume: 1500

Total volume: 5820 kg

=== Analysis ===
Max volume:    2400
Min volume:    1500
Mean volume:   1940.0
Above average: ['Bench Press', 'Squat']

=== File ===
Workout saved to workout_log.txt ✅
Workout loaded successfully ✅
--- workout_log.txt content ---
Bench Press,chest,3,8,80
Squat,legs,4,6,100
Overhead Press,shoulders,3,10,50
```

---

## Topics covered

| Topic | Where |
|---|---|
| OOP — inheritance | `exercise.py` |
| OOP — composition | `workout.py` |
| `*args` | `add_exercise()`, `analyze()` |
| `map` + `lambda` | `total_volume()` |
| `filter` + `lambda` | above average in `analyzer.py` |
| File handling + exceptions | `file_handler.py` |
| NumPy — vectorized ops + broadcasting | `analyzer.py` |
| Modules + packages | entire structure |
| List comprehensions | `main.py` |