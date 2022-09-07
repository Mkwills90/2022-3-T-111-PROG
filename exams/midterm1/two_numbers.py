num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))

if num1 > num2:
    print("First number is larger.")
elif num2 > num1:
    print("Second number is larger.")
else:
    print("The numbers are equal.")

if num1 % 2 == 0 or num2 % 2 == 0:
    print("At least one number is even.")
if num1 % 2 == 1 or num2 % 2 == 1:
    print("At least one number is odd.")