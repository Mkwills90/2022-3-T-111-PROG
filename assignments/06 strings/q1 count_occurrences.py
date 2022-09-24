a_str = input("Input a string: ")
char_to_count = input("Input a character to count: ")

index = 0
for char_in_str in a_str:
    if char_in_str == char_to_count:
        print(index)
    index += 1
