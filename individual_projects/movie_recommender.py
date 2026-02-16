#bg 1st movie recommendations program
#needed libraries
import csv


#function to load and normalize movie data from csv file
def load_movies(filepath):  
    #load and normalize movie data from csv file. args: filepath (str): path to csv file. returns: list: list of dictionaries with normalized movie data. raises: filenotfounderror: if csv file doesn't exist. valueerror: if csv is malformed
    
    #initialize movies list
    movies = []
    
    try:
        with open(filepath, mode="r", encoding="utf-8") as f:
            pass
    #if file cant be found
    except FileNotFoundError:
        #display movie list file not found
        raise FileNotFoundError(f"Movie list file not found: {filepath}")
    
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
                #normalize the movie record
                normalized_movie = {
                    'Title': row.get('Title', '').strip(),
                    'Director': row.get('Director', '').strip(),
                    'Genre': row.get('Genre', '').strip(),
                    'Rating': row.get('Rating', '').strip(),
                    'Length (min)': row.get('Length (min)', '').strip(),
                    'Notable Actors': row.get('Notable Actors', '').strip(),
                }
                movies.append(normalized_movie)
    
    except ValueError as e:
        raise ValueError(f"Error parsing CSV file: {e}")
    
    return movies


def filter_by_genre(movies, genre_query):
    #filter movies by genre (case-insensitive substring match). args: movies (list): list of movie dictionaries. genre_query (str): genre to search for. returns: list: filtered movies matching the genre
    
    if not genre_query or genre_query.lower() == 'skip':
        return movies
    
    query = genre_query.strip().lower()
    return [m for m in movies if query in m['Genre'].lower()]


def filter_by_director(movies, director_query):
    #filter movies by director (case-insensitive substring match). args: movies (list): list of movie dictionaries. director_query (str): director name to search for. returns: list: filtered movies matching the director
    
    if not director_query or director_query.lower() == 'skip':
        return movies
    
    query = director_query.strip().lower()
    return [m for m in movies if query in m['Director'].lower()]


def filter_by_actor(movies, actor_query):
    #filter movies by actor name (case-insensitive substring match). args: movies (list): list of movie dictionaries. actor_query (str): actor name to search for. returns: list: filtered movies matching the actor
    
    if not actor_query or actor_query.lower() == 'skip':
        return movies
    
    query = actor_query.strip().lower()
    return [m for m in movies if query in m['Notable Actors'].lower()]


def filter_by_rating(movies, rating_query):
    #filter movies by rating (case-insensitive exact match). args: movies (list): list of movie dictionaries. rating_query (str): rating to search for (e.g., 'pg', 'r', 'pg-13'). returns: list: filtered movies matching the rating
    
    if not rating_query or rating_query.lower() == 'skip':
        return movies
    
    query = rating_query.strip().upper()
    return [m for m in movies if m['Rating'].upper() == query]


def filter_by_length(movies, min_length=None, max_length=None):
    #filter movies by length (in minutes). args: movies (list): list of movie dictionaries. min_length (int): minimum movie length (inclusive). max_length (int): maximum movie length (inclusive). returns: list: filtered movies within the length range
    
    if min_length is None and max_length is None:
        return movies
    
    #initialize result list
    result = []
    #iterate through each movie
    for movie in movies:
        #attempt to convert length to integer
        try:
            length = int(movie['Length (min)'])
            #check if below minimum
            if min_length is not None and length < min_length:
                continue
            #check if above maximum
            if max_length is not None and length > max_length:
                continue
            result.append(movie)
        #handle invalid length values
        except ValueError:
            print(f"Warning: Invalid length value for {movie['Title']}")
            continue
    
    return result


def apply_filters(movies, genre=None, director=None, actor=None, rating=None, min_length=None, max_length=None):
    #apply multiple filters using and logic (all filters must match). args: movies (list): list of movie dictionaries. genre (str): genre filter (optional). director (str): director filter (optional). actor (str): actor filter (optional). rating (str): rating filter (optional). min_length (int): minimum length filter (optional). max_length (int): maximum length filter (optional). returns: tuple: (filtered_movies, applied_filters_count)
    
    #start with all movies
    result = movies
    #count of filters applied
    filters_applied = 0
    
    #apply genre filter if provided
    if genre:
        result = filter_by_genre(result, genre)
        #increment filter count
        filters_applied += 1
    
    #apply director filter if provided
    if director:
        result = filter_by_director(result, director)
        #increment filter count
        filters_applied += 1
    
    #apply actor filter if provided
    if actor:
        result = filter_by_actor(result, actor)
        #increment filter count
        filters_applied += 1
    
    #apply rating filter if provided
    if rating:
        result = filter_by_rating(result, rating)
        #increment filter count
        filters_applied += 1
    
    #apply length filter if provided
    if min_length is not None or max_length is not None:
        result = filter_by_length(result, min_length, max_length)
        #increment filter count
        filters_applied += 1
    
    #return filtered movies and count
    return result, filters_applied



