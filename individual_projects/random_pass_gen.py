#BG 1st
#use premade libraries
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
    #while loop is not stopped
    while True:
        #display 1 is the default of 8
        print("1 is the default of 8")
        #display 2 is the default of 10
        print("2 is the default of 10")
        #display 3 is the default of 20
        print("3 is the default of 20")
        #display 4 is to choose the length of password
        print("4 is to choose the length of password")
        #ask user to enter a number 1-4
        a = input("Enter a number 1-4: ")
        #if user enters 1
        if a == "1":
            #length is 8
            length = 8
            #call genorate function with length 8
            geno(length)
            #end loop
            break
        #else if user enters 2
        elif a == "2":
            #length is 10
            length = 10
            #call genorate function with length 10
            geno(length)
            #end loop
            break
        #else if user enters 3
        elif a == "3":
            #length is 20
            length = 20
            #call genorate function with length 20
            geno(length)
            #end loop
            break
        #else if user enters 4
        elif a == "4":
            #check for valid number was entered
            try:
                #ask user to enter a number for the length of password
                length = int(input("Enter a number for the length of the pass: "))
                #if length is less than 8
                if length < 8:
                    #display password must be at least 8 characters long
                    print("Password must be at least 8 characters long.")
                    #restart loop
                    continue
                #call genorate function with user inputed length
                geno(length)
                #end loop
                break
            #if user does not enter a valid number
            except ValueError:
                #display please enter a valid number
                print("Please enter a valid number.")
        #else 
        else:
            #display try again
            print("Try again but enter a number 1-4 this time")

#function to generate password based on what user wants
def geno(length):
    #ask user if password needs capital letters
    cap = input("Does the pass need capital letters? (Y/N): ").lower()
    #ask user if password needs lowercase letters
    low = input("Does the pass need lowercase letters? (Y/N): ").lower()
    #ask user if password needs special characters
    special = input("Does the pass need special characters? (Y/N): ").lower()
    #ask user if password needs numbers
    num = input("Does the pass need numbers? (Y/N): ").lower()
    #while loop is not stopped
    while True:
        #check user inputs for validity
        #if capitals are needed
        if cap == "y":
            #upercase is needed as true
            up = True
        #else if capitals are not needed
        elif cap == "n":
            #uppercase is not needed as false
            up = False
        #else
        else:
            #display try again
            print("Try again")
            #restart loop
            continue
        
        #if lowercase are needed
        if low == "y":
            #lowercase is needed as true
            lo = True
        #else if lowercase are not needed
        elif low == "n":
            #lowercase is not needed as false
            lo = False
        #else
        else:
            #display try again
            print("Try again")
            #restart loop
            continue
        #if special characters are needed
        if special == "y":
            #special characters is needed as true
            spe = True
        #else if special characters are not needed
        elif special == "n":
            #special characters is not needed as false
            spe = False
        #else
        else:
            #display try again
            print("Try again")
            #restart loop
            continue
        #if numbers are needed
        if num == "y":
            #numbers is needed as true
            n = True
        #else if numbers are not needed
        elif num == "n":
            #numbers is not needed as false
            n = False
        #else
        else:
            #display try again
            print("Try again")
            #restart loop
            continue

        #start the build password prosses based on what user wants
        char_set = ""
        #if up is needed as true
        if up:
            #add uppercase letters to char_set
            char_set += string.ascii_uppercase
        #if lo is needed as true
        if lo:
            #add lowercase letters to char_set
            char_set += string.ascii_lowercase
        #if spe is needed as true
        if spe:
            #add special characters to char_set
            char_set += string.punctuation
        #if n is needed as true
        if n:
            #add digits to char_set
            char_set += string.digits
        
        #generate password
        #if the password that the user wants are not met
        #regenerate the password
        if not char_set:
            #display no character types selected
            print("No character types selected. Please try again.")
            #restart loop
            continue
        
        #generate password and verify it meets what user wants
        password_valid = False
        #until password is valid stop
        while not password_valid:
            #generate a random password from char_set of given length
            password = ''.join(random.choice(char_set) for _ in range(length))
            
            #check if password contains what the user wants for the character types
            #check for uppercase letters if user wants it
            has_upper = any(c in string.ascii_uppercase for c in password) if up else True
            #check for lowercase letters if user wants it
            has_lower = any(c in string.ascii_lowercase for c in password) if lo else True
            #check for special characters if user wants it
            has_special = any(c in string.punctuation for c in password) if spe else True
            #check for numbers if user wants it
            has_number = any(c in string.digits for c in password) if n else True
            
            #check if all that the user wants are present and/or password is valid
            if has_upper and has_lower and has_special and has_number:
                #password valid is true
                password_valid = True
                #stops the loop/checks
        #for passwords 1-4
        for i in range(4):
            #generate a random password from char_set of given length
            password = ''.join(random.choice(char_set) for _ in range(length))
            #display generated password
            print(f"Generated password {i+1}: {password}")
        #end loop
        break
#call main funtion
main()
