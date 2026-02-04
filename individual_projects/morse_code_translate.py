# BG 1st Morse Code Translator

# Create two tuples (one of the alphabet letters in English, 
# and the other for the corresponding Morse Code symbols)
# Tuple for letters
letter = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
          "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

# Tuple for morse code (each morse code corresponds to each letter)
code = (".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", 
        ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", 
        "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..")

# Create a dictionary for easier lookup (maps letters to morse code and vice versa)
letter_to_morse = dict(zip(letter, code))
morse_to_letter = dict(zip(code, letter))


# Function to translate English into Morse Code
def english_to_morse():
    # Get user input - only letters will be processed
    user_input = input("Enter a phrase to convert to Morse Code\n(Only letters will be converted): ").lower()
    
    # Error handling: check if input is empty
    if not user_input.strip():
        print("Error: Please enter some text to translate.\n")
        return
    
    # Process each character in the input
    morse_output = ""
    invalid_chars = []
    
    for char in user_input:
        if char == " ":
            # Add space between words in morse code output
            morse_output += "/ "
        elif char in letter_to_morse:
            # Add the morse code for this letter
            morse_output += letter_to_morse[char] + " "
        else:
            # Track characters that cannot be converted
            if char not in invalid_chars:
                invalid_chars.append(char)
    
    # Display the morse code output with proper formatting
    print(f"English: {user_input}")
    print(f"Morse Code: {morse_output.strip()}")
    
    # Error handling: display invalid characters if any were found
    if invalid_chars:
        print(f"Note: The following characters were skipped (not letters): {', '.join(invalid_chars)}\n")


# Function to translate Morse Code into English
def morse_to_english():
    # Get user input - morse code separated by spaces
    user_input = input("Enter Morse Code to convert to English\n(Use space between letters, / for word breaks): ")
    
    # Error handling: check if input is empty
    if not user_input.strip():
        print("Error: Please enter some Morse Code to translate.\n")
        return
    
    # Process morse code input
    morse_output = ""
    invalid_codes = []
    
    # Split by "/" to separate words
    words = user_input.split("/")
    
    for word in words:
        # Split each word by spaces to get individual morse codes
        morse_chars = word.strip().split()
        
        for morse_char in morse_chars:
            if morse_char in morse_to_letter:
                # Add the letter corresponding to this morse code
                morse_output += morse_to_letter[morse_char]
            else:
                # Track morse codes that cannot be converted
                if morse_char not in invalid_codes and morse_char != "":
                    invalid_codes.append(morse_char)
        
        # Add space between words
        morse_output += " "
    
    # Display the english output with proper formatting
    print(f"Morse Code: {user_input}")
    print(f"English: {morse_output.strip()}")
    
    # Error handling: display invalid morse codes if any were found
    if invalid_codes:
        print(f"Note: The following codes were not recognized: {', '.join(invalid_codes)}\n")


# Main function - creates a loop where users can choose translation options
def main():
    while True:
        # Display menu options with clear formatting
        print("Welcome to the Morse Code Translator!\n")
        print("1 - Translate English to Morse Code")
        print("2 - Translate Morse Code to English")
        print("3 - Exit the Translator")
        
        # Get user choice
        user_choice = input("Enter the number of what you want to do: ")
        
        # Error handling: validate user choice
        if user_choice == "1":
            english_to_morse()
        elif user_choice == "2":
            morse_to_english()
        elif user_choice == "3":
            print("\nThank you for using the Morse Code Translator. Goodbye!\n")
            break
        else:
            print("Error: Please enter a valid option (1, 2, or 3).\n")
            continue


# Run the program
main()