def pretty_print_movies(movies, title=""):
    #pretty-print a list of movies in tabular format. args: movies (list): list of movie dictionaries to display. title (str): optional title for the display
    
    #check if movies list is empty
    if not movies:
        print("No movies found.")
        return
    
    #display title if provided
    if title:
        print(title)
    
    #display movie count
    print(f"Found {len(movies)} movie(s):\n")
    
    #iterate through each movie
    for i, movie in enumerate(movies, 1):
        #display movie title
        print(f"{i}. {movie['Title']}")
        #display director
        print(f"   Director: {movie['Director']}")
        #display genre
        print(f"   Genre: {movie['Genre']}")
        #display rating
        print(f"   Rating: {movie['Rating']}")
        #display length
        print(f"   Length: {movie['Length (min)']} minutes")
        #display actors
        print(f"   Notable Actors: {movie['Notable Actors']}")
        #blank line for readability
        print()


def print_full_list(movies):
    #display all movies in the database. args: movies (list): list of all movies
    
    #call pretty print with all movies
    pretty_print_movies(movies, "COMPLETE MOVIE DATABASE")


def print_welcome():
    #display welcome message and options
    #display menu options
    print("Hi, and welcome to Movie Recommendations!\n1 to search by director\n2 to search by actor\n3 to search by rating\n4 to search by genre\n5 to search by length range\n6 for custom multi-filter search\n7 to show all movies\n8 to exit")


def search_director(movies):
    #interactive director search.
    #get director input
    director = input("Enter director name (or 'skip' to skip): ").strip()
    #check if user wants to skip
    if director.lower() == 'skip':
        #return unchanged movies list
        return movies
    
    #filter by director
    results = filter_by_director(movies, director)
    #if results found
    if results:
        #display results
        pretty_print_movies(results, f"Movies directed by: {director}")
    #if no results found
    else:
        #display no results message
        print(f"\nNo movies found by director '{director}'.")
        #provide suggestion
        print("Try a shorter name or check the spelling.")
    
    #return filtered results
    return results


def search_actor(movies):
    #interactive actor search.
    #get actor input
    actor = input("Enter actor name (or 'skip' to skip): ").strip()
    #check if user wants to skip
    if actor.lower() == 'skip':
        #return unchanged movies list
        return movies
    
    #filter by actor
    results = filter_by_actor(movies, actor)
    #if results found
    if results:
        #display results
        pretty_print_movies(results, f"Movies with actor(s): {actor}")
    #if no results found
    else:
        #display no results message
        print(f"\nNo movies found with actor '{actor}'.")
        #provide suggestion
        print("Try a shorter name or check the spelling.")
    
    #return filtered results
    return results


def search_rating(movies):
    #interactive rating search.
    #display valid ratings
    print("Valid ratings: G, PG, PG-13, R, Not Rated")
    #get rating input
    rating = input("Enter rating (or 'skip' to skip): ").strip()
    #check if user wants to skip
    if rating.lower() == 'skip':
        #return unchanged movies list
        return movies
    
    #filter by rating
    results = filter_by_rating(movies, rating)
    #if results found
    if results:
        #display results
        pretty_print_movies(results, f"Movies with rating: {rating}")
    #if no results found
    else:
        #display no results message
        print(f"\nNo movies found with rating '{rating}'.")
    
    #return filtered results
    return results

#funtiong for searching genre in the movies list
def search_genre(movies):
    #interactive genre search.
    #get genre input
    genre = input("Enter genre (Drama, Action, Comedy, etc., or 'skip' to skip): ").strip()
    #check if user wants to skip
    if genre.lower() == 'skip':
        #return unchanged movies list
        return movies
    
    #filter by genre
    results = filter_by_genre(movies, genre)
    #if results found
    if results:
        #display results
        pretty_print_movies(results, f"Movies in genre: {genre}")
    #if no results found
    else:
        #display no results message
        print(f"\nNo movies found in genre '{genre}'.")
        #provide suggestion
        print("Try related genres or check the spelling.")
    
    #return filtered results
    return results


