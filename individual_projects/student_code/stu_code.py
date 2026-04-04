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
            score = self.get_average_score()
            grade = self.get_letter_grade(score)
            print(f"The total grade is: {score}\nLetter grade is: {grade}")
# Grade Management:
    def get_letter_grade(self, average_grade):
        if average_grade >= 90:
            letter = "A"
        elif average_grade >80:
            letter = "B"
        elif average_grade >= 70:
            letter = "C"
        elif average_grade >= 60:
            letter = "D"
        else:
            letter = "F"
        return letter

    def get_average_score(self):
        total = 0.0
        count = len(self.grades)
        if count == 0:
            return None
        else:
            for i in self.grades:
                total += i
            average_grade = total / count
            return average_grade


#student add grade
    def add_grade(self):
        while True:
# Develop methods to add individual grades

# Implement input validation for grades (0-100 range)
            new_student_grade = input("Enter the new grade 1 - 100: ")
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
        #makes a list for holding students
        self.students = []

    #what student do you want to choose and grade change
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


# Handle cases where students have no grades entered yet
    def class_summary(self):
        count = len(self.students)
        if count == 0:
            print("There are no students in the list")
            return

        total = 0.0
        count = 0

        for i in self.students:
            avg = i.get_average_score()
            if avg is not None:
                total += avg
                count += 1

        if count == 0:
            print("No grades available for class average")
        else:
            print(f"There are {count} student(s).\nClass average is {total / count}\nClass letter grade is: {self.students[0].get_letter_grade(total / count)}")


    def display_menu(self):
        while True:
            # Design a simple text-based menu with 5-6 basic options
            #input 1-6 else exit
            print("\n1 to add student to class\n2 to add grade to student\n3 to show grade record of student\n4 to view student grade average\n5 to view class grade average\n6 to save and exit\n")
            choice = input("Enter a number 1-6: ")
            if choice == "1":
                #add student
                # Allow users to add new students and enter grades
                student = Student()
                self.students.append(student)
            elif choice == "2":
                #add grade
                student = self.pick_student()
                if student != None:
                    student.add_grade()
            # Include options to view individual student records and class summary
            elif choice == "3":
                student = self.pick_student()
                student.show_record()
            elif choice == "4":
                #show all students in class
                for i in self.students:
                    i.show_record()
            elif choice == "5":
                self.class_summary()
            elif choice == "6":
                break
# Include simple error handling for invalid menu choices
            else:
                print("must enter a valid number between 1-6")
                continue

grade = GradeBook()
grade.display_menu()








