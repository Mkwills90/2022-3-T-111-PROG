INPUT_PROMPT = "Enter a word to add to the set: "
QUIT = "q"


def main():
    input_set = set()
    # New feature in Python 3.8, called the walrus operator,
    # allows you to assign a variable and compare it inline.
    while (user_input := input(INPUT_PROMPT)) != QUIT:
        input_set.add(user_input)
        display_set(input_set)


def display_set(inputs: set) -> None:
    print(f"The set now contains the following {len(inputs)} element(s):")
    print(", ".join(sorted(inputs)))


if __name__ == "__main__":
    main()
