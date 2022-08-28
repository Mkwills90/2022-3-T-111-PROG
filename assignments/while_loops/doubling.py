answer = input("You need something doubled? (Y)es? (N)o? ")
while answer == 'Y':
    number = float(input("All right, then. Give me a number, and I'll double it for ya: "))
    doubled = 2 * number
    print("That's easy!", number, "doubled is", doubled)

    answer = input("You need something else doubled? (Y)es? (N)o? ")