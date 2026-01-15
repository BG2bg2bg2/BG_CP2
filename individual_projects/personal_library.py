#BG 1st personal library

#list of items
items = []

#main function of choice
def main():
    while True:
        #instructions
        print("1 to add\n2 to search\n3 to remove\n4 to show items\n5 to exit")
        #enter what you want to do
        enter = input("Choose a number 1-5: ")
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
        #else if user wants to exit
        elif enter == "5":
            #dysplay goodbye exit
            break
        #if user enters invalid choice 
        # display to them
        #to try again
        else:
            print("Invalid choice. Try again")

#Funtion to add items in the list items
def add():
    #ask user what they want to add
    item = input("Enter an item that you want to add: ")
    items.append(item)
    return items
#funtion to seach items
def search():
    #ask user what item 
    #they want to seach for
    item = input("What item do you want to search for: ")
    if item in items:
        print("There are exactly ")
    else:
        print(f"The item {item} could not be found")
def remove():
    item = input("Enter an item you want to remove: ")
    if item in items:
        items.remove(item)
        return items
    else:
        print(f"Sorry the {item} could not be found")
def show():
    print(items)
main()