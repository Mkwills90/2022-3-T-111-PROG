number_of_players = 0
while number_of_players < 2:
    number_of_players = int(input("Enter number of players (at least 2): "))

player = 0
total = 0
while player < number_of_players:
    print("Your turn, player", player)
    contribution_of_player = int(input("Enter any number you like: "))
    total += contribution_of_player
    player += 1

chosen_one = total % number_of_players
print("The sum of all contributions is", total)
print("When", total, "is divided by", number_of_players, "the remainder is", chosen_one)
print("Player", chosen_one, "is the winner!")
