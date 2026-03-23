#BG 1st Pet simulator

#class for pets
class Anamals:
    def __init__(self, animal, age):
        self.animal = animal
        self.age = age

animal = ["dog", "cat", "bear", "wolf", "lizard"]

#class for money that you make
class Money():
    def __init__ (self, m_p_h, have, saved):
        self.m_p_h = m_p_h
        self.make = m_p_h*0.9
        self.have = have
        self.saved = saved
    #function for how much you have
    def keep(self):
        #display how much you earned, made with tax, saved with what you want to save
        print(f"You make ${self.m_p_h} per hour, after tax you earn ${self.make} and you have ${self.have}, and you saved {self.saved}")
#ask how much user makes an hour
m_p_h = float(input("Enter how much you make an hour: "))
#tax the answer
make = m_p_h*0.9
#ask how much they want to save
saves = float(input(f"You have earned {make} how much do you want to save: "))
#have the outcome with how much you curently have
have = make - saves
#how much you saved
saved = make - have
#call the curent amount of money
money = Money(m_p_h, saved, have)
money.keep()




#class for the food types the anamals will need
class Food_types:
    def __init__(self, food_type, fcost):
                self.food_type = food_type.capitalize()
                self.cost = fcost
    def anamal_food(self):
        #dislpaly the type of anamal will need to eat type of food that costs x amount of money
        print(f"The anamal {self.species} will need to eat {self.food} that costs ${self.fcost}")

food_type = {
    "species": f"{species}", "food type": f"{food_type}", "cost": f"{fcost}"
    }

#species = age  pcost

#class for pets that are availible
class Pets_for_sale:
    def __init__(self, species, age, pcost):
        self.secies = species.capitalize()
        self.age = age
        self.pcost = pcost

    #funtion for buying a pet
    def store(self):
        self.pcost += self.age
        self.species += self.pcost
    def pets(self):
        print(f"{self.species}, age: {self.age}, cost: ${self.pcost}")
pets = {
    "species": f"{species}", "age": f"{age}", "pcost": f"{pcost}"
}   

#Create a Pet class with attributes such as name, species, age, hunger, happiness, and energy

#class for pets that you own
class Pets_owned:
    #function for the pets you own
    def __init__(self, name, species, age, food_type, hunger, happiness, energy, thirst):
        self.name = name.capitalize()
        self.species = species.capitalize()
        self.age = age
        self.food_type = food_type.capitalize()
        self.hunger = hunger
        self.happiness = happiness
        self.engergy = energy
        self.thirst = thirst

        #Implement methods for feeding, playing, and putting the pet to sleep
        #functin for interaction with pet
    def pet_interacitons(self):
        pass


#Include a method to check and display the pet's status

#

#Pet Interactions:
#Develop a system where each action (feeding, playing, sleeping) affects multiple attributes


#do I have all requirements met?
#Implement a time system where each action advances time
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

def save_sim():
    pass
    #1 to save progres and quit
    #2 to delete progres and quit
    #3 to save progres and continue
    #4 to delete progres and contiue
    #5 to continue game
    #display opions
