#BG 1st document word counter
import os
from file_handler import add_content, view_file, update_word_count, read_file


def main():
    #display welcome and use an internal header that matches sample output
    print("--- Document Word Count Updater ---")
    base = os.path.dirname(__file__)
    default_path = os.path.join(base, "file.txt")
    path = None

    while True:
        #display menu and prompt
        print("\n--- Document Word Count Updater ---")
        print("1. Update document info\n2. View document\n3. Add content to document\n4. Exit")
        option = input("Enter your choice (1-4): ").strip()

        if option == "1":
            # If no path set yet, ask for exact file path; empty input will perform update on current path
            p = input("\nEnter the exact file path for your document (press Enter to update current file): ").strip()
            if p:
                path = p
                print(f"Using file: {path}")
            else:
                if not path:
                    path = default_path
                # perform update
                wc, ts = update_word_count(path)
                if wc is not None:
                    print(f"Document updated. Word count: {wc}")
                    print("\nFILE UPDATES:\n")
                    view_file(path)
        elif option == "2":
            if not path:
                path = input("Enter the exact file path for your document: ").strip() or default_path
            print("\nDocument content:")
            view_file(path)
        elif option == "3":
            if not path:
                path = input("Enter the exact file path for your document: ").strip() or default_path
            add_content(path)
        elif option == "4":
            print("Exiting. Goodbye.")
            break
        else:
            print("Please enter a valid option (1-4).")

#run the main function
main()