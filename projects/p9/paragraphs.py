import string
import operator

def main():
    """The main program retrieves the data and prints the requested information."""

    filename = input("Enter filename: ")
    file_stream = open_file(filename)
    if file_stream is not None:
        with file_stream:
            all_paragraphs = get_words_in_paragraphs(file_stream)

        par_index = convert_to_paragraph_index(all_paragraphs)
        print_index(par_index)

        word_counts = convert_to_word_counts(all_paragraphs)
        print_top_highest(10, word_counts)
        print_top_highest(20, word_counts)
    else:
        print("Filename {} not found!".format(filename))


def open_file(filename):
    """Returns a file stream if filename is found, otherwise None."""

    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None


def get_words_in_paragraphs(file_stream):
    """Returns the data from the given file stream as a list of list of words.

    The first inner list contains the words found on the first paragraph,
    the second inner list contains the words foud on the second paragraph, etc.
    Punctuations at the beginning and end of words are stripped.
    """

    all_paragraphs = [] # List of list of words
    current_paragraph = [] # List of words
    for line_str in file_stream:
        if line_str == '\n':  # Emtpy line between paragraphs
            all_paragraphs.append(current_paragraph)
            current_paragraph = []
        else:
            words = get_words_from_line(line_str)
            current_paragraph += words
        
    return all_paragraphs


def get_words_from_line(line_str):
    """Gets the words appearing in line, 
    stripping out punctuations, and converting to lower case.
    """

    words = []
    word_list = line_str.strip().split()
    for word in word_list:
        word = word.strip(string.punctuation)
        word = word.lower()
        words.append(word)

    return words


def convert_to_paragraph_index(all_paragraphs):
    """All_paragraphs is a list of list of words.
    Each sublist contains the words found in the corresponding paragraph.
    
    Returns a dictionary of sets.
    The key is a word, the value is the set of paragraphs in which the word occured.
    """

    paragraph_index = {}
    for idx, word_list in enumerate(all_paragraphs):
        for word in word_list:
            if word not in paragraph_index:
                paragraph_index[word] = set()

            paragraph_index[word].add(idx+1)
    
    return paragraph_index


def convert_to_word_counts(all_paragraphs):
    """All_paragraphs is a list of list of words.
    Each sublist contains the words found in the corresponding paragraph.
    
    Returns a dictionary of counts.
    The key is a word, the value is the total count of the words in all paragraphs.
    """

    word_counts = {}
    for word_list in all_paragraphs:
        for word in word_list:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1 
    return word_counts


def print_index(index):
    """Prints the index in a sorted manner."""

    print()
    print('The paragraph index: ')
    for term in sorted(index):
        print(term, end=' ')
        paragraph_set = index[term]
        sorted_paragraph_numbers_to_str = [str(paragraph) for paragraph in sorted(paragraph_set)]
        print(", ".join(sorted_paragraph_numbers_to_str))


def print_top_highest(top, word_counts):
    """Prints the top highest word counts."""

    print()
    print(f'The highest {top} counts: ')
    sorted_on_words = sorted(word_counts.items()) 
    sorted_on_counts = sorted(sorted_on_words, key=operator.itemgetter(1),reverse=True)
    top_counts = sorted_on_counts[:top]
    for word, count in top_counts:
        print(f'{word}: {count}')


if __name__ == "__main__":
    main()