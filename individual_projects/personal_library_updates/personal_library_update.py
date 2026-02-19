#BG 1st update personal library
#import csv module
import csv

#set default field names for library items
FIELDNAMES = ["title", "creator", "year", "genre", "format", "rating", "notes"]


def load_library(path):
    #load items from csv file or create empty file if not exists
    #initialize empty items list
    items = []
    #attempt to open and read file
    try:
        #open the file for reading in utf-8 encoding
        with open(path, newline="", encoding="utf-8") as f:
            #create csv dictionary reader from file
            reader = csv.DictReader(f)
            #check if reader has no field names
            if not reader.fieldnames:
                #display warning message about missing header
                print(f"Warning: '{path}' has no header, using defaults.")
                #set field names to default
                reader.fieldnames = FIELDNAMES
            #loop through each row in reader starting from row 2
            for rownum, row in enumerate(reader, start=2):
                #create item dict with lowercase keys and stripped values
                item = {k.strip(): v.strip() for k, v in row.items() if k}
                #check if item has title and creator
                if not item.get("title") or not item.get("creator"):
                    #display warning for missing required fields
                    print(f"Warning: skipping malformed row {rownum} in {path}")
                    #skip this row and continue to next
                    continue
                #add item to items list
                items.append(item)
    #handle file not found error
    except FileNotFoundError:
        #create new file with header
        with open(path, "w", newline="", encoding="utf-8") as f:
            #create csv writer with fieldnames
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            #write header row
            writer.writeheader()
    #return list of items
    return items


def save_library(path, items):
    #save items list to csv file at path
    #open file for writing in utf-8 encoding
    with open(path, "w", newline="", encoding="utf-8") as f:
        #create csv writer with fieldnames
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        #write header row
        writer.writeheader()
        #loop through each item
        for item in items:
            #write item row to csv file
            writer.writerow({k: item.get(k, "") for k in FIELDNAMES})


def display_simple(items):
    #display title and creator for each item
    #check if items list is empty
    if not items:
        #display empty library message
        print("Library is empty.")
        #exit function
        return
    #loop through items with index starting at 1
    for idx, it in enumerate(items, 1):
        #print item number, title, and creator
        print(f"{idx}. {it.get('title','')} - {it.get('creator','')}")


def display_detailed(items):
    #display all details for each item
    #check if items list is empty
    if not items:
        #display empty library message
        print("Library is empty.")
        #exit function
        return
    #loop through items with index starting at 1
    for idx, it in enumerate(items, 1):
        #print item number
        print(f"{idx}.")
        #loop through each field in fieldnames
        for field in FIELDNAMES:
            #print field name and value
            print(f"   {field.title()}: {it.get(field,'')}")
        #print blank line for readability
        print()


def input_nonempty(prompt):
    #keep prompting until user enters non-empty input
    #loop forever until return
    while True:
        #get user input and strip whitespace
        val = input(prompt).strip()
        #check if input is not empty
        if val:
            #return the non-empty value
            return val
        #display error message for empty input
        print("Input cannot be empty.")


def add_item(items):
    #display instructions for adding new item
    print("Adding new item. Leave optional fields blank.")
    #create empty dictionary for new item
    new = {}
    #prompt for title until non-empty
    new["title"] = input_nonempty("Title: ")
    #prompt for creator until non-empty
    new["creator"] = input_nonempty("Creator (author/artist/director): ")
    #prompt for year and strip whitespace
    new["year"] = input("Year: ").strip()
    #prompt for genre and strip whitespace
    new["genre"] = input("Genre: ").strip()
    #prompt for format and strip whitespace
    new["format"] = input("Format: ").strip()
    #prompt for rating and strip whitespace
    new["rating"] = input("Rating: ").strip()
    #prompt for notes and strip whitespace
    new["notes"] = input("Notes: ").strip()
    #add new item to items list
    items.append(new)
    #display confirmation message
    print("Item added.")


