import math

length_cm = 50

degrees = int(input("Roof's angle in degrees: "))
radians = math.radians(degrees)

hypotenuse = length_cm / math.cos(radians)
height_cm = math.sin(radians) * hypotenuse

# Alternatively:
# height_cm = math.tan(radians) * length_cm

print("To make the platform level, the height must be", round(height_cm, 1), "cm")
