#BG 1st

import random
all = []
length = 0
what = []
what1 = []
what2 = []
what3 = []
come = []
#funtion for main
def main():
    while True:
        #display welcome to the random password genorator
        print("Welcome to the random passward genorator\n")
        #display instructoins
        print("instructions\n")
        #display 1 is to genorate a password that is strong
        print("1 is to genorate a password that is strong and at least 8 characters long\n")
        #display 2 is to exit/quit
        print("2 is to exit/quit the program\n")
        #ask what number it will be 1 or 2
        choice = input("Enter a number 1 or 2: ")
        #if user enters 1
        if choice == "1":
            #call genorater
            gen()
        #else if user enters 2
        elif choice == "2":
            #end program
            break
        #else display try again
        else:
            print("Try again and this time enter 1 or 2\n")
#funtion for genorating passwords
def gen():
    while True:
        print("1 is the defalt of 8")
        print("2 is the defalt of 10")
        print("3 is the defalt of 20")
        print("4 is to choose the length of password")
        a = input("Enter a number 1-4 ")
        if a == "1":
            defalt()
        elif a == "2":
            ten()
        elif a == "3":
            twentey()
        elif a == "4":
            calling()
        else:
            print("Try again but enter a number 1-4 this time")
def defalt():
    
    length = 8
    
    cap = input("Does the pass require cappital letters? (Y/N): ").lower()
    low = input("Does the pass require lowercase letters? (Y/N): ").lower()
    special = input("Does the pass require special characters? (Y/N): ").lower()
    num = input("Does the pass require numbers? (Y/N): ").lower()
    
    while True:
        if cap == "y":
            up = True
        elif cap == "n":
            up = False
        else:
            print("Try again")

        if low == "y":
            lo = True
        elif low == "n":
            lo = False
        else:
            print("Try again")

        if special == "y":
            spe = True
        elif special == "n":
            spe = False
        else:
            print("try again")

        if num == "y":
            n = True
        elif num == "n":
            n == False
        else:
            print("Try again")

        come = [up, lo, spe, n]
        for _ in range(length):
            if random.come[lo, spe, up, n]:
                if up == True:
                    what.append(chr(random.randint(65, 90)))
                elif lo == True:
                    what1.append(chr(random.randint(97, 122)))
                elif spe == True:
                    what2.append(chr(random.randint(33,47)))
                elif n == True:
                    what3.append(chr(random.randint(48,57)))
        result = ''.join(what, what1, what2, what3)
        all = random.random(result, length)
        print(all)