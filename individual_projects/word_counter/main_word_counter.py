#BG 1st

from file_handler import add_contnt, view_file, update_word_count

#funtion for main
def main():
#main
    #display welcome to the Document Word Counter
    print("Welcome to the Document Word Counter")
    #loop till false
    while True:
        #display options
        #1 to update document info (the name of the file/document)
        #2 to view document (read what is on the document)
        #3 to add content to document (write on the document)
        #4 to exit (save and quit)
        print("1 to update document info (the name of the file/document)\n2 to view document (read what is on the document)\n3 to add content to document (write on the document)\n4 to exit (save and quit)")
        #user enter option
        option = input("Enter the number that you want to do")
        
        #if user entered 1
        if option == "1":
            #loop false and call update
            update_word_count(path)
        #else if user entered 2
        elif option == "2":    
            #loop false and call view document
            view(path)

        #else if user entered 3
        elif option == "3":
            #loop false and call add content
            add_content(path)
        #else
        else:
            #display enter valid option
            print("Please enter valid option")
            #restart loop as continue
            continue