num = int(input("Enter an integer: "))
largest = 0
evens = 0
odds = 0
cum_total = 0

while num > 0:
    if num > largest:
        largest = num

    if num % 2 == 0:
        evens += 1 
    else:
        odds += 1
    
    cum_total = cum_total + num
    print("Cumulative total:",cum_total)
    num = int(input("Enter an integer: "))

if largest != 0:
    print("Largest number:", largest)
    print("Count of even numbers:", evens)
    print("Count of odd numbers:", odds)
