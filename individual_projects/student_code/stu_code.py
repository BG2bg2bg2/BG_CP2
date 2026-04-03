import csv

# Class Implementation:
class Student:
# Create a Student class with attributes: name, student_id, and a list to store grades
    def __init__(self):
        self.name = input("Enter the name of student: ")
        self.student_id = input(f"What is the student id for {self.name}: ")
        self.grades = []
# Implement methods to add grades, calculate average, and display student information
    def show_record(self):
        print(f"Name: {self.name} Student Id: {self.student_id} ", end="")
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

# Create a GradeBook class to manage a collection of students
class GradeBook:
    def __init__(self):
        self.students = []

    def pick_student(self):
        if len(self.students) == 0:
            print("No students in list")
            return None

        for i in self.students:
            print(i.name, i.student_id)
        while True:
            enter_student_id = input("Enter the student id: ")
            for i in self.students:
                if i.student_id == enter_student_id:
                    return i

    def display_menu(self):
        while True:
            #input 1-6 else exit
            print("\n1 to add student to class\n2 to add grade to student\n3 to show grade record of student\n4 to view student grade average\n5 to view class grade average\n6 to save and exit\n")
            choice = input("Enter a number 1-6: ")
            if choice == "1":
                #add student
                student = Student()
                self.students.append(student)
            elif choice == "2":
                #add grade
                student = self.pick_student()
                if student != None:
                    student.add_grade()
            elif choice == "3":
                student = self.pick_student()
                student.show_record()
            elif choice == "4":
                #show all students in class
                for i in self.students:
                    i.show_record()
            elif choice == "5":
                student.class_summary()
            elif choice == "6":
                break
            else:
                print("must enter a valid number between 1-6")
                continue

grade = GradeBook()
grade.display_menu()
#    with open("BG_CP2\\individual_projects\\student_code\\student.csv", "r+", newline='\n') as csvfile:
#        fieldnames = ["student", "student_id", "grades", "advrage_grade"]
#        reader = csv.reader(csvfile)

# Include methods to add students and find students by ID or name
# Grade Management:

# Develop methods to add individual g

# Design a simple text-based menu with 5-6 basic options
# Allow users to add new students and enter grades
# Include options to view individual student records and class summary
# Keep the interface straightforward with numbered menu choices
# Basic Logic:

# Implement input validation for grades (0-100 range)
# Handle cases where students have no grades entered yet
# Include simple error handling for invalid menu choices

