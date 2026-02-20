#BG 1st

#funtion for main
#main
    #display welcome to the Document Word Counter
    #loop till false
        #display options
        #1 to update document info (the name of the file/document)
        #2 to view document (read what is on the document)
        #3 to add content to document (write on the document)
        #4 to exit (save and quit)
        #user enter option
        
        #if user entered 1
            #loop false and call update

        #else if user entered 2
            #loop false and call view document

        #else if user entered 3
            #loop false and call add content

        #else if user entered 4
            #save file
            #loop false as break

        #else
            #display enter valid option
            #restart loop as continue

#funtion for call update
def call_update():
    #exact path is for only this cpu
    #relitive path is universal meaning you can use any cpu with vscode or python language
    #display enter the exact or reltive path
    #user enter path
    path = input("Enter the path that you want to use example for defalt: file_handler_word_counter.txt")
    #try
    try:
        with open("path", mode = "r") as file:
        #How do you alter text to work as data in a program?
            for line in file:
                print(f"Hello{line.strip()}")
            #content = file.read()
            #print(content)
    except:
        print("Can't find the file")
        #if path not found
            #add path
        #else if path found
            #use path
    #exept
        #display can't use that path because it won't work