#BG 1st morse code translater

#Create two tuples (one of the alphabet letters in English, and other for the corresponding Morse Code Symbols) 
#tuple for letters
letter = ("a","b","c","d","e","f","g",'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

#tuple for morse code
code = (".- "," -... "," -.-. "," -.. "," . "," ..-. "," --. "," .... "," .. "," .--- "," -.- "," .-.. "," -- "," -. "," --- "," .--. "," --.- "," .-. "," ... "," - "," ..- "," ...- "," .-- "," -..- "," -.-- "," --..")

#Create a function to translate English into Morse Code
def english_to_morse():
    enter = input("Enter a phrase that can convert into code\n\nOnly use letters: ")
#Create a function to translate Morse Code into English
def morse_to_english():
    #user inputs the code
    enter = input("Enter the code that you want to be converted into letters\n\nCP will try to convert everythig as long as it is a letter: ")
    #if user inputs the code and in code
    if enter in code:
        #for index code enumorate code
        for index, enter in enumerate(code):
            count = code.count(len(index))
            print(count)
                
#Create a main loop where users can choose to translate English to Morse Code, Morse Code to English, or Exit
def main():
    while True:
        print("Welcome to the Morse code translater")
        print("1 to translate Engilsh to morse code")
        print("2 to translate morse code to English")
        print("3 to exit the translater")
        enter = input("Enter the number of what you want to do: ")
        if enter == "1":
            english_to_morse()
        elif enter == "2":
            morse_to_english()
        elif enter == "3":
            break
        else:
            print("Try a gain and enter a vaild answer")
            continue
#Project needs to:
#Use string manipulation to control the appearance of the output 
#Use basic error handling (for characters not in Morse Code)
#Use good naming for functions and variables
#Use pseudocode comments to explain what the program is doing
#Use white space to make sure code is easy to read
main()