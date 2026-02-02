#BG 1st reading files
import csv
while True:
    try:
        #How do you open a file in your program?
        #Notes/reading.txt
        with open("Notes\\reading.txt", "r") as file:

        #How do you alter text to work as data in a program?
            for line in file:
                print(f"Hello{line.strip()}")
            #content = file.read()
            #print(content)

#How do you keep your program from breaking if the file can't be found?
#try
#exept
    except:
        print("that file can't be found")
    else:
        print("My code works!")
        break
#What is a CSV file Download CSV file?
try:
    with open("C:\Users\brett.gerlach\Downloads\Class CSV sample - Sheet1.csv", mode = "r") as File:
    #CSV = comma Seporated Values files
    
#How are they used in programming?

#How id reading a CSV different from reading a txt file?