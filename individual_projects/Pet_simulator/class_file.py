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