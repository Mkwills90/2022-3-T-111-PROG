import string


def main():
    # Your are NOT allowed to change this main function
    filename = input("Enter name of file: ")
    file_object = open_file(filename)
    if file_object is not None:
        scrambled_word_list = scramble_file_content(file_object)
        print_word_list(scrambled_word_list)
        file_object.close()
    else:
        print(f"File {filename} not found!")


def open_file(filename):
  """Opens the given file, returning its file object if found, otherwise None."""

  try:
    file_object = open(filename, 'r')
    return file_object
  except FileNotFoundError:
    return None


def scramble_file_content(fileobject):
    """Returns a list of scrambled version of the words found in the given file."""
    
    scrambled_word_list = []
    for word in fileobject: # We assume that the file contains a single word in each line
        word = word.strip() # remove the carriage return
        scrambled_word = scramble(word)
        scrambled_word_list.append(scrambled_word)
    
    return scrambled_word_list


def scramble(word):
    """Returns a scrambled version of the given word."""

    if len(word) <= 3:
        return word

    # A punctuation character is left untouched
    last_index = -1
    if word[last_index] in string.punctuation:
        last_index -= 1

    sequence = word[1:last_index]   # excluding the first and last letters
    scrambled_sequence = swap_adjacent(sequence)
    scrambled_word = word[0] + scrambled_sequence + word[last_index:]
    
    return scrambled_word


def swap_adjacent(sequence):
    """Returns a scrambled version of the given sequence, in which adjacent characters
    of the original sequence have been swapped."""

    odd = False
    length = len(sequence)
    if length % 2 != 0:     # odd number of characters in sequence
        length -= 1
        odd = True

    scrambled_sequence = ''
    for i in range(0,length,2):
        scrambled_sequence += sequence[i+1] + sequence[i]
    if odd:
        scrambled_sequence += sequence[-1]  # Add the last letter of the sequence

    return scrambled_sequence


def print_word_list(word_list):
    """Prints each word in the given word_list, with a space after each word."""

    for word in word_list:
        print(word, end=' ')


if __name__ == "__main__":
    main()