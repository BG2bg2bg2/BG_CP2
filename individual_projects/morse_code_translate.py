#BG 1st Morse Code Translator

#create two tuples (one of the alphabet letters in English, 
#and the other for the corresponding Morse Code symbols)
#tuple for letters
letter = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
          "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

#tuple for morse code (each morse code corresponds to each letter)
code = (".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", 
        ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", 
        "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..")

#create a dictionary for easier lookup (maps letters to morse code and vice versa)
letter_to_morse = dict(zip(letter, code))
morse_to_letter = dict(zip(code, letter))


#function to translate English into Morse Code
def english_to_morse():
    #get user input - only letters will be processed
    user_input = input("Enter a phrase to convert to Morse Code\n(Only letters will be converted): ").lower()
    
    #check if input is empty
    if not user_input.strip():
        print("Please enter some text to translate.\n")
        return
    
    #process each character in the input
    morse_output = ""
    invalid_chars = []
    
    for char in user_input:
        if char == " ":
            #add space between words in morse code output
            morse_output += "/ "
        elif char in letter_to_morse:
            #add the morse code for this letter
            morse_output += letter_to_morse[char] + " "
        else:
            #track characters that cannot be converted
            if char not in invalid_chars:
                invalid_chars.append(char)
    
    #display the morse code output with proper formatting
    print(f"English: {user_input}")
    print(f"Morse Code: {morse_output.strip()}")
    
    #display invalid characters if any were found
    if invalid_chars:
        print(f"The following characters were skipped (not letters): {', '.join(invalid_chars)}\n")


#function to translate Morse Code into English
def morse_to_english():
    #get user input - morse code separated by spaces
    user_input = input("Enter Morse Code to convert to English\n(Use space between letters, / for word breaks): ")
    
    #check if input is empty
    if not user_input.strip():
        print("Please enter some Morse Code to translate.\n")
        return
    
    #process morse code input
    morse_output = ""
    invalid_codes = []
    
    #split by "/" to separate words
    words = user_input.split("/")
    
    for word in words:
        #split each word by spaces to get individual morse codes
        morse_chars = word.strip().split()
        
        for morse_char in morse_chars:
            if morse_char in morse_to_letter:
                #add the letter corresponding to this morse code
                morse_output += morse_to_letter[morse_char]
            else:
                #track morse codes that cannot be converted
                if morse_char not in invalid_codes and morse_char != "":
                    invalid_codes.append(morse_char)
        
        #add space between words
        morse_output += " "
    
    #display the english output with proper formatting
    print(f"Morse Code: {user_input}")
    print(f"English: {morse_output.strip()}")
    
    #if there is a not valid code
    if invalid_codes:
        #display invalid morse codes
        print(f"Note: The following codes were not recognized: {', '.join(invalid_codes)}\n")


#main function that creates a loop where user can choose translation options
def main():
    while True:
        #display Welcome to the Morse Code Translator!
        print("Welcome to the Morse Code Translator!\n")
        #display 1 to Translate English to Morse Code
        print("1 to Translate English to Morse Code")
        #display 2 to Translate Morse Code to English
        print("2 to Translate Morse Code to English")
        #display 3 to Exit the Translator
        print("3 to Exit the Translator")
        
        #get user choice
        user_choice = input("Enter the number of what you want to do: ")
        
        #if user wants to translate engilsh to morse code by pressing 1
        if user_choice == "1":
            #call from english_to_morse translate funtion
            english_to_morse()
        #else if user want to translate morse code to english by pressing 2
        elif user_choice == "2":
            #call from morse_to_english translate funtion
            morse_to_english()
        #else if user want to quit by pressing 3
        elif user_choice == "3":
            #display Thank you for using the Morse Code Translator. Goodbye!
            print("\nThank you for using the Morse Code Translator. Goodbye!\n")
            #end program
            break
        else:
            print("Please enter a valid option (1, 2, or 3).\n")
            continue


#Run the program
main()