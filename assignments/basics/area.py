"""A program that calculates the area of a triangle.

Prompts for three floats,
denoting the lengths of the sides of a triangle,
calculates the area, and prints the result.
"""

import math

a_str = input("Enter the value for a: ")
b_str = input("Enter the value for b: ")
c_str = input("Enter the value for c: ")

# Convert values to float
a_float, b_float, c_float = float(a_str), float(b_str), float(c_str)

s = (a_float + b_float + c_float) / 2
area = math.sqrt(s * (s - a_float) * (s - b_float) * (s - c_float))

print("The area of the triangle is", area)