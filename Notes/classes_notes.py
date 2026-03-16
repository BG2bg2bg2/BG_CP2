#BG 1st csp 2 classes notes

#example 1
class Animal:
    #1
    def __init__(self,name, species, age):
        self.name = name.capitalize()
        self.species = species.capitalize()
        self.age = age
    #2
    def __str__(self):
        return(f"\n\nName:{self.name}\nspecies:{self.species}\nage:{self.age}")
    #3
    def birthday(self):
        self.age += 1

dog = Animal('Doug', "dog", 4)
bunny = Animal("Judy", "Rabit", 20)
#1
print(f"""\n\nName = {dog.name}
species = {dog.species}
age = {dog.age}""")

#2
print(bunny)

#3
dog.birthday()
print(dog)

# Example 2
class Classperiod:
    def __init__(self, subject, teacher = "Ms. LaRose", room = None):
        self.subject = subject.capitalize()
        self.teacher = teacher
        self.room = room
    
    def __str__(self):
        return f"Subject: {self.subject}\nTeacher: {self.teacher}\nRoom: {self.room}"

first = Classperiod("Computer Programing 2", room = 200)
second = Classperiod("Computer Programing 2", room = 200)
third = Classperiod("Computer Science Principles", room = 200)
sixth = Classperiod("English 8", "Miss Jensen", 216)
print(first, second, third, sixth)