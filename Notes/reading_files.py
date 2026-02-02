#BG 1st reading files
while True:
    try:
        #How do you open a file in your program?
        #Notes/reading.txt
        with open("Notes\\reading.txt", "r") as file:
    
        #How do you alter text to work as data in a program?
            content = file.read()
            print(content)

#How do you keep your program from breaking if the file can't be found?
#try
#exept
    except:
        print("that file can't be found")
    else:
        print("My code works!")
        print(content)
        break
#What is a CSV file Download CSV file?

#How are they used in programming?

#How id reading a CSV different from reading a txt file?