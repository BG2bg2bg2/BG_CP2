# file_handler.py
import os
from time_handler_word_counter import get_clean_time

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
    # Append multi-line user text to file (press Enter twice to finish)
    try:
        print("Enter new content (press Enter twice to finish):")
        lines = []
        prev_empty = False
        while True:
            line = input()
            if line == "":
                if prev_empty:
                    break
                prev_empty = True
                # preserve a single blank line in content
                lines.append("")
                continue
            prev_empty = False
            lines.append(line)

        text = "\n".join(lines).rstrip() + "\n"
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "a") as file:
            file.write(text)
        print("Content added successfully.")
    except FileNotFoundError:
        print("File not found.")

def update_word_count(path):
    # Append word count and timestamp to file; return (word_count, timestamp) on success
    try:
        with open(path, "r") as file:
            content = file.read()
        word_count = len(content.split())
        timestamp = get_clean_time()
        with open(path, "a") as file:
            file.write("\n\nWord Count: {0}\nLast Updated: {1}\n".format(word_count, timestamp))
        return word_count, timestamp
    except FileNotFoundError:
        print("File not found.")
        return None, None

def view_file(path):
    #Display the content of the file
    content = read_file(path)
    if content is not None:
        print("\n--- File Content ---")
        print(content)
        print("--- End of File ---")