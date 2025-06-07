import math

# 1. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# ```
# *
# **
# ***
# ```
# if input is 4 then it should print
# ```
# *
# **
# ***
# ****
# ```
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

def print_pattern(n=5):
    '''
    :param n: Integer number representing number of lines
    to be printed in a pattern. If n=3 it will print,
      *
      **
      ***
    If n=4, it will print,
      *
      **
      ***
      ****
    Default value for n is 5. So if function caller doesn't
    supply the input number then it will assume it to be 5
    :return: None
    '''
    for i in range(n+1):
        s = ""
        for j in range(i):
            s += "*"
        print(s)


# 2. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# ```
# area = (1/2)*base*height
# ```
#
# 3. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# ```
# rectangle area=length*width
# ```
# If no shape is supplied then it should take triangle as a default shape

def calculate_area(dimension1, dimension2, shape = "triangle"):
    """
    Calculate the area of a triangle or rectangle based on given dimensions.

    Parameters:
        dimension1 (float): The base or length of the shape.
        dimension2 (float): The height or width of the shape.
        shape (str): The type of shape ("triangle" or "rectangle").

    Returns:
        float or None: The calculated area if the shape is valid; otherwise, None.
    """
    if shape == "triangle":
        return (1/2)*dimension1*dimension2
    elif shape == "rectangle":
        return dimension1*dimension2
    else:
        print("Error: Input shape is neither triangle nor rectangle")
        return None
    

# 3. Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and returns area, circumference and diameter. You should get these values in your main program by calling circle_calc function and then print them.

def circle_calc(radius):
    area_of_circle = round(math.pi*(radius**2), 2)
    circumference = round(2*math.pi*radius, 2)
    diameter = 2*radius
    return area_of_circle, circumference, diameter  



base = float(input("Enter dimension of figure : "))
height = float(input("Enter another dimension of the figure: "))
figure = input("Enter shape of the figure (triangle/rectangle): ").lower()

area = calculate_area(base, height, figure)
print(f"Area of {figure} is: {area}")



print("Print pattern with input = 3")
print_pattern(3)
print("Print pattern with input = 4")
print_pattern(4)
print("Print pattern without parameter or default parameter")
print_pattern()



if __name__ == "__main__":
    radius = input("Enter radius of the circle: ")
    radius = float(radius)
    circle_Area, c, d = circle_calc(radius)
    print(f"Area: {circle_Area}, Circumference: {c}, Diameter: {d}")
