a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("The greatest common divisor of", a, "and", b, "is...")

while b > 0:
    remainder = a % b
    a, b = b, remainder

print(a)
