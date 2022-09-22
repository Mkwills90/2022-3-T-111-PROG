COUNTRIES_OF_THE_WORLD = "countries.txt"
INPUT_PROMPT = "Enter a suffix for a country: "


def main():
    country_suffix = input(INPUT_PROMPT)
    file_object = open_file(COUNTRIES_OF_THE_WORLD)

    display_countries(file_object, country_suffix)

    file_object.close()


def open_file(file_name):
    return open(file_name, "r")


def display_countries(file_object, suffix):
    count = 0
    for line in file_object:
        country = line.strip()
        if country.endswith(suffix):
            print(country)
            count += 1

    print(f"{count} countries with suffix '{suffix}'.")


# You'll often see the following two lines at the bottom of python files.
# This is a good way of setting up the program.
# It checks if this file is being run as the main program.
#
# Python modules have a special attribute called __name__,
# which indicates whether the file is being run as the main program,
# or being imported into another module.
#
# If it is being run, then its __name__ attribute will be "__main__".
# But if it is being imported, it's __name__ will be the name of the .py file.
#
# In case it is being imported, we don't want to run any functions, just import their names.
# But if it is being run, then we call the main() function to start the program.
if __name__ == "__main__":
    main()
