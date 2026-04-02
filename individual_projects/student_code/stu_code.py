# Class Implementation:
class Student:
# Create a Student class with attributes: name, student_id, and a list to store grades
    def __init__(self):
        self.name = input("Enter the name of student: ")
        self.student_id = input(f"What is the student id for {self.name}: ")
        self.grades = []

# Implement methods to add grades, calculate average, and display student information
    def show_record(self):
        print(f"Name: {self.name}\nStudent Id: {self.student_id} ")
        print(f"Grades: ", end = "") 
        if not self.grades:
            print("None yet")
        else:
            total = 0.0
            count = len(self.grades)
            for i in self.grades:
                total += i
            average_grade = total / count
            print(f"{average_grade}")

#student add grade
    def add_grade(self):
        while True:
            new_student_grade = input("Enter the new grade: ")
            try:
                value = float(new_student_grade)
                if 0 <= value <= 100:
                    break
                else:
                    print("must be a valid input")
            except ValueError:
                print("Please enter a valid number")
        self.grades.append(value)

# beginning of main program
student = Student()
student.add_grade()
student.show_record()
# Create a GradeBook class to manage a collection of students
# Include methods to add students and find students by ID or name
# Grade Management:

# Develop methods to add individual grades to students
# Implement average calculation for each student
# Create a method to determine letter grade from numerical average (A=90+, B=80-89, C=70-79, D=60-69, F=<60)
# User Interface:

# Design a simple text-based menu with 5-6 basic options
# Allow users to add new students and enter grades
# Include options to view individual student records and class summary
# Keep the interface straightforward with numbered menu choices
# Basic Logic:

# Implement input validation for grades (0-100 range)
# Handle cases where students have no grades entered yet
# Include simple error handling for invalid menu choices

