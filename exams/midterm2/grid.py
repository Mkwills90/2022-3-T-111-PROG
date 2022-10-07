# Constants to be used in the implementation
DIM = 5
POSITION = 'o'
EMPTY = 'x'
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'
QUIT = 'q'

def main():
    """The main program explains itself!"""

    grid = initialize_grid()
    row, col = (0,0)
    display_grid(grid)
    move = get_move()

    while move != QUIT:
        row, col = make_move(grid, move, row, col)
        display_grid(grid)
        move = get_move()    


def initialize_grid():
    """Returns an initialized grid (a nested list) for the given dimension."""
    
    grid = []
    for _ in range(DIM):
        sublist = []
        for _ in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)

    grid[0][0] = POSITION  # Current position
    return grid


def display_grid(grid):
    """Displays the grid."""

    for i in range(DIM):
        for j in range(DIM):
            print(grid[i][j], end=' ')
        print()
    print()


def get_move():
    """Returns a move corresponding to the user input direction."""
    
    move = input('Move: ')
    if move not in [LEFT, RIGHT, UP, DOWN]:
        return QUIT
    else:
        return move


def make_move(grid, move, row, col):
    """Makes the given move in the given grid.
    
    Returns new row, col as a tuple.
    """

    grid[row][col] = EMPTY
    row, col = find_new_position(move, row, col)
    grid[row][col] = POSITION
    return (row, col)


def find_new_position(move, row, col):
    """Returns the new row, col given the move and the current row, col."""
    
    def decrease(value):
        value = value - 1 if value > 0 else DIM - 1
        return value
    
    def increase(value):
        value = value + 1 if value < DIM - 1 else 0
        return value
    
    if move == LEFT:
        col = decrease(col)  
    elif move == RIGHT:
        col = increase(col)
    elif move == UP:
        row = decrease(row)
    elif move == DOWN:
        row = increase(row)
    
    return row, col    


if __name__ == "__main__":
    main()