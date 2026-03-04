import turtle
import os

#funtion for triangle
def sierpinski(points, depth, color):
    #base case: if depth is 0
    if depth == 0:
        #call draw triangle function
        draw_triangle(points, color)
    else:
        #Midpoints
        #points to start and end triangle
        mid1 = ((points[0][0] + points[1][0]) / 2,
                (points[0][1] + points[1][1]) / 2)

        mid2 = ((points[1][0] + points[2][0]) / 2,
                (points[1][1] + points[2][1]) / 2)

        mid3 = ((points[0][0] + points[2][0]) / 2,
                (points[0][1] + points[2][1]) / 2)

        #Recursive calls
        sierpinski([points[0], mid1, mid3], depth - 1, color)
        sierpinski([mid1, points[1], mid2], depth - 1, color)
        sierpinski([mid3, mid2, points[2]], depth - 1, color)


#Koch Snowflake
def koch_snowflake(length, depth, color):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(3):
        koch_curve(length, depth)
        turtle.right(120)
    turtle.end_fill()

#funtion for drawing triangle
def draw_triangle(points, color):
    #turtle for fill in the color
    turtle.fillcolor(color)
    #turtle move up
    turtle.up()
    #turtle draw and go to
    turtle.goto(points[0])
    #turtle move down
    turtle.down()
    #turtle start filling
    turtle.begin_fill()
    #turtle draw until reached point
    turtle.goto(points[1])
    #turtle draw until reached point
    turtle.goto(points[2])
    #turte draw until reached point
    turtle.goto(points[0])
    #turtle stop filling/drawing
    turtle.end_fill()

#Koch Curve (helper for snowflake)
def koch_curve(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3
        koch_curve(length, depth - 1)
        turtle.left(60)
        koch_curve(length, depth - 1)
        turtle.right(120)
        koch_curve(length, depth - 1)
        turtle.left(60)
        koch_curve(length, depth - 1)

def size_of_screen(triangle, snowflake, screen):
    #turtle screen
    screen = turtle.Screen()
    #make the screen size
    screen.setup(width=800, height=800)
    #turtle speed = fast
    turtle.speed(0)
    #hide the turtle arrow
    turtle.hideturtle()
    #call fractal choice
    fratal_choice(triangle, snowflake)

#Save image (creates folder automatically)
def save_image(screen):
    filename = "individual_projects\\fractal_save"

    # Create folder if it doesn't exist
    folder = os.path.dirname(filename)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    screen.getcanvas().postscript(file=filename + ".eps")
    print(f"Image saved as {filename}.eps")

def fratal_choice(triangle, snowflake, screen):
    #Choose fractal
    #display instructions
    print("Choose fractal type:")
    print("1. Sierpinski Triangle")
    print("2. Koch Snowflake")

    #until false
    while True:
        #ask user what they want to enter
        choice = input("Enter choice (1 or 2): ")
        #if choice is valid
        if choice == "1":
            #call depth funtion
            return depth(screen), shape(triangle)
        elif choice == "2":
            return depth(screen), shape(triangle)
        #else
        else:
            #display invalid choice
            print("Invalid choice.")
            #restart loop
            continue

#funtion for depth of shape
def depth(screen):
    #Depth input
    while True:
        try:
            depth = int(input("\nEnter recursion depth (1-5): "))
            if 1 <= depth <= 5:
                break
            print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Enter a whole number.")

    #Colors
    color = input("\nEnter triangle color (e.g., red, blue, green): ")
    bg_color = input("Enter background color: ")
    screen.bgcolor(bg_color)

    print("\nGenerating fractal...\n")

def shape(triangle):
    size = 500
    points = [(-size/2, -size/3),
        (0, size/2),
        (size/2, -size/3)]
    sierpinski(points, depth, color)
    
    turtle.up()
    turtle.goto(-250, 150)
    turtle.down()
    koch_snowflake(500, depth, color)

    print("Fractal generated successfully!\n")

    #Save option
    save = input("Would you like to save the image? (y/n): ").lower()
    if save == "y":
        save_image(screen)

    input("\nPress Enter to exit the program.")
    turtle.done()


snowflake = koch_snowflake(length, depth, color)

triangle = sierpinski(points, depth, color)


def main():
    #display welcome message
    print("Welcome to the Sierpinski Triangle Generator!")
    print("This program creates a Sierpinski Triangle fractal using recursion.\n")
    fratal_choice()

main(snowflake, triangle)