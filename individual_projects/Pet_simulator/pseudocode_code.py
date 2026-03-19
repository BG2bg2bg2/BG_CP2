#BG 1st Pet simulator

#class for money that you make
class Money():
    def __init__ (self, make, have, save, m_p_h_a):
        self.make = make
        self.m_p_h_a = m_p_h_a
        self.have = have
        self.save = save

    def cal(self):
        self.m_p_h_a = input(float("Enter how much money you make anualy"))
        self.make = self.m_p_h_a/10
        save += input(float(f"You have earned ${self.make} how much money do you want to save?: "))
#class for food types
class Food_types:
    def __init__(self, food_type, fcost):
                self.food_type = food_type.capitalize()
                self.cost = fcost

#class for pets that are availible
class Pets_for_sale:
    def __init__(self, species, age, pcost):
        self.secies = species.capitalize()
        self.age = age
        self.cost = pcost

    #funtion for buying a pet
    def store(self):
        self.pcost += self.age
        self.species += self.pcost

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
    def pet_interacitons():
        

#Include a method to check and display the pet's status

#

#Pet Interactions:
#Develop a system where each action (feeding, playing, sleeping) affects multiple attributes



#Implement a time system where each action advances time
##User Interface:
#Design a text-based menu for interacting with pets
#Allow users to create multiple pets and switch between them
#Include options to perform various actions with the selected pet
#Game Logic:
#Implement a health attribute that changes based on how well the pet is cared for
#Create events that occur randomly (e.g., pet gets sick, finds a toy)
#Add a leveling system where pets can learn new skills as they grow
#Data Management:
#Implement a simple save/load system to store pet data between sessions