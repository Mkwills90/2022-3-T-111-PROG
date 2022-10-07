import string

def main():
    file_name = input("Enter filename: ")
    file_stream = open_file(file_name)
    if file_stream is not None:
        token_list = get_tokens(file_stream)
        print_list(token_list)
        file_stream.close()
    else:
        print(f"File {file_name} not found!")


def open_file(filename):
    """Returns a file stream if filename found, otherwise None."""

    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None


def get_tokens(file_stream):
    """Returns a list of the tokens found in the specified stream."""

    all_tokens = []
    for line in file_stream:
        word_list = line.split()
        all_tokens += extract_punctuation(word_list)
    return all_tokens


def extract_punctuation(word_list):
    """Returns a new list in which 
    punctuation characters, found at the beginning and end of a word, 
    have been extracted and made separate tokens.
    """
    
    token_list = []
    for word in word_list:
        start_index = 0
        # Punctuation character at the start of the word?
        if len(word) > 1 and word[start_index] in string.punctuation:
            token_list.append(word[start_index])
            start_index = 1
        # Punctuation characters at the end of the word?
        token_list += extract_punctuation_from_end(word[start_index:])
        
    return token_list
    
    
def extract_punctuation_from_end(word):
    """Extracts possible punctuation characters 
    from two last characters of the given word and 
    returns a list of 1-3 tokens.
    """
    
    token_list = []
    if len(word) > 1 and word[-1] in string.punctuation:  
        if word[-2] in string.punctuation:
            token_list.append(word[:-2])    # the word
            token_list.append(word[-2])     # next to last punctuation char
        else:
            token_list.append(word[:-1])    # the word
        token_list.append(word[-1])         # last punctuation char
    else:
        token_list.append(word)             # the word unchanged

    return token_list  


def print_list(token_list):
    """Prints each token from the given list in a separate line."""

    for token in token_list:
        print(token)

if __name__ == "__main__":
    main()