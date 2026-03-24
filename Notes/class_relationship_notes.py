#BG 1st class relationship notes CSP2


#What is polymorphism?

#What is inheritance? 

#parent class
class Vehical:
    def __init__(self, model, brand):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Move!")

#child class
class Car(Vehical):
    pass

class Plane(Vehical):
    def move(self):
        print("Fly!")

class Boat(Vehical):
    def move(self):
        print("Sail!")

car = Car("Ford", "Mustang")
boat = Boat("Ibiza", "Toruing 20")
plane = Plane("Boeing", "747")

print(boat.brand)
print(boat.model)
print(car.brand)
print(car.model)
car.move()
boat.move()
plane.move()
#What do we call the classes in an inheritance relationship?

#parent child

#How does inheritance simplify your code?

#What is aggregation? 

#How do you use aggregation?

#How does aggregation simplify your code?

#What is composition?

#How do you use composition?

#How does composition simplify your code?








#Agergation "Has A"
class Library:
    def __init__(self, name, catalog = []):
        self.name = name
        self.catalog = catalog
    
    def add_book(self, book):
        self.catalog.append(book)
    
    def remove_book(self, book):
        if book in self.catalog:
            self.catalog.pop(book)
        else:
            print("That book isn't in this library")
    
    def view_catalog(self):
        for book in self.catalog:
            print(book)

class Book:
    def __init__(self, title, author):
        self.title = title.title()
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}"
lib = Library("Provo Library")
lib.add_book(Book("Way of Kings", "Brandon Sanderson"))
lib.add_book(Book("Steel Heart", "Brandon Sanderson"))
lib.add_book(Book("Alcatraz", "Brandon Sanderson"))

lib.view_catalog()

#composition "Has a" relationship
