from turtlefunctions import turtleFunctions

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Ask the user for input and save it as a variable
    print("Is it daytime? (y or n)")
    daytime = input()

    # Create our turtle object which has our drawing functions
    turtle = turtleFunctions()

    # If it is daytime (daytime is 'y'), draw a sun
    if daytime == 'y':
        turtle.draw_sun()
    # For any other values, draw a star
    else:
        turtle.draw_star()
