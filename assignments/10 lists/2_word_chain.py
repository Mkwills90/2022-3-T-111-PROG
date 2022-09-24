def main():
    all_words = get_words_from_user()
    word_chain = form_chain(all_words)
    display_results(all_words, word_chain)


def get_words_from_user():
    PROMPT = "Enter a word to be added to the list: "

    words = []
    user_input = input(PROMPT)
    while user_input != "x":
        words.append(user_input)
        user_input = input(PROMPT)

    return words


def form_chain(words):
    chain = []
    for word in words:
        add_matching_word_to_chain(word, chain)

    return chain


def add_matching_word_to_chain(new_word, chain):
    try:
        if chain[-1][-1] == new_word[0]:
            # The first letter of the new word
            # matches the last character from the last word of the chain.
            chain.append(new_word)

    except IndexError:
        # There is no last word of chain,
        # because no word has been added to the chain yet.
        chain.append(new_word)


def display_results(input_list, criteria_list):
    print(input_list)
    for item in criteria_list:
        print(item)


if __name__ == "__main__":
    main()
