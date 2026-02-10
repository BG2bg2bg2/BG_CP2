#BG 1st movie recommendations

#bring in libraries
import csv

#funtion for seaching length
def length_of_movie():
    with open("BG_CP2\individual_projects\\Movies_list.csv", "r") as file:
        print("hi")
    #

#funtion for searching names, titles, rating, genra
def seaching():
    print("Hi")
    #

#main funtion
def main():
    fine = ["1",'2','3',"4"]
    allowed = ["1",'2','3',"4", "5", "6"]
    while True:
        #display Welcome to the movie recommendations I am here to help with... what ok ... I am here to help you to find what you want to watch
        print("Welcome to the movie recommendations I am here to help with\n\n... What??? ...\n\n... OK ...\n\n... \n\n... Got it ...\n\nI am here to help you to find what you want to watch.")
        #display 1 to search directors
        print("1 to search directiors")
        #display 2 to search actors
        print("2 to seach actors")
        #display 3 to search rating
        print("3 to search ratings")
        #display 4 to search genra
        print("4 to search genra")
        #display 5 to search length of movie
        print("5 to search the length of minimum and maximum of the movie")
        #display 6 to exit/leave program
        print("6 to exit/leave the program")
        #ask user to enter a number 1-6
        user = input("What do you want to do")
        if user == "6":
            break
        elif user == "5":
            length_of_movie()
        elif user != allowed:
            print("must enter a valid number")
            continue
        else:
            seaching()
#call main
main()