#BG 1st write to nots

 
#How do you find a file in a folder?

#with open("BG_CP2/Notes\\reading.txt", "w") as file:
#    file.write("I wrote on my file")
#print("code end")

#with open("BG_CP2/Notes\\write.txt", "r+") as file:
#    file.write("\nThis is more on my file")
#print("Code end")

#In a python project how do you open a file?

#What is the difference between writing, appending, and creation modes?

#How is writing to a CSV different from writing to a txt file
import csv
with open("BG_CP2\\Notes\\Sample.csv", "r+", newline='\n') as csvfile:
    fieldnames = ["username", "color"]
    reader = csv.reader(csvfile)
    for line in reader:
        #parsing a string to make it easy to read
        print(f"{fieldnames[0]}, {line[0]} favorite color {line[1]}")
    #writer = csv.writer(csvfile, delimiter=',')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'username': "rUb", "color": 'Orange'})
    writer.writerow({'username': 'Bob', 'color': 'blue'})
    writer.writerow({'username': 'lob', 'color': 'green'})
    writer.writerow({'username': 'cob', 'color': 'red'})

print('code is done')