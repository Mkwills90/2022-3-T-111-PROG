rating = int(input("Input elo rating: "))

if rating < 1000:
    print("Invalid")
elif rating < 2400:
    print("Amateur")
elif rating < 2500:
    print("International")
elif rating < 2700:
    print("Grandmaster")
else:
    print("Super grandmaster")
