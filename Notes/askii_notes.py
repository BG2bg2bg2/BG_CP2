#BG 1st askii notes
import random

chars = []

for _ in range(9):
    if random.choice([True, False]):
        # uppercase letter
        chars.append(chr(random.randint(65, 90)))
    else:
        # lowercase letter
        chars.append(chr(random.randint(97, 122)))

result = ''.join(chars)
print(result)

#convert ascii to characters

# Convert single ASCII values to characters
ascii_value_A = 65
ascii_value_exclamation = 33

char_A = chr(ascii_value_A)
char_exclamation = chr(ascii_value_exclamation)

print(f"The character for ASCII value {ascii_value_A} is: {char_A}")
print(f"The character for ASCII value {ascii_value_exclamation} is: {char_exclamation}")

# Output:
# The character for ASCII value 65 is: A
# The character for ASCII value 33 is: !

ascii_values = [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100] # "Hello World"
result_string = ""

for value in ascii_values:
    result_string += chr(value)

print(f"The string from the ASCII values is: {result_string}")

# Output:
# The string from the ASCII values is: Hello World


#convert characters to ascii

# Convert single characters to ASCII values
char_B = 'B'
char_hash = '#'

ascii_value_B = ord(char_B)
ascii_value_hash = ord(char_hash)

print(f"The ASCII value for character '{char_B}' is: {ascii_value_B}")
print(f"The ASCII value for character '{char_hash}' is: {ascii_value_hash}")

# Output:
# The ASCII value for character 'B' is: 66
# The ASCII value for character '#' is: 35

input_string = "Python"
ascii_list = []

for char in input_string:
    ascii_list.append(ord(char))

print(f"The ASCII values for '{input_string}' are: {ascii_list}")

# Output:
# The ASCII values for 'Python' are: [80, 121, 116, 104, 111, 110]


