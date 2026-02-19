#bg 1st book recommendations program
#needed libraries
import csv


#function to load and normalize book data from csv file
def load_books(filepath):  
    #load and normalize book data from csv file. args: filepath (str): path to csv file. returns: list: list of dictionaries with normalized book data. raises: filenotfounderror: if csv file doesn't exist. valueerror: if csv is malformed
    
    #initialize books list
    books = []
    
    try:
        with open(filepath, mode="r", encoding="utf-8") as f:
            pass
    #if file cant be found
    except FileNotFoundError:
        #display book list file not found
        raise FileNotFoundError(f"book list file not found: {filepath}")
    
    try:
        with open(filepath, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            if not reader.fieldnames:
                raise ValueError("CSV file is empty or malformed")
            
            #iterate through csv rows
            for row_num, row in enumerate(reader, start=2):
                #check if title exists
                if not row.get('Title'):
                    print(f"Warning: Skipping empty row {row_num}")
                    continue
                #normalize the book record
                normalized_book = {
                    'Title': row.get('Title', '').strip(),
                    'editor': row.get('editor', '').strip(),
                    'Genre': row.get('Genre', '').strip(),
                    'cost': row.get('cost', '').strip(),
                    'authors': row.get('authors', '').strip(),
                }
                books.append(normalized_book)
    
    except ValueError as e:
        raise ValueError(f"Error parsing CSV file: {e}")
    
    return books


def filter_by_genre(books, genre_query):
    #filter books by genre (case-insensitive substring match). args: books (list): list of book dictionaries. genre_query (str): genre to search for. returns: list: filtered books matching the genre
    
    if not genre_query or genre_query.lower() == 'skip':
        return books
    
    query = genre_query.strip().lower()
    return [m for m in books if query in m['Genre'].lower()]


def filter_by_editor(books, editor_query):
    #filter books by editor (case-insensitive substring match). args: books (list): list of book dictionaries. editor_query (str): editor name to search for. returns: list: filtered books matching the editor
    
    if not editor_query or editor_query.lower() == 'skip':
        return books
    
    query = editor_query.strip().lower()
    return [m for m in books if query in m['editor'].lower()]


def filter_by_author(books, author_query):
    #filter books by author name (case-insensitive substring match). args: books (list): list of book dictionaries. author_query (str): author name to search for. returns: list: filtered books matching the author
    
    if not author_query or author_query.lower() == 'skip':
        return books
    
    query = author_query.strip().lower()
    return [m for m in books if query in m['Notable authors'].lower()]


def filter_by_cost(books, cost_query):
    #filter books by cost (case-insensitive exact match). args: books (list): list of book dictionaries. cost_query (str): cost to search for (e.g., 'pg', 'r', 'pg-13'). returns: list: filtered books matching the cost
    
    if not cost_query or cost_query.lower() == 'skip':
        return books
    
    query = cost_query.strip().upper()
    return [m for m in books if m['cost'].upper() == query]




def apply_filters(books, genre=None, editor=None, author=None, cost=None):
    #apply multiple filters using and logic (all filters must match). args: books (list): list of book dictionaries. genre (str): genre filter (optional). editor (str): editor filter (optional). author (str): author filter (optional). cost (str): cost filter (optional). filter (optional). returns: tuple: (filtered_books, applied_filters_count)
    
    #start with all books
    result = books
    #count of filters applied
    filters_applied = 0
    
    #apply genre filter if provided
    if genre:
        result = filter_by_genre(result, genre)
        #increment filter count
        filters_applied += 1
    
    #apply editor filter if provided
    if editor:
        result = filter_by_editor(result, editor)
        #increment filter count
        filters_applied += 1
    
    #apply author filter if provided
    if author:
        result = filter_by_author(result, author)
        #increment filter count
        filters_applied += 1
    
    #apply cost filter if provided
    if cost:
        result = filter_by_cost(result, cost)
        #increment filter count
        filters_applied += 1
    
    #return filtered books and count
    return result, filters_applied



def pretty_print_books(books, title=""):
    #pretty-print a list of books in tabular format. args: books (list): list of book dictionaries to display. title (str): optional title for the display
    
    #check if books list is empty
    if not books:
        print("No books found.")
        return
    
    #display title if provided
    if title:
        print(title)
    
    #display book count
    print(f"Found {len(books)} book(s):\n")
    
    #iterate through each book
    for i, book in enumerate(books, 1):
        #display book title
        print(f"{i}. {book['Title']}")
        #display editor
        print(f"   editor: {book['editor']}")
        #display genre
        print(f"   Genre: {book['Genre']}")
        #display cost
        print(f"   cost: {book['cost']}")
        #display authors
        print(f"   Notable authors: {book['Notable authors']}")
        #blank line for readability
        print()


def print_full_list(books):
    #display all books in the database. args: books (list): list of all books
    
    #call pretty print with all books
    pretty_print_books(books, "COMPLETE book DATABASE")


def print_welcome():
    #display welcome message and options
    #display menu options
    print("Hi, and welcome to book Recommendations!\n1 to search by editor\n2 to search by author\n3 to search by cost\n4 to search by genre\n5 for custom multi-filter search\n6 to show all books\n7 to exit")


def search_editor(books):
    #interactive editor search.
    #get editor input
    editor = input("Enter editor name (or 'skip' to skip): ").strip()
    #check if user wants to skip
    if editor.lower() == 'skip':
        #return unchanged books list
        return books
    
    #filter by editor
    results = filter_by_editor(books, editor)
    #if results found
    if results:
        #display results
        pretty_print_books(results, f"books directed by: {editor}")
    #if no results found
    else:
        #display no results message
        print(f"\nNo books found by editor '{editor}'.")
        #provide suggestion
        print("Try a shorter name or check the spelling.")
    
    #return filtered results
    return results


def search_author(books):
    #interactive author search.
    #get author input
    author = input("Enter author name (or 'skip' to skip): ").strip()
    #check if user wants to skip
    if author.lower() == 'skip':
        #return unchanged books list
        return books
    
    #filter by author
    results = filter_by_author(books, author)
    #if results found
    if results:
        #display results
        pretty_print_books(results, f"books with author(s): {author}")
    #if no results found
    else:
        #display no results message
        print(f"\nNo books found with author '{author}'.")
        #provide suggestion
        print("Try a shorter name or check the spelling.")
    
    #return filtered results
    return results


def search_cost(books):
    #interactive cost search.
    #display valid costs
    print("Valid costs: G, PG, PG-13, R, Not Rated")
    #get cost input
    cost = input("Enter cost (or 'skip' to skip): ").strip()
    #check if user wants to skip
    if cost.lower() == 'skip':
        #return unchanged books list
        return books
    
    #filter by cost
    results = filter_by_cost(books, cost)
    #if results found
    if results:
        #display results
        pretty_print_books(results, f"books with cost: {cost}")
    #if no results found
    else:
        #display no results message
        print(f"\nNo books found with cost '{cost}'.")
    
    #return filtered results
    return results

#funtiong for searching genre in the books list
def search_genre(books):
    #interactive genre search.
    #get genre input
    genre = input("Enter genre (Drama, Action, Comedy, etc., or 'skip' to skip): ").strip()
    #check if user wants to skip
    if genre.lower() == 'skip':
        #return unchanged books list
        return books
    
    #filter by genre
    results = filter_by_genre(books, genre)
    #if results found
    if results:
        #display results
        pretty_print_books(results, f"books in genre: {genre}")
    #if no results found
    else:
        #display no results message
        print(f"\nNo books found in genre '{genre}'.")
        #provide suggestion
        print("Try related genres or check the spelling.")
    
    #return filtered results
    return results

def update(books):
    #funtion for updating books
    #ask user what they want to update
    while True:
        book_update = input("What do you want to update 1 to add a book, 2 to update cost, 3 to delete book, 4 to save library.")
        if book_update == "1":
            title = input("Enter the title of the book")
            author = input("Enter the writer of the book")
            editor = input("Enter the editor of the book")
            add_published_date = input("Enter the year of the book it was first published")
            cost = float(input("Enter how much the book cost $"))
            stock = int("Enter how many books are in stock")
            return books.append(author,cost,editor, stock, title, add_published_date)
def custom_search(books):
    #interactive custom multi-filter search.
    #display instructions
    print("\nCombine multiple filters (all filters must match).\n")
    #get title input
    title = input("Title (or press enter to skip): ").strip() or None
    #get genre input
    genre = input("Genre (or press enter to skip): ").strip() or None
    #get editor input
    editor = input("editor (or press enter to skip): ").strip() or None
    #get author input
    author = input("author (or press enter to skip): ").strip() or None
    #get cost input
    cost = input("cost (or press enter to skip): ").strip() or None

    
    #apply all filters with and logic
    results, filters_count = apply_filters(
        books,
        title=title,
        genre=genre,
        editor=editor,
        author=author,
        cost=cost
    )
    
    #initialize filter summary
    filter_summary = []
    #if title was provided
    if title:
        #add to summary
        filter_summary.append(f"genre '{genre}'")
    #if genre was provided
    if genre:
        #add to summary
        filter_summary.append(f"genre '{genre}'")
    #if editor was provided
    if editor:
        #add to summary
        filter_summary.append(f"editor '{editor}'")
    #if author was provided
    if author:
        #add to summary
        filter_summary.append(f"author '{author}'")
    #if cost was provided
    if cost:
        #add to summary
        filter_summary.append(f"cost '${cost}'")
    
    #if results found
    if results:
        #create title from filters
        title = f"books matching: {', '.join(filter_summary)}"
        #display results
        pretty_print_books(results, title)
    #if no results found
    else:
        #display no results message
        print(f"\nNo books match your criteria.")
        #if filters were applied
        if filter_summary:
            #show attempted filters
            print(f"Tried filtering by: {', '.join(filter_summary)}")
        #provide suggestion
        print("Try relaxing one or more filters.")
    #return filtered results
    return results
#main function that runs the program with persistent menu.
def main():
    #get the csv file path
    csv_path = "BG_CP2/individual_projects/personal_library_updates/personal_library_update.csv"
    
    #try to load books
    try:
        #load books from csv file
        books = load_books(csv_path)
        #display count of loaded books
        print(f"Found {len(books)} recommended books!")
    #if file not found or csv error
    except (FileNotFoundError, ValueError) as e:
        #display error message
        print(f"ERROR: {e}")
        #exit program
        return
    #main menu loop
    while True:
        #display welcome menu
        print_welcome()
        #get choice
        choice = input("What would you like to do? (Enter 1-7): ").strip()
        #search by editor
        if choice == "1":
            #call editor search
            search_editor(books)
        #search by author
        elif choice == "2":
            #call author search
            search_author(books)
        #search by cost
        elif choice == "3":
            #call cost search
            search_cost(books)
        #search by genre
        elif choice == "4":
            #call genre search
            search_genre(books)
        #custom multi-filter search
        elif choice == "5":
            #call custom search
            custom_search(books)
        #show all books
        elif choice == "6":
            #display all books
            print_full_list(books)
        #update book folder
        elif choice == "7":
            #call update books
            update(books)
        #exit program
        elif choice == "":
            #goodbye message
            print("\nThank you for using book Recommendations. Goodbye!")
            #exit loop
            break
        #invalid choice
        else:
            #error message
            print("Invalid choice. Please enter a number between 1 and 7.\n")
        
        #wait for user before showing menu again
        input("Press Enter to continue...")  


#start/run/call main function
main()