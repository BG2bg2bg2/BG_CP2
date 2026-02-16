#BG 1st personal library

#main function of choice
def main():
    lists = []
    display = ("Author", "Title", "Genra", "Year", "Series")
    while True:
        #instructions
        print("\n1 to add\n2 to search\n3 to remove\n4 to show items\n5 clear\n6 to exit\n")
        #enter what you want to do
        enter = input("Choose a number 1-6: ")
        #if user wants to add
        if enter == "1":
            #call function adding as add
            add()
        #else if user wants to search
        elif enter == "2":
            #call funtion searching as search
            search()
        #else if user wants remove
        elif enter == "3":
            #call funtions removing as remove
            remove()
        #else if user wants to see what they have
        elif enter == "4":
            #call funtion showing list as show
            show()
        elif enter == "5":
            break
        #if user enters invalid choice 
        #display to them try again and enter a choice 1-5 only
        else:
            print("\nInvalid choice. Try again.\nEnter a chioce 1-5")
    #ask user what they want to add
    item = input("Enter an item that you want to add: ")
    #add that item to the library
    items.append(item)
    #update library
    return items
#funtion to seach items
def search():
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
def remove():
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
def show():
    #display every item in the library
    print(items)
#wipe the library funtion
def clear():
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