num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))

max_int = num1
if num2 > max_int:
    max_int = num2
if num3 > max_int:
    max_int = num3

print(f"{max_int} is the greatest of the three numbers.")

# Alternatively:
# if num1 > num2 and num1 > num3:
#     max_int = num1
# elif num2 > num3:
#     max_int = num2
# else:
#     max_int = num3
