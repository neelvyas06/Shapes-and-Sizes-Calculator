"""
******************************
CS 1026 - Assignment 1 - Shapes and Sizes Calculator
Code by: [Neel Vyas]
Student ID: [NVYAS23]
File created: September 22, 2024
******************************

This program calculates the perimeter and area of various shapes:
rectangle, triangle, circle, trapezoid, and hexagon.

"""

import math  # Importing math library for constants like pi and functions like sqrt


# Function to calculate perimeter and area of a rectangle
def calculate_rectangle():
    width = float(input("Enter width: "))  # Get width of rectangle from user
    height = float(input("Enter height: "))  # Get height of rectangle from user

    # Check if the input values are valid (greater than 0)
    if width <= 0 or height <= 0:
        print("Invalid value entered")  # Print error message if any dimension is invalid
        return  # Exit the function if invalid input is detected

    # Calculate perimeter and area of the rectangle
    perimeter = 2 * (width + height)  # Perimeter = 2 * (width + height)
    area = width * height  # Area = width * height

    # Output the results, rounded to 2 decimal places
    print(f"Rectangle - Perimeter: {perimeter:.2f}, Area: {area:.2f}")


# Function to calculate perimeter and area of a triangle
def calculate_triangle():
    base = float(input("Enter base: "))  # Get base of triangle
    side_a = float(input("Enter side a: "))  # Get second side of triangle
    side_c = float(input("Enter side c: "))  # Get third side of triangle
    height = float(input("Enter height: "))  # Get height of triangle

    # Check if all inputs are positive numbers
    if base <= 0 or side_a <= 0 or side_c <= 0 or height <= 0:
        print("Invalid value entered")  # Error message if input is invalid
        return  # Exit the function if invalid input is detected

    # Calculate perimeter and area of the triangle
    perimeter = base + side_a + side_c  # Perimeter = sum of all sides
    area = (base * height) / 2  # Area = (base * height) / 2

    # Output the results, rounded to 2 decimal places
    print(f"Triangle - Perimeter: {perimeter:.2f}, Area: {area:.2f}")


# Function to calculate perimeter and area of a circle
def calculate_circle():
    radius = float(input("Enter radius: "))  # Get radius of circle from user

    # Check if radius is a positive number
    if radius <= 0:
        print("Invalid value entered")  # Error message if input is invalid
        return  # Exit the function if invalid input is detected

    # Calculate perimeter (circumference) and area of the circle
    perimeter = 2 * math.pi * radius  # Perimeter = 2 * pi * radius
    area = math.pi * radius ** 2  # Area = pi * radius^2

    # Output the results, rounded to 2 decimal places
    print(f"Circle - Perimeter: {perimeter:.2f}, Area: {area:.2f}")


# Function to calculate perimeter and area of a trapezoid
def calculate_trapezoid():
    top_side = float(input("Enter top side: "))  # Get top side length
    bottom_side = float(input("Enter bottom side: "))  # Get bottom side length
    left_side = float(input("Enter left side: "))  # Get left side length
    right_side = float(input("Enter right side: "))  # Get right side length
    height = float(input("Enter height: "))  # Get height of trapezoid

    # Check if all inputs are positive numbers
    if top_side <= 0 or bottom_side <= 0 or left_side <= 0 or right_side <= 0 or height <= 0:
        print("Invalid value entered")  # Error message if input is invalid
        return  # Exit the function if invalid input is detected

    # Calculate perimeter and area of the trapezoid
    perimeter = top_side + bottom_side + left_side + right_side  # Perimeter = sum of all sides
    area = ((top_side + bottom_side) * height) / 2  # Area = ((top + bottom) * height) / 2

    # Output the results, rounded to 2 decimal places
    print(f"Trapezoid - Perimeter: {perimeter:.2f}, Area: {area:.2f}")


# Function to calculate perimeter and area of a hexagon
def calculate_hexagon():
    side_length = float(input("Enter side length: "))  # Get length of one side

    # Check if the input is a positive number
    if side_length <= 0:
        print("Invalid value entered")  # Error message if input is invalid
        return  # Exit the function if invalid input is detected

    # Calculate perimeter and area of the hexagon
    perimeter = 6 * side_length  # Perimeter = 6 * side length
    area = (3 * math.sqrt(3) / 2) * side_length ** 2  # Area = (3 * sqrt(3) / 2) * side_length^2

    # Output the results, rounded to 2 decimal places
    print(f"Hexagon - Perimeter: {perimeter:.2f}, Area: {area:.2f}")


# Main function to handle user input and shape selection
def main():
    # Display the available shapes for the user
    print("You can calculate the perimeter and area for the following shapes:")
    print("Rectangle, Triangle, Circle, Trapezoid, Hexagon")

    # Get the shape name from the user (case-insensitive)
    shape = input("Enter the name of the shape: ").strip().lower()

    # Check which shape was entered and call the corresponding function
    if shape == "rectangle":
        calculate_rectangle()
    elif shape == "triangle":
        calculate_triangle()
    elif shape == "circle":
        calculate_circle()
    elif shape == "trapezoid":
        calculate_trapezoid()
    elif shape == "hexagon":
        calculate_hexagon()
    else:
        print("Invalid shape entered")  # Error message if an invalid shape is entered


# Ensure the program runs only if executed directly
if __name__ == "__main__":
    main()
