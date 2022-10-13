def main():
    dictionary = {}

    add_word(dictionary)
    while more():
        add_word(dictionary)

    display_result(dictionary)


def add_word(dictionary: dict) -> None:
    """Asks the user for a word and definition and stores it in the dictionary."""

    word = input("Enter a word: ")
    dictionary[word] = input(f"Enter the definition for {word}: ")


def more() -> bool:
    """Checks if the user wants to add more words."""

    answer = input("Would you like to add another word and definition (y/n)?: ")
    return answer.lower() != "n"


def display_result(dictionary: dict) -> None:
    """Prints the words in alphabetical order, along with the definitions."""

    for word, definition in sorted(dictionary.items()):
        print(f"\n{word}:\n    {definition}")


# # Alternatively:
# def display_result(dictionary: dict) -> None:
#     """Prints the words in alphabetical order, along with the definitions."""

#     for word in sorted(dictionary):
#         definition = dictionary[word]
#         print(f"\n{word}:\n    {definition}")


if __name__ == "__main__":
    main()
