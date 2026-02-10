import csv

def length_of_movie():
    # Use DictReader so we can use column names like 'Length (min)'
    try:
        # Get user input and convert to integers for comparison
        min_len = int(input("Minimum movie length (minutes): "))
        max_len = int(input("Maximum movie length (minutes): "))
        
        # Adjust the path to your actual file location
        path = "BG_CP2/individual_projects/Movies_list.csv"
        
        with open(path, mode="r", encoding="utf-8") as file:
            content = csv.DictReader(file)
            print(f"\nMovies between {min_len} and {max_len} minutes:")
            print("-" * 30)
            
            found = False
            for row in content:
                # Convert the CSV string value to an integer
                movie_length = int(row['Length (min)'])
                
                if min_len <= movie_length <= max_len:
                    print(f"- {row['Title']} ({movie_length} min)")
                    found = True
            
            if not found:
                print("No movies found in that range.")
    except FileNotFoundError:
        print("Error: Could not find 'Movies_list.csv'. Check your file path.")
    except ValueError:
        print("Please enter valid numbers for the lengths.")

def main():
    allowed = ["1", "2", "3", "4", "5", "6"]
    while True:
        print("\n--- Movie Finder ---")
        print("1-4: Search (Directors, Actors, Ratings, Genre)")
        print("5: Search by Length (Min/Max)")
        print("6: Exit")
        
        user = input("\nWhat do you want to do? ")
        
        if user == "6":
            print("Goodbye!")
            break
        elif user == "5":
            length_of_movie()
        elif user in ["1", "2", "3", "4"]:
            print("Search function coming soon!")
        else:
            print("Invalid input. Please enter a number 1-6.")

if __name__ == "__main__":
    main()

import csv

# 1. PARSER: Load and normalize data
def load_movies(filepath):
    movies = []
    try:
        with open(filepath, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Normalize: trim whitespace and handle multi-value fields
                record = {
                    "title": row["Title"].strip(),
                    "director": row["Director"].strip().lower(),
                    "genre": [g.strip().lower() for g in row["Genre"].replace('/', ',').split(',')],
                    "rating": row["Rating"].strip().upper(),
                    "length": int(row["Length (min)"]) if row["Length (min)"].isdigit() else 0,
                    "actors": [a.strip().lower() for a in row["Notable Actors"].split(',')]
                }
                movies.append(record)
    except FileNotFoundError:
        print(f"Error: The file at {filepath} was not found.")
    return movies

# 2. FILTER FUNCTIONS
def filter_by_text(movies, key, query):
    if not query: return movies
    query = query.lower().strip()
    # Check if query is in string (director) or in list (genre/actors)
    return [m for m in movies if any(query in item for item in (m[key] if isinstance(m[key], list) else [m[key]]))]

def filter_by_length(movies, min_len=None, max_len=None):
    filtered = movies
    if min_len is not None:
        filtered = [m for m in filtered if m["length"] >= min_len]
    if max_len is not None:
        filtered = [m for m in filtered if m["length"] <= max_len]
    return filtered

# 3. OUTPUT FUNCTIONS
def print_results(movie_list):
    if not movie_list:
        print("\n[!] No movies found matching those criteria. Try relaxing your filters.")
        return
    print(f"\n{'TITLE':<35} | {'GENRE':<20} | {'MIN':<5} | {'RATING'}")
    print("-" * 75)
    for m in movie_list:
        genres = ", ".join(m['genre']).title()
        print(f"{m['title']:<35} | {genres:<20} | {m['length']:<5} | {m['rating']}")

# 4. MAIN PROGRAM
def main():
    # Load data from the [Python CSV Module](https://docs.python.org)
    path = "Movies_list.csv" # Ensure this matches your filename
    all_movies = load_movies(path)
    
    if not all_movies:
        return

    while True:
        print("\n--- MOVIE SEARCH MENU ---")
        print("1. Search by Director")
        print("2. Search by Actor")
        print("3. Search by Genre")
        print("4. Search by Length Range")
        print("5. Show All Movies")
        print("6. Exit")
        
        choice = input("\nSelect an option: ")
        
        if choice == "6": break
        
        results = all_movies
        
        if choice == "1":
            query = input("Enter Director Name: ")
            results = filter_by_text(all_movies, "director", query)
        elif choice == "2":
            query = input("Enter Actor Name: ")
            results = filter_by_text(all_movies, "actors", query)
        elif choice == "3":
            query = input("Enter Genre: ")
            results = filter_by_text(all_movies, "genre", query)
        elif choice == "4":
            try:
                low = int(input("Min length (leave blank for 0): ") or 0)
                high = int(input("Max length (leave blank for 999): ") or 999)
                results = filter_by_length(all_movies, low, high)
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue
        elif choice == "5":
            results = all_movies
        else:
            print("Invalid selection.")
            continue

        print_results(results)

if __name__ == "__main__":
    main()
