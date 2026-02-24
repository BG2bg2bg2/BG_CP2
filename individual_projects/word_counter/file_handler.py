# file_handler.py
import os
from time_handler import get_clean_time

def read_file(path):
    #Read file and return its content
    if not os.path.exists(path):
        print("File not found.")
        return None
    try:
        with open(path, "r") as file:
            content = file.read()
        return content.strip()
    except:
        print("Error reading file.")
        return None

def add_content(path):
    #Append user text to file
    try:
        text = input("Type what you want to add: ")
        with open(path, "a") as file:
            file.write(text + "\n")
        print("Text added.")
    except FileNotFoundError:
        print("File not found.")

def update_word_count(path):
    #Append word count and timestamp to file
    try:
        with open(path, "r") as file:
            content = file.read()
        word_count = len(content.split())
        timestamp = get_clean_time()
        with open(path, "a") as file:
            file.write("\n---- Word Count Update ----\n")
            file.write(f"Words: {word_count}\n")
            file.write(f"Last Updated: {timestamp}\n")
        print("Word count updated successfully.")
        print(f"Words: {word_count}")
        print(f"Last Updated: {timestamp}")
    except FileNotFoundError:
        print("File not found.")

def view_file(path):
    #Display the content of the file
    content = read_file(path)
    if content is not None:
        print("\n--- File Content ---")
        print(content)
        print("--- End of File ---")