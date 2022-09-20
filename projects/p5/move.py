MAX = 10
MIN = 1

def read_position():
    position = int(input("Input a position between " + str(MIN) + " and " + str(MAX) + ": "))
    return position

def display_position(position):
    for i in range(MIN, MAX+1):
        if i == position:
            print('o', end='')
        else:
            print('x', end='')
    print()

def display_instructions():
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")

def read_choice():
    choice = input("Input your choice: ")
    return choice

def get_new_position(position, choice):
    if choice == 'l' and position > MIN:
        position -= 1
    elif choice == 'r' and position < MAX:
        position += 1
    return position

# The main program starts here
position = read_position()
display_position(position)
display_instructions()

choice = 'l'
while choice == 'l' or choice == 'r':
    choice = read_choice()
    position = get_new_position(position, choice)
    display_position(position)