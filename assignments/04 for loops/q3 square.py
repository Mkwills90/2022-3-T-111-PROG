size = int(input("How large is the square?: "))

for i in range(size):
    for j in range(size):
        # are we on the top or botton?
        if i == 0 or i == size - 1:
            print("*", end=" ")
        # are we on the sides?
        elif j == 0 or j == size - 1:
            print("*", end=" ")
        # then we are not on the edge
        else:
            print(" ", end=" ")
    # print empty line to force a newline
    print()
