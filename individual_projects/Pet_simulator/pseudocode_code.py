#BG 1st Pet simulator

from class_file import *



animal = [
    {"species": "dog", "food": "peas", "cost": 20},
    {"species":"cat", "food": "ham", "cost": 10},
    {"species": "bear", "food": "fish", "cost": 500},
    {"wolf", "lizard"}
        ]



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



food_type = {
    "species": f"{species}", "food type": f"{food_type}", "cost": f"{fcost}"
    }

pets = {
    "species": f"{species}", "age": f"{age}", "pcost": f"{pcost}"
}   

#Create a Pet class with attributes such as name, species, age, hunger, happiness, and energy


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
    while True:
        #1 to save progres and quit
        print("1 to save progress and quit")
        #2 to delete progres and quit
        print("2 to delete progress and quit")
        #3 to save progres and continue
        print("3 to save progress and continue")
        #4 to delete progres and contiue
        print("4 to delete progress/restart")
        #5 to continue game
        print("5 to continue playing")
        #display opions

        choice = input("What do you want to do? ")
        if choice == "1":
            break
        else:
            continue