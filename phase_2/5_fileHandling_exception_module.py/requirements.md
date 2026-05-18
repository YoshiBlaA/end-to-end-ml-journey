# Exercise: StudentGradeBook

## Requirements

### Student class:

**Attributes**

- name
- grades  (empty dict — {"Math": [85, 90, 78], ...})

**Methods**

- add_grade(subject, score) — appends score to that subject's list, creates it if it doesn't exist
- average(subject) — returns average score for a subject, raises ValueError if subject doesn't exist
- overall_average() — average across all grades
- __str__ — e.g. "Alice — Overall avg: 87.3"

### GradeBook class (main):

**Attributes**

- course
- students (empty dict — {"Alice": Student, ...})

**Methods**

- add_student(student) — adds student by name, raises ValueError if already exists
- get_student(name) — returns the student, raises KeyError if not found
- save(filename) — saves to JSON
- load(filename) — classmethod reconstructs from JSON.
    - handles FileNotFoundError, json.JSONDecodeError, KeyError
- summary() — prints all students and their overall average

## Expected behavior
    gb = GradeBook("Computer Science")

    alice = Student("Alice")
    bob   = Student("Bob")

    alice.add_grade("Math", 90)
    alice.add_grade("Math", 85)
    alice.add_grade("Algorithms", 78)

    bob.add_grade("Math", 70)
    bob.add_grade("Algorithms", 95)

    gb.add_student(alice)
    gb.add_student(bob)

    gb.save("gradebook.json")

    loaded = GradeBook.load("gradebook.json")
    loaded.summary()

## Expected output:
    📚 Computer Science
    -----------------------------------
    Alice — Overall avg: 84.3
    Bob   — Overall avg: 82.5
    -----------------------------------