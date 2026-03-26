#BG 1st Pet simulator

from class_file import *



animal = [
    {"species": "dog", "food type": "peas", "food type cost": .5, "pet cost": 20, "age": 2},
    {"species": "cat", "food type": "ham", "food type cost": .8, "pet cost": 10, "age": 2},
    {"species": "bear", "food type": "fish", "food type cost": .7, "pet cost": 500, "age": 2},
]





while True:
    try:
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
        break
    except:
        print("Must enter a number")





#Include a method to check and display the pet's status
def pet_stats():
    for pet in animal:
    pets = {
        "species": pet["species"],
        "age": pet["age"],
        "pet food cost": pet["food type cost"]
    }
    print(pets)
#

#Pet Interactions:
#Develop a system where each action (feeding, playing, sleeping) affects multiple attributes


#Class Implementation:


#Create a Pet class with attributes such as name, species, age, hunger, happiness, and energy


#Implement methods for feeding, playing, and putting the pet to sleep


#Include a method to check and display the pet's status


#Pet Interactions:


#Develop a system where each action (feeding, playing, sleeping) affects multiple attributes


#Implement a time system where each action advances time


#Create different food types that affect hunger and happiness differently


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