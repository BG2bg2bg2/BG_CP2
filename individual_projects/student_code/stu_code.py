# Class Implementation:
class Student:
# Create a Student class with attributes: name, student_id, and a list to store grades
    def __init__(self, name, student_id):
        self.name = name
        student_id = student_id

# Implement methods to add grades, calculate average, and display student information
    def info(self, name, student_id):
        name = input("Enter the name of student: ")
        student_id = input(f"What is the student id for {name}: ")

class child(Student):
    def info(self):
        name = input("Enter name of student: ")
        student_id = input(f"What is the student id of {name}:")
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

