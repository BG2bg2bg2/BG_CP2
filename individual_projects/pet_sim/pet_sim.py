
#Class Implementation:


#Create a Pet class with attributes such as name, species, age, hunger, happiness, and energy
class Pet:
    def __init__(self, name, species, age, hunger, happiness, energy):
        self.name = name
        self.species = species
        self.age = age
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy

name = input("enter a name for your pet")
speices = input("enter a species for your pet")

def main():
    welcome()
    choose()
#Implement methods for feeding, playing, and putting the pet to sleep
#Include a method to check and display the pet's status
print(Pet)
#Pet Interactions:
#Develop a system where each action (feeding, playing, sleeping) affects multiple attributes
def feed():
    pass
def play():
    pass
def sleep():
    pass
#Implement a time system where each action advances time
#Create different food types that affect hunger and happiness differently
def store():
    pass
#User Interface:
#Design a text-based menu for interacting with pets
#Allow users to create multiple pets and switch between them

#Include options to perform various actions with the selected pet
#Game Logic:
#Implement a health attribute that changes based on how well the pet is cared for
#Create events that occur randomly (e.g., pet gets sick, finds a toy)
#Add a leveling system where pets can learn new skills as they grow
#Data Management:
#Implement a simple save/load system to store pet data between sessions

#class Save:
#   print("How do you want to save")
def welcome():
    print("Welcome Lets make pet")
    choose()

def choose():
    while True:
        print(f"1 to feed {Pet[name]}\n2 to play with {Pet[name]}\n3 to make pet sleep\n4 to do something else")
        enter = input("What do you want to do")
        if enter == "1":
            feed()
        elif enter == "2":
            play()
        elif enter == "3":
            sleep()
        elif enter == "4":
            main()
        else:
            continue