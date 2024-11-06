# Ethan Hankel
# UWYO COSC 1010
# Submission Date: 11/05/24
# Lab 8
# Lab Section: 02
# Sources, people worked with, help given to:
# I used the functions and while loop powerpoints
# Then when i had mistakes in my code or it wasn't working correctly than i used Chat GPT
# Had a lot of problems with having an extra space in my functions


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def int_check(value):
    try:
        int_value = int(value)
        return int_value
    except ValueError:
        try:
            float_value = float(value)
            if value.count(".") == 1:
                return float_value
            else:
                return False
        except ValueError:
            return False

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, low_bound, up_bound):
    if not isinstance(low_bound, int) or not isinstance(up_bound, int):
        return False
    if low_bound > up_bound:
        return False
    
    y_values = []
    for x in range(low_bound, up_bound + 1):
        y = m * x + b
        y_values.append(y)
    return y_values

while True:
    m = input("Enter Slope (m) or exit to quit: ")
    if m.lower() == 'exit': 
        break
    b = input("Enter intercept (b): ")
    low_bound = input("Enter Lower Bound for x: ")
    up_bound = input("Enter upper Bound for x: ")

    m = int_check(m)
    b = int_check(b)
    low_bound = int_check(low_bound)
    up_bound = int_check(up_bound)

    if isinstance(m, (int, float)) and isinstance(b, (int, float)) \
        and isinstance(low_bound, int) and isinstance(up_bound, int):
        y_values = slope_intercept(m, b, low_bound, up_bound)
        print("y values:", y_values)
    else:
        print("Please enter actual numbers!")
    


print("*" * 75)

# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null


import math


def safe_sqrt(value):
    if value < 0:
        return None
    return math.sqrt(value)

def quad_form(a, b, c):
    discrim = b**2 - 4*a*c
    sqrt_discrim = safe_sqrt(discrim)
    if sqrt_discrim is None:
        return None

    first_root = (-b + sqrt_discrim) / (2 * a)
    second_root = (-b - sqrt_discrim) / (2 * a)
    return first_root, second_root


    
while True:
    a = input("Enter coefficient a: ")
    if a.lower() == 'exit':
        break
    b = input("Enter coefficient b: ")
    c = input("Enter coefficient c: ")

    a = int_check(a)
    b = int_check(b)
    c = int_check(c)

    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        roots = quad_form(a, b, c)
        print("Roots", roots)
    else:
        print("Please enter actual number!")



