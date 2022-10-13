import string


def main():
    with get_valid_file() as file_object:
        word_list = get_word_list(file_object)

    word_count_dict = count_each_word(word_list)
    frequency_dict = categorize_by_frequency(word_count_dict)
    display_result(frequency_dict)


def get_valid_file():
    """Asks the user for a file name, repeatedly, until a valid name is given.

    Returns the corresponding file, opened in read mode.
    """

    file_name = input("Name of file: ")

    while (file_obj := open_file(file_name)) is None:
        print(f"File {file_name} not found!")
        file_name = input("Name of file: ")

    return file_obj


def open_file(file_name: str):
    """Returns the given file, open, if it exists, but None otherwise."""

    try:
        return open(file_name, "r")
    except FileNotFoundError:
        return None


def get_word_list(file_object) -> list:
    """Returns a list of the words found in the file associated with the file object.

    The words are transformed to lower case and punctuation is stripped off the end of the word.
    """

    word_list = []
    for line in file_object:
        for word in line.split():
            bare_word = word.strip(string.punctuation)
            word_list.append(bare_word.lower())
    return word_list


def count_each_word(word_list: list) -> dict:
    """Makes a dictionary of word counts from the given word list."""

    word_counts = {}

    for word in word_list:
        if word not in word_counts:
            word_counts[word] = 0

        word_counts[word] += 1

    return word_counts


def categorize_by_frequency(word_count_dict: dict) -> dict:
    """Groups words by their frequency.

    All words that appear exactly once are listed together,
    all words that appear exactly twice are listed together, etc.
    """

    frequency_dict = {}

    for word in word_count_dict:
        count = word_count_dict[word]
        if count not in frequency_dict:
            frequency_dict[count] = []

        frequency_dict[count].append(word)

    return frequency_dict


def display_result(frequency_dict: dict) -> None:
    """Prints the words of each count, most frequent first."""

    for frequency in sorted(frequency_dict, reverse=True):
        words = frequency_dict[frequency]
        if len(words) == 1:
            print(f"There's only 1 word that appears {frequency} times:")
        else:
            print(f"There are {len(words)} words that appear {frequency} times:")

        print(f" {', '.join(words)}")


if __name__ == "__main__":
    main()
