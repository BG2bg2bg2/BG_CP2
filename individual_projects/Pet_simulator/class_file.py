#class for pets
class Anamals:
    def __init__(self, animal, age):
        self.animal = animal
        self.age = age
    
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

            
#class for the food types the anamals will need
class Food_types:
    def __init__(self, food_type, fcost):
                self.food_type = food_type.capitalize()
                self.cost = fcost
    def anamal_food(self):
        #dislpaly the type of anamal will need to eat type of food that costs x amount of money
        print(f"The anamal {self.species} will need to eat {self.food} that costs ${self.fcost}")

#class for pets that are availible
class Pets_for_sale:
    def __init__(self, species, age, pcost):
        self.secies = species.capitalize()
        self.age = age
        self.pcost = pcost

    #funtion for buying a pet
    def store(self):
        self.species = self.species
        self.pcost += self.age + self.species + self.pcost
    def pets(self):
        print(f"{self.species}, age: {self.age}, cost: ${self.pcost}")
#species = age + pcost

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
        pet_int = input("1 to feed\n2 to play\n3 to give water\n4 to take it on a walk\n5 to change pet")
        if pet_int == "1":
             #display you have x food
             print(f"You have {pfood}")
        pass

#Create a Pet class with attributes such as name, species, age, hunger, happiness, and energy