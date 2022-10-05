# Constants
NORTH = "n"
EAST = "e"
SOUTH = "s"
WEST = "w"


def main():
    row = 1
    col = 1

    while not destination_reached(col, row):
        valid_directions = find_directions(col, row)
        print_directions(valid_directions)
        col, row = play_one_move(col, row, valid_directions)

    print("Victory!")


def destination_reached(col, row):
    """Returns True if player is in the victory cell."""

    return col == 3 and row == 1  # (3,1)


def find_directions(col, row):
    """Returns valid directions as a string given the supplied location."""

    if col == 1 and row == 1:  # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2:  # (1,2)
        valid_directions = NORTH + EAST + SOUTH
    elif col == 1 and row == 3:  # (1,3)
        valid_directions = EAST + SOUTH
    elif col == 2 and row == 1:  # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2:  # (2,2)
        valid_directions = SOUTH + WEST
    elif col == 2 and row == 3:  # (2,3)
        valid_directions = EAST + WEST
    elif col == 3 and row == 2:  # (3,2)
        valid_directions = NORTH + SOUTH
    elif col == 3 and row == 3:  # (3,3)
        valid_directions = SOUTH + WEST

    return valid_directions


def print_directions(available_directions: list) -> None:
    print("You can travel: ", end="")

    one_done_already = False
    for direction in available_directions:
        if one_done_already:
            print(" or ", end="")

        if direction == NORTH:
            print("(N)orth", end="")
        elif direction == EAST:
            print("(E)ast", end="")
        elif direction == SOUTH:
            print("(S)outh", end="")
        elif direction == WEST:
            print("(W)est", end="")

        one_done_already = True

    print(".")


# Alternatively:
# def print_directions(available_directions: list) -> None:
#     options = " or ".join(available_directions)
#     print(f"You can travel: {options}.")


def play_one_move(col, row, valid_directions):
    """Plays one move of the game.

    Returns whether victory has been obtained, and updated col, row.
    """

    direction = input("Direction: ")
    direction = direction.lower()

    if direction in valid_directions:
        col, row = move(direction, col, row)
    else:
        print("Not a valid direction!")

    return col, row


def move(direction, col, row):
    """Returns updated col, row given the direction."""

    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return (col, row)


if __name__ == "__main__":
    main()
