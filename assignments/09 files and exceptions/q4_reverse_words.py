def main():
    file_name = input("Enter the filename: ")

    file_obj = open_file(file_name)
    if file_obj is None:
        print(f"File {file_name} not found.")
    else:
        print_reversed_words(file_obj)

        file_obj.close()


def open_file(file_name):
    try:
        return open(file_name, "r")
    except FileNotFoundError:
        return None


def print_reversed_words(file):
    for line in file:
        line = line.strip()

        for word in line.split():
            print(word[::-1], end=" ")

        print()


if __name__ == "__main__":
    main()
