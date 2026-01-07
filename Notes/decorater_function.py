#BG 1st decorater funtion notes

def decorator(func):
    def wrapper():
        print ("Befor calling the funtion")
        func()
        print ("after calling the function")
    return wrapper

@decorator
def greet():
    print ("Hello, World")

greet()

@decorator
def add():
    print(1+1)

add()