def choose_index(items, action):
    #prompt user to choose item index for action
    #check if items list is empty
    if not items:
        #display empty library message
        print("Library is empty.")
        #return none for cancelled
        return None
    #display simple list of items
    display_simple(items)
    #loop forever until valid selection
    while True:
        #prompt user for item number
        resp = input(f"Enter the number of the item to {action} (or 'c' to cancel): ").strip()
        #check if user entered cancel
        if resp.lower() == 'c':
            #return none for cancelled
            return None
        #check if response is a digit
        if not resp.isdigit():
            #display error for invalid input
            print("Please enter a valid number.")
            #continue loop
            continue
        #convert response to 0-based index
        i = int(resp) - 1
        #check if index is in valid range
        if 0 <= i < len(items):
            #return valid index
            return i
        #display error for out of range
        print("Number out of range.")


def update_item(items):
    #get index of item to update
    idx = choose_index(items, "update")
    #check if user cancelled
    if idx is None:
        #exit function
        return
    #get item at chosen index
    item = items[idx]
    #display instruction to user
    print("Press Enter to keep current value.")
    #loop through each field in fieldnames
    for field in FIELDNAMES:
        #get current value of field
        current = item.get(field, "")
        #prompt user for new value
        new = input(f"{field.title()} [{current}]: ").strip()
        #check if user entered new value
        if new:
            #update field with new value
            item[field] = new
    #display confirmation message
    print("Item updated.")


def delete_item(items):
    #get index of item to delete
    idx = choose_index(items, "delete")
    #check if user cancelled
    if idx is None:
        #exit function
        return
    #remove and store item at index
    removed = items.pop(idx)
    #display confirmation with removed item title
    print(f"Removed '{removed.get('title','')}'.")


def main():
    #set file path to personal library update csv
    path = "individual_projects/personal_library_updates/personal_library_update.csv"
    #load library from file
    library = load_library(path)
    #initialize changed flag as false
    changed = False
    #create menu string with all options
    menu = (
        "\nMain menu:\n"
        "1 Show simple list\n"
        "2 Show detailed list\n"
        "3 Add item\n"
        "4 Update item\n"
        "5 Delete item\n"
        "6 Save library\n"
        "7 Reload library from file\n"
        "8 Exit\n"
    )
    #main loop that runs until user exits
    while True:
        #display menu to user
        print(menu)
        #get user choice
        choice = input("Choose an action: ").strip()
        #check if user chose show simple list
        if choice == '1':
            #display simple view of library
            display_simple(library)
        #check if user chose show detailed list
        elif choice == '2':
            #display detailed view of library
            display_detailed(library)
        #check if user chose add item
        elif choice == '3':
            #call add item function
            add_item(library)
            #mark library as changed
            changed = True
        #check if user chose update item
        elif choice == '4':
            #call update item function
            update_item(library)
            #mark library as changed
        elif choice == '6':
            #save library to file
            save_library(path, library)
            #display success message
            print("Library saved.")
            #mark library as not changed
            changed = False
        #check if user chose reload library
        elif choice == '7':
            #check if library has unsaved changes
            if changed:
                #warn user about losing changes
                ans = input("Unsaved changes will be lost. Continue? (y/n): ").strip().lower()
                #check if user said no
                if ans != 'y':
                    #go back to main menu
                    continue
            #load library from file
            library = load_library(path)
            #mark library as not changed
            changed = False
            #display success message
            print("Library reloaded.")
        #check if user chose exit
        elif choice == '8':
            #check if library has unsaved changes
            if changed:
                #prompt user to save before exiting
                ans = input("You have unsaved changes. Save before exiting? (y/n): ").strip().lower()
                #check if user said yes
                if ans == 'y':
                    #save library to file
                    save_library(path, library)
                    #display success message
                    print("Saved.")
            #display goodbye message
            print("Goodbye!")
            #break out of main loop
            break
        #user entered invalid choice
        else:
            #display error message
            print("Invalid selection, please enter 1-8.")

#call main function
main()
