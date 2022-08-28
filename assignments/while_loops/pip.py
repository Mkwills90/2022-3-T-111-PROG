number = int(input("Enter a positive integer: "))

no_7_found_yet = True
while number > 0 and no_7_found_yet:
    last_digit = number % 10
    if last_digit == 7:
        no_7_found_yet = False
    number = number // 10

if no_7_found_yet:
    print("The number does not contain the digit 7.")
else:
    print("The number contains the digit 7.")