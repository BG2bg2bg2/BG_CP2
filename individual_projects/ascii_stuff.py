#ascii stuff
#use random library
import random

#main funtion
def main():
    #while loop until false
    while True:
        #display welcome to the random password generator
        print("\nWelcome to the random password generator")
        #display 1 to generat password 
        print("1 to Generate password")
        #display 2 to quit
        print("2 to Quit")

        #ask what they want to put
        choice = input("Enter 1 or 2: ")

        #if user enter 1
        if choice == "1":
            #call password generator (gen)
            gen()
        
        #else if user enter 2
        elif choice == "2":
            #end program as break
            break
        #else
        else:
            #display invealid choice
            print("Invalid choice")
#genorater funtion (gen)
def gen():
    #display password length option
    print("\nPassword length options:")
    #display enter 1 for 8 character long pass
    print("enter 1 for 8 characters long pass")
    #display enter 2 for 10 characters long pass
    print("enter 2 for 10 characters long pass")
    #display enter 3 for 20 characters long pass
    print("enter 3 for 20 characters long pass")
    #disply enter 4 for Custom length for the pass
    print("enter 4 for Custom length for the pass")

    #user enters a number of their choice
    choice = input("Enter 1-4: ")

    #if user entered 1
    if choice == "1":
        #length for pass is 8
        length = 8
    #else if user entered 2
    elif choice == "2":
        #length for pass is 10
        length = 10
    #else if user entered 3
    elif choice == "3":
        #length for pass is 20
        length = 20
    #else if user enterd 4
    elif choice == "4":
        #length for pass is what the number the user inputs
        length = int(input("Enter password length: "))
    #else
    else:
        #display invalid choice
        print("Invalid choice")
        #return/update the length for pass
        return
    #call generate password for length
    generate_password(length)

# genterate password with length of pass
def generate_password(length):
    #ask if pass needs uppercase yes or no
    use_upper = input("Capital letters? (y/n): ").lower() == "y"
    #ask if pass needs lowercase yes or no
    use_lower = input("Lowercase letters? (y/n): ").lower() == "y"
    #ask if pass needs numbers yes or no
    use_numbers = input("Numbers? (y/n): ").lower() == "y"
    #ask if pass needs special characters yes or no
    use_special = input("Special characters? (y/n): ").lower() == "y"

    #if user does not use any characters
    if not (use_upper or use_lower or use_numbers or use_special):
        #display You must choose at least one character type.
        print("You must choose at least one character type.")
        #return/update character types for password
        return
    
    #make password
    password = []
    #for length for pass in number they want
    for _ in range(length):
        #randomize character types
        choice = random.choice(["upper", "lower", "num", "special"])
        
        #if user wants uppercase 
        if choice == "upper" and use_upper:
            #add randomized uppercase to pass
            password.append(chr(random.randint(65, 90)))
        #else if user wants lowercase
        elif choice == "lower" and use_lower:
            #add randomized lowercase to pass
            password.append(chr(random.randint(97, 122)))
        #else if user wants numbers
        elif choice == "num" and use_numbers:
            #add randomized numbers to pass
            password.append(chr(random.randint(48, 57)))
        #else if user wants special characters
        elif choice == "special" and use_special:
            #add special cahracters to pass
            password.append(chr(random.randint(33, 47)))
        #else
        else:
            # retry if that type wasn't allowed
            password.append(chr(random.randint(97, 122)))

    #if password does not have the wanted types
    #if password == ["upper", "lower", 'num', 'special']
        #print(password)
    #else if password does not have any of the wanted items
    #regenorate
    print("\nGenerated password:", ''.join(password))

main()
