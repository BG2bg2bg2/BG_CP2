import turtle
import os


#Draw a filled triangle

def draw_triangle(points, color):
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(points[0])
    turtle.down()
    turtle.begin_fill()
    turtle.goto(points[1])
    turtle.goto(points[2])
    turtle.goto(points[0])
    turtle.end_fill()



#Recursive Sierpinski Triangle

def sierpinski(points, depth, color):
    #BASE CASE
    if depth == 0:
        draw_triangle(points, color)
    else:
        #Midpoints
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



#Koch Snowflake (Extra Credit)

def koch_snowflake(length, depth, color):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(3):
        koch_curve(length, depth)
        turtle.right(120)
    turtle.end_fill()



#Save image (creates folder automatically)

def save_image(screen):
    filename = "individual_projects/fractal_save"

    # Create folder if it doesn't exist
    folder = os.path.dirname(filename)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    screen.getcanvas().postscript(file=filename + ".eps")
    print(f"Image saved as {filename}.eps")



#MAIN FUNCTION

def main():
    print("Welcome to the Sierpinski Triangle Generator!")
    print("This program creates a Sierpinski Triangle fractal using recursion.\n")

    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    turtle.speed(0)
    turtle.hideturtle()

    #Choose fractal
    print("Choose fractal type:")
    print("1. Sierpinski Triangle")
    print("2. Koch Snowflake")

    while True:
        choice = input("Enter choice (1 or 2): ")
        if choice in ["1", "2"]:
            break
        print("Invalid choice.")

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

    if choice == "1":
        size = 500
        points = [(-size/2, -size/3),
                  (0, size/2),
                  (size/2, -size/3)]
        sierpinski(points, depth, color)
    else:
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


main()