class Student:
    
    """
    This class represents a student with a name and a dictionary of grades for different subjects.
    """
    
    def __init__(self, name, grades=None):
        
        """
        Initialize the Student object with a name and an empty dictionary for grades.
        Args:
            name (str): The name of the student.
        """
        
        self.name = name
        self.grades = grades if grades is not None else {}
        
    def add_grade(self, subject:str, grade:int) -> None:
        
        """
        Add a grade for a specific subject. If the subject does not exist in the grades dictionary, it will be created.
        Args:
            subject (str): The name of the subject.
            grade (int): The grade to be added for the subject.
        """
        
        if not subject in self.grades:
            #print(f"Subject {subject} not found, creating new subject.")
            self.grades[subject] = []
            self.grades[subject].append(grade)
            return
            
        #print(f"Subject {subject} found, adding grade to existing subject.")
        self.grades[subject].append(grade)
        
    def average(self, subject:str) -> float:
        
        """
        Calculate the average grade for a specific subject. If the subject does not exist in the grades dictionary, a ValueError will be raised.
        Args:
            subject (str): The name of the subject for which to calculate the average grade.
        Returns:
            float: The average grade for the specified subject.
        Raises:
            ValueError: If the subject is not found in the grades dictionary.    
        """
        
        try:
            average = sum(self.grades[subject]) / len(self.grades[subject])
            return average
        except:
            raise ValueError(f"Subject {subject} not found, cannot calculate average.")
    
    def overall_average(self):
        
        """
        Calculate the overall average grade across all subjects. If there are no grades available, a ValueError will be raised.
        Returns:
            float: The overall average grade across all subjects.   
        """
        
        if len(self.grades) > 0:
            total_grades = []
            for subject in self.grades:
                total_grades.extend(self.grades[subject])
                
            avg = sum(total_grades) / len(total_grades)
            
            return round(avg, 2)
        else:
            raise ValueError(f"No grades available, cannot calculate overall average.")
        
    def __str__(self) -> str:
        
        """
        Return a string representation of the Student object, which includes the name and overall average grade.

        Returns:
            str: A string representation of the Student object.
        """
        return f'{self.name} - Overall avg: {self.overall_average()}'    
    
    def to_dict(self)-> dict:
        
        """
        Return a dictionary representation of the Student object, which includes the name and grades.
        Returns:
            dict: A dictionary representation of the Student object.
        """

        return {
                "name": self.name,
                "grades": self.grades
                }
    
if __name__ == "__main__":
    student = Student("Victor")
    student.add_grade("Math", 85)
    student.add_grade("Science", 90)
    student.add_grade("Math", 95)
    student.add_grade("History", 80)
    #print(student.average("Ethics")) # This will raise a ValueError because "Ethics" is not a subject in the student's grades.
    print(student.grades)
    print(student.overall_average()) # This will print the overall average of all grades for the student.
    print(student) # This will print the string representation of the student, which includes the name and overall average.
    print(student.to_dict()) # This will print the dictionary representation of the student, which includes the name and grades.