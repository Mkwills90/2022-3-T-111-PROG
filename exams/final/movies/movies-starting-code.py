def open_file(filename):
    """Opens the file with the given file name.

    Returns the corresponding file stream, or None if the file cannot be opened.
    """

    try:
        file_stream = open(filename)
        return file_stream
    except FileNotFoundError:
        return None

def read_file(my_file):
    "Reads file and splits it for future use"
    result = {}
    for line in my_file:
        data = line.split(';')
        result[data[0]] = [round(float(num), 2) for num in data[1:]]
    return result

def print_menu():
    """Prints out menu"""
    print("********************************")
    print("1. Movies in alphabetical order")
    print("2. Titles in given year")
    print("3. Modify all ratings")
    print("********************************")


def movie_alphabetical_order(data, prints=True):
    """Prints out the movies in alphabetical order"""
    for key, value in sorted(data.items()):
        print("{:<50}".format(key), end='')
        for num in value:
            print("{:>6.2f}".format(num), end='')
        if prints:
            print("{:>6}".format(num, end=''))
        else:
            print()

def titles_given_year():
    pass

def  modify_ratings():
    pass

def main():
    file_name = input("Enter filename: ")
    file_stream = open_file(file_name)
    print_menu()
    movie_data = read_file(file_stream)
    choice = input("Enter your selection: ")
    if choice =="1":
        movie_alphabetical_order(movie_data)
    elif choice == "2":
        titles_given_year(movie_data)
    elif choice == "3":
        modify_ratings(movie_data)
    
    

# Main program starts here.  Do NOT change the starter code.
if __name__ == "__main__":
    main()