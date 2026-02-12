#BG 1st update personal library

#libraries for importing/exporting csv data

#funtion for searching in csv file as "csvff()"
    #display "1 to add onto the csv file\n2 to clear and write on the csv file\n3 to read on the csv file\n4 to read and write on the csv file\n5 to go back to main menu"
    #user enters a number of what they want to do
    #if user entered 1
        #display and ask "You want to put/add something but it must be in a dictionary like form ex: name: Bob, color: red, fav_food: pancake"
        #call csvff() funtion
    #else if user entered 2

    #else if user entered 3
    #else if user entered 4
    #else if user entered 5
#funtion for searching in text file
#funtion for main



#BG 1st personal library

#funtion for list of items, sets of items, tuples of items

#main function of choice
def main():
    items = []
    sets = ("Title", "Author","writer", "song")

    while True:
        #instructions
        print("\n1 to add\n2 to search\n3 to remove\n4 to show items\n5 clear\n6 to exit\n")
        #enter what you want to do
        enter = input("Choose a number 1-6: ")
        #if user wants to add
        if enter == "1":
            #call function adding as add
            add(items, sets)
        #else if user wants to search
        elif enter == "2":
            #call funtion searching as search
            search(items, sets)
        #else if user wants remove
        elif enter == "3":
            #call funtions removing as remove
            removes(items, sets)
        #else if user wants to see what they have
        elif enter == "4":
            #call funtion showing list as show
            show(items, sets)
        elif enter == "5":
            clear(items)
        #else if user wants to exit
        elif enter == "6":
            #dysplay goodbye exit
            print("Goodbye")
            break
        #if user enters invalid choice 
        #display to them try again and enter a choice 1-5 only
        else:
            print("\nInvalid choice. Try again.\nEnter a chioce 1-5")

#Funtion to add items in the list items
def add(items, sets):
    print(sets)
    #ask user what they want to add
    item = input("Enter an item that you want to add: ")
    #add that item to the library
    items.append(item)
    #update library
    return items
#funtion to seach items
def search(items, sets):
    
    #ask user what item 
    #they want to seach for
    item = input("What item do you want to search for: ")
    #if the item is in the library with 2 or more items in it
    if items.count(item) >= 2:
        #count/search for the items
        a = items.count(item)
        #show how many items are serched
        print(f"There are exactly {a} items called {item}")
    #else if there is only one item in the library
    elif items.count(item) == 1:
        #count/search for that item
        a = items.count(item)
        #display there is exactly 1 item called what was searched
        print(f"There is exactly {a} item called {item}")
    #if there is no items wanted to be seached and counted
    else:
        #display no items are found with that name
        print(f"The item {item} could not be found")
#remove funtcion
def removes(items, sets):
    
    #ask what item they want to remove
    item = input("Enter an item you want to remove: ")
    #if the item is in the library
    if item in items:
        #remove that item
        items.remove(item)
        #display that item has been removed
        print(f"{item} has been removed")
        #updated library
        return items
    #if there is no items in the library
    else:
        #display no items called can't be found 
        print(f"Sorry the {item} could not be found")
#show the list library
def show(items, sets):
    
    #display every item in the library
    print(sets)
    print(items)
#wipe the library funtion
def clear(items):
    
    #clarify they want to wipe the library
    ask = input("Do you want to clear your library? y/n: ").lower()
    #approved to do it
    if ask == "yes" or "y":
        #items are cleared
        items.clear()
        #display success
        print("you have just cleared your library")
    #Not approved
    else:
        #display cancled
        print("Cancled")
    #Update items
    return items
#call all the funtions and main funtions
main()