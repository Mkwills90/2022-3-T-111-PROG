"""A program that calculates the volume of a hemisphere.

Prompts for a diameter, d (a float),
calculates the volume of half a sphere with diameter d,
and prints the result.
"""

import math

d = float(input("What is the diameter? "))

r = d/2
volume_of_sphere = (4/3) * math.pi * (r**3)
volume_of_half_sphere = volume_of_sphere/2

print("The volume of the half-sphere is", round(volume_of_half_sphere, 2))