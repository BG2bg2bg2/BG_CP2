#BG 1st fractal pattern generator

#import turtle library
import turtle as t
#funtion for entering color
def shape_color(color_choice):
    colors = ["red", "blue", "green", "black"]
    while True:
        color_choice = input("Enter the color you want for the triange")
        if color_choice not in colors:
            print("Please enter a valid color")
        else:
            return t.color(color_choice)
#funtion for entering the amount of triangles needed


#main function that runs the program and handles user input
def main(color_choice, depth):
    while True:
        print("Welcome to the fractal pattern generator")
        user_shape_choice = input("To make a triangle with color red enter 1\nTo make a triangle with your choice of color enter 2\nTo make a triangle with your choice of depth enter 3\nTo make a triange with your choice of depth and color enter 4\nTo make shape of your choice enter 5")
        if user_shape_choice == "1":
            color_choice = "red"
            depth = 100
            return draw_shape(color_choice, depth)
        
        elif user_shape_choice == "2":
            depth = 100
            return depth, shape_color(color_choice)
        
        elif user_shape_choice == "3":
            print("send you to shape funtion")
        elif user_shape_choice == "4":
            print("shape_choice()")
#function to draw the Sierpinski Triangle using recursion
def draw_shape(color_choice, depth):
    while True:
        t.color(color_choice)
        for x in range(1,depth):
            t.forward(depth)
            t.right(120)
        t.end_fill()
#Use Python's turtle graphics module for drawing
#Allow users to specify:
#Recursion depth (1-5)
#Triangle color
#HINT: Remember to implement a base case in your recursive function to prevent infinite recursion!

#HINT: Use thins image to help you think about HOW to draw this with turtle!

main(color_choice = t.color(), depth = t.forward(3))
