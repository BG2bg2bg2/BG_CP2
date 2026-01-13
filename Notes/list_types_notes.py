#BG 1st list notes

#Create a table showing how lists, tuples and sets are different

games = ["BTD2", "BTD6", "MTGA", "Satisfactory", "Trading Card Game Sim"]

print(games[3])
games[-2] = "DOW"

print(games)

fruit = ["apple", "orange", "peach", "kiwi"]
#tuple
home = (0,0)
x,y = home
print(x)
print(y)
#fruit[3 = "pineapple"]

#set
color = {"Orange", "Purple", "Green", "Blue", "Yellow", "Red"}
color.add("Pink")
color.remove("Purple")
for i in color:
    if i == "Orange":
        print("Fruit")
    print(i)

print("What punctuation is used for each type of list?")
print('commas')

print("Is it ordered")
print("yes")

print("Is it changeable")
print("Yes")

print("are duplicates allowed")
print("Yes")
games.append("BTD2")

print("What types of data would we store in each type of list?")

print("What methods can be used on the different types of lists?")