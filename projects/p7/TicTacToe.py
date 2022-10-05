NO_WINNER = -1
PLAYER_O = 0
PLAYER_X = 1
CHAR_O = 'O' 
CHAR_X = 'X'

def main():
    """Initializes the game board and runs the game loop."""

    dim = int(input("Input dimension of the board: "))
    board = init_board(dim)
    display_board(board, dim)

    player = PLAYER_X
    while not game_over(board, dim):
        make_move(board, dim, player)
        display_board(board, dim)
        player = switch_player(player)

    winner = get_winner(board, dim)   
    display_result(winner)


def init_board(dim):
    """Returns an initialized board for the given dimension."""
    
    board = []
    pos = 1

    for _ in range(dim):
        sublist = []
        for _ in range(dim):
            sublist.append(str(pos))
            pos += 1
        board.append(sublist)
    
    return board


def display_board(board, dim):
    """Displays the board."""

    for row in range(dim):
        for col in range(dim):
            #print("{:>5}".format(board[row][col]), end='')
            print(f"{board[row][col]:>5}", end='')
        print()


def game_over(board, dim):
    """Returns True if the game is over, otherwise False."""
    winner = get_winner(board, dim)
    return winner != NO_WINNER or is_board_filled(board, dim)
        

def is_board_filled(board, dim):
    """Returns True if all squares of the board have been filled, 
    otherwise False.
    """

    for row in range(dim):
        for col in range(dim):
            if board[row][col] != CHAR_X and board[row][col] != CHAR_O:
                return False
    return True


def make_move(board, dim, player):
    """Makes a move on the given board of the given dimension 
    for the given player.
    """

    symbol = get_symbol_for_player(player)

    pos = get_pos_input(symbol)
    while not is_legal_move(pos, board, dim):
        print("Illegal move!")
        pos = get_pos_input(symbol)
    
    row, col = pos_to_row_col(int(pos), dim)
    board[row][col] = symbol


def get_symbol_for_player(player):
    """Returns the appropriate symbol for the given player."""

    return CHAR_X if player == PLAYER_X else CHAR_O


def get_pos_input(symbol):
    """Returns an input position entered by player."""

    return input(symbol + " position: ")


def is_legal_move(pos, board, dim):
    """Returns True if the given move in pos is legal on the board, otherwise False."""

    if not pos.isdigit():
        return False
    
    pos = int(pos)
    if pos < 1 or pos > dim**2:  # Outside board?
        return False
    
    row, col = pos_to_row_col(pos, dim)
    # Square already occupied?
    if board[row][col] == CHAR_X or board[row][col] == CHAR_O:
        return False
    
    return True


def pos_to_row_col(pos, dim):
    """Returns the (col, row) of the given dimension associated with the given integer position."""

    row = (pos-1) // dim
    col = (pos-1) % dim
    return (row, col)


def get_winner(board, dim):
    """Returns the winner for the given board if found, else NO_WINNER."""

    # First check for winner in rows
    for row in range(dim):
        winner = check_winner_in_row(board, dim, row)
        if winner != NO_WINNER: 
            return winner

    # Then check for winner in columns
    for col in range(dim):
        winner = check_winner_in_column(board, dim, col)
        if winner != NO_WINNER: 
            return winner

    # Finally, check the diagonals,
    winner = check_diagonals(board, dim)
    return winner


def check_winner_in_row(board, dim, row):
    """Checks for and returns a winner for the given row."""

    numO = 0
    numX = 0

    for col in range(dim):
        numO, numX = increase_num_Os_Xs(board, row, col, numO, numX)

    return interpret_result(numO, numX, dim)


def increase_num_Os_Xs(board, row, col, numO, numX):
    """Increases number of O's or X's."""

    if board[row][col] == CHAR_O:
        numO += 1
    elif board[row][col] == CHAR_X:
        numX += 1
    
    return (numO, numX)


def interpret_result(numO, numX, dim):
    """Returns the winner given the number of O's and X's for the given dimension."""

    if numO == dim:
        return PLAYER_O
    elif numX == dim:
        return PLAYER_X
    else:
        return NO_WINNER


def check_winner_in_column(board, dim, col):
    """Checks for and returns a winner for the given column."""

    numO = 0
    numX = 0

    for row in range(dim):
        numO, numX = increase_num_Os_Xs(board, row, col, numO, numX)

    return interpret_result(numO, numX, dim)


def check_diagonals(board, dim):
    """Checks for and returns a winner in the two diagonals."""

    numO = 0
    numX = 0
    col = 0

    # From top left to bottom right
    for row in range(dim):
        numO, numX = increase_num_Os_Xs(board, row, col, numO, numX)
        col += 1

    winner =  interpret_result(numO, numX, dim)

    # From top right to bottom left
    if (winner == NO_WINNER):
        numO = 0
        numX = 0
        col = dim-1

        for row in range(dim):
            numO, numX = increase_num_Os_Xs(board, row, col, numO, numX)
            col -= 1
        
        winner = interpret_result(numO, numX, dim)

    return winner


def switch_player(player):
    return PLAYER_O if player == PLAYER_X else PLAYER_X


def display_result(winner):
    """Prints out the result of the game."""

    if winner == NO_WINNER:
        print("Draw!")
    elif winner == PLAYER_O:
        print("Winner is: " + CHAR_O)
    else:
        print("Winner is: " + CHAR_X)
        

if __name__ == "__main__":
    main()
