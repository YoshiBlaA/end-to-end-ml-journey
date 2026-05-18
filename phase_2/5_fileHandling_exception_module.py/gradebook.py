from student import Student
import json

class GradeBook(Student):
    
    def __init__(self, course, students=None):
        
        """
        Initialize the GradeBook object with a course name and an empty dictionary for students.
        Args:
            course (str): The name of the course for which the gradebook is being created.
        """
        self.course = course
        self.students = students if students is not None else {}
        
    def add_student(self, student:Student):
        
        """
        Add a student to the gradebook. If a student with the same name already exists in the gradebook, a ValueError will be raised.
        Args:
            student (Student): The Student object to be added to the gradebook.
        Raises:
            ValueError: If a student with the same name already exists in the gradebook.
        """
        
        student_name = student.name
        if not student_name in self.students:
            self.students[student_name] = student
        else:
            raise ValueError(f"Student {student_name} already exists in the gradebook.")
        
    def save(self, json_filename:str):
        
        """
        Save the gradebook data to a JSON file. The JSON file will contain the course name and a list of students with their respective grades.
        Args:
                json_filename (str): The name of the JSON file to which the gradebook data will be saved.
        """
        
        with open(json_filename, "w") as f:
            
            """
            Create a dictionary representation of the gradebook data, which includes the course name and a list of students with their respective grades. This dictionary will then be serialized to JSON and written to the specified file.
            E.g.
            {
                "course": "Computer Science",
                "students": [
                    {
                        "name": "Alice",
                        "grades": {
                            "Math": [90, 85],
                            "Algorithms": [78]
                        }
                    },
                    {
                        "name": "Bob",
                        "grades": {
                            "Math": [70],
                            "Algorithms": [95]
                        }
                    }
                ]
            }
            """
            dictParse = {
                "course": self.course,
                "students": [
                    student.to_dict() for student in self.students.values()
                ]
            }          
            
            # Serialize the gradebook data to JSON and write it to the specified file with an indentation of 4 spaces for better readability.
            json.dump(dictParse, f, indent=4)
            
    @classmethod
    def load(cls, json_filename:str):
        
        """
        Load the gradebook data from a JSON file and reconstruct the GradeBook object. The JSON file is expected to contain the course name and a list of students with their respective grades. If the file is not found, is not a valid JSON file, or is missing required keys, appropriate exceptions will be raised.
        Args:
            json_filename (str): The name of the JSON file from which to load the gradebook data.
        Returns:
            GradeBook: A GradeBook object reconstructed from the data loaded from the JSON file.
        Raises:
            FileNotFoundError: If the specified JSON file is not found.
            json.JSONDecodeError: If the specified file is not a valid JSON file.
            KeyError: If the specified JSON file is missing required keys (e.g., "course" or "students").
        Self Notes:
            cls: The class method decorator allows this method to be called on the class itself rather than on an instance of the class. This is useful for creating a new instance of the GradeBook class based on the data loaded from the JSON file.
        """
        
        def reconstruct_student(student):
            
            """
            Reconstruct a Student object from a dictionary representation of a student, which includes the name and grades. This function will be used to create Student objects from the data loaded from the JSON file.
            Args:
                student (dict): A dictionary representation of a student, which includes the name and grades.
            Returns:
                Student: A Student object reconstructed from the provided dictionary.
            """
            return Student(student["name"], student["grades"])
        
        try:
            with open(json_filename, "r") as f:
                data = json.load(f)
            
            students = {student["name"] : reconstruct_student(student) for student in data["students"]}
            return cls(data["course"], students)
        
        except FileNotFoundError:
            raise FileNotFoundError(f"File {json_filename} not found. Cannot load gradebook.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"File {json_filename} is not a valid JSON file. Cannot load gradebook.")
        except KeyError:
            raise KeyError(f"File {json_filename} is missing required keys. Cannot load gradebook.")
            
    def summary(self):
        
        """
        Print a summary of the gradebook, including the course name and the overall average grade for each student. If there are no students in the gradebook, a ValueError will be raised.
        Raises:
            ValueError: If there are no students in the gradebook.
        """
        
        print(f'{self.course}')
        print("-----------------------------------")
        for student in self.students.values():
            print(student)
        print("-----------------------------------") 

if __name__ == "__main__":
    
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

    loaded = GradeBook.load("gradebook.json") # This will load the gradebook data from the "gradebook.json" file and reconstruct a GradeBook object based on that data. If the file is not found, is not a valid JSON file, or is missing required keys, appropriate exceptions will be raised.
    loaded.summary() # This will print a summary of the loaded gradebook, including the course name and the overall average grade for each student.