def search_length(movies):
    #interactive length search.
    #display instructions
    print("Enter minimum and/or maximum length (in minutes)")
    
    #get minimum length
    min_len_input = input("Minimum length (or press Enter to skip): ").strip()
    #get maximum length
    max_len_input = input("Maximum length (or press Enter to skip): ").strip()
    
    #initialize minimum
    min_len = None
    #initialize maximum
    max_len = None
    
    #attempt to parse lengths
    try:
        #if minimum was provided
        if min_len_input:
            #convert to integer
            min_len = int(min_len_input)
        #if maximum was provided
        if max_len_input:
            #convert to integer
            max_len = int(max_len_input)
    #if conversion fails
    except ValueError:
        #display error
        print("Invalid input. Please enter valid numbers.")
        #return unchanged movies list
        return movies
    
    #if neither provided
    if min_len is None and max_len is None:
        #return unchanged movies list
        return movies
    
    #filter by length
    results = filter_by_length(movies, min_len, max_len)
    
    #initialize length description list
    length_desc = []
    #if minimum provided
    if min_len:
        #add to description
        length_desc.append(f"at least {min_len} min")
    #if maximum provided
    if max_len:
        #add to description
        length_desc.append(f"at most {max_len} min")
    
    #if results found
    if results:
        #display results
        pretty_print_movies(results, f"Movies {' and '.join(length_desc)}")
    #if no results found
    else:
        #display no results message
        print(f"\nNo movies found matching the length criteria.")
        #provide suggestion
        print("Try adjusting the length range.")
    
    #return filtered results
    return results


def custom_search(movies):
    #interactive custom multi-filter search.
    #display instructions
    print("\nCombine multiple filters (all filters must match).\n")
    
    #get genre input
    genre = input("Genre (or press Enter to skip): ").strip() or None
    #get director input
    director = input("Director (or press Enter to skip): ").strip() or None
    #get actor input
    actor = input("Actor (or press Enter to skip): ").strip() or None
    #get rating input
    rating = input("Rating (or press Enter to skip): ").strip() or None
    
    #get minimum length
    min_len_input = input("Minimum length in minutes (or press Enter to skip): ").strip()
    #get maximum length
    max_len_input = input("Maximum length in minutes (or press Enter to skip): ").strip()
    
    #initialize minimum
    min_len = None
    #initialize maximum
    max_len = None
    
    #attempt to parse lengths
    try:
        #if minimum was provided
        if min_len_input:
            #convert to integer
            min_len = int(min_len_input)
        #if maximum was provided
        if max_len_input:
            #convert to integer
            max_len = int(max_len_input)
    #if conversion fails
    except ValueError:
        #display error
        print("Invalid length input. Skipping length filter.")
    
    #apply all filters with and logic
    results, filters_count = apply_filters(
        movies,
        genre=genre,
        director=director,
        actor=actor,
        rating=rating,
        min_length=min_len,
        max_length=max_len
    )
    
    #initialize filter summary
    filter_summary = []
    #if genre was provided
    if genre:
        #add to summary
        filter_summary.append(f"genre '{genre}'")
    #if director was provided
    if director:
        #add to summary
        filter_summary.append(f"director '{director}'")
    #if actor was provided
    if actor:
        #add to summary
        filter_summary.append(f"actor '{actor}'")
    #if rating was provided
    if rating:
        #add to summary
        filter_summary.append(f"rating '{rating}'")
    #if length filter was provided
    if min_len or max_len:
        #if both min and max provided
        if min_len and max_len:
            #add range to summary
            filter_summary.append(f"length {min_len}-{max_len} min")
        #if only min provided
        elif min_len:
            #add min to summary
            filter_summary.append(f"length >= {min_len} min")
        #if only max provided
        else:
            #add max to summary
            filter_summary.append(f"length <= {max_len} min")
    
    #if results found
    if results:
        #create title from filters
        title = f"Movies matching: {', '.join(filter_summary)}"
        #display results
        pretty_print_movies(results, title)
    #if no results found
    else:
        #display no results message
        print(f"\nNo movies match your criteria.")
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
    csv_path = "individual_projects/Movies_list.csv"
    
    #try to load movies
    try:
        #load movies from csv file
        movies = load_movies(csv_path)
        #display count of loaded movies
        print(f"Found {len(movies)} recommended movies!")
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
        choice = input("What would you like to do? (Enter 1-8): ").strip()
        #search by director
        if choice == "1":
            #call director search
            search_director(movies)
        #search by actor
        elif choice == "2":
            #call actor search
            search_actor(movies)
        #search by rating
        elif choice == "3":
            #call rating search
            search_rating(movies)
        #search by genre
        elif choice == "4":
            #call genre search
            search_genre(movies)
        #search by length
        elif choice == "5":
            #call length search
            search_length(movies)
        #custom multi-filter search
        elif choice == "6":
            #call custom search
            custom_search(movies)
        #show all movies
        elif choice == "7":
            #display all movies
            print_full_list(movies)
        #exit program
        elif choice == "8":
            #goodbye message
            print("\nThank you for using Movie Recommendations. Goodbye!")
            #exit loop
            break
        #invalid choice
        else:
            #error message
            print("Invalid choice. Please enter a number between 1 and 8.\n")
        
        #wait for user before showing menu again
        input("Press Enter to continue...")  


#start/run/call main function
main()