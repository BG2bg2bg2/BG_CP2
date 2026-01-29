#BG 1st

import random
import string
#function for main
def main():
    while True:
        #display welcome to the random password generator
        print("Welcome to the random password generator\n")
        #display instructions
        print("instructions\n")
        #display 1 is to generate a password that is strong
        print("1 is to generate a password that is strong and at least 8 characters long\n")
        #display 2 is to exit/quit
        print("2 is to exit/quit the program\n")
        #ask what number it will be 1 or 2
        choice = input("Enter a number 1 or 2: ")
        #if user enters 1
        if choice == "1":
            #call generator
            gen()
        #else if user enters 2
        elif choice == "2":
            #end program
            break
        #else display try again
        else:
            print("Try again and this time enter 1 or 2\n")
#function for generating passwords
def gen():
    while True:
        print("1 is the default of 8")
        print("2 is the default of 10")
        print("3 is the default of 20")
        print("4 is to choose the length of password")
        a = input("Enter a number 1-4: ")
        if a == "1":
            length = 8
            geno(length)
            break
        elif a == "2":
            length = 10
            geno(length)
            break
        elif a == "3":
            length = 20
            geno(length)
            break
        elif a == "4":
            try:
                length = int(input("Enter a number for the length of the pass: "))
                geno(length)
                break
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Try again but enter a number 1-4 this time")
def geno(length):
    
    cap = input("Does the pass require capital letters? (Y/N): ").lower()
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
            continue

        if low == "y":
            lo = True
        elif low == "n":
            lo = False
        else:
            print("Try again")
            continue

        if special == "y":
            spe = True
        elif special == "n":
            spe = False
        else:
            print("Try again")
            continue

        if num == "y":
            n = True
        elif num == "n":
            n = False
        else:
            print("Try again")
            continue

        # Build character set based on requirements
        char_set = ""
        if up:
            char_set += string.ascii_uppercase
        if lo:
            char_set += string.ascii_lowercase
        if spe:
            char_set += string.punctuation
        if n:
            char_set += string.digits
        
        # Generate password
        #if password requirements are not met
        #regenerate the password
        if not char_set:
            print("No character types selected. Please try again.")
            continue
        
        # Generate password and verify it meets requirements
        password_valid = False
        while not password_valid:
            password = ''.join(random.choice(char_set) for _ in range(length))
            
            # Check if password contains required character types
            has_upper = any(c in string.ascii_uppercase for c in password) if up else True
            has_lower = any(c in string.ascii_lowercase for c in password) if lo else True
            has_special = any(c in string.punctuation for c in password) if spe else True
            has_number = any(c in string.digits for c in password) if n else True
            
            # If all required types are present, password is valid
            if has_upper and has_lower and has_special and has_number:
                password_valid = True
        
        print(f"Generated password: {password}")
        break
main()
