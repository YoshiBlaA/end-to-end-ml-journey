"""
Student grade book

You have this dictionary:
    grades = {
        "math": 88,
        "physics": 74,
        "history": 91,
        "english": 63,
        "programming": 95
    }

Requirements:

    - Loop through all subjects and print each one with its grade
    - Calculate and print total, average, highest and lowest grade
    - Print a status next to each grade: 
        - PASS if >= 70, 
        - FAIL if < 70
    - Use .items(), sum(), len(), max(), min() with key=grades.get

Expected output:
    === Grade Book ===
    math           : 88  PASS
    physics        : 74  PASS
    history        : 91  PASS
    english        : 63  FAIL
    programming    : 95  PASS

    Total:           411
    Average:         82.2
    Highest grade:   programming (95)
    Lowest grade:    english (63)
"""

if __name__ == "__main__":

    grades = {
        "math": 88,
        "physics": 74,
        "history": 91,
        "english": 63,
        "programming": 95
    }


    print("=== Grade Book ===")
    for subject, grade in grades.items():
        status = "PASS" if grade >= 70 else "FAIL"
        print(f'{subject.ljust(15)} : {grade} {status}')
        
    total = sum(grades.values())
    average = total / len(grades)
    highest_grade = max(grades, key = grades.get)
    lowest_grade = min(grades, key = grades.get)
    print(f'Total: {total}')
    print(f'Average: {average:.1f}')
    print(f'Highest grade: {highest_grade} ({grades[highest_grade]})')
    print(f'Lowest grade: {lowest_grade} ({grades[lowest_grade]})')