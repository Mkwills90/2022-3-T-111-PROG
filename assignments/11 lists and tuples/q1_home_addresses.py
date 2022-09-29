def main():
    home_addresses = get_home_addresses()
    print(home_addresses)
    street_and_number = get_tuple_from_home_addresses(home_addresses)
    print(street_and_number)


def get_home_addresses():
    PROMPT = "Home address: "
    home_addresses = []

    home_address = input(PROMPT)
    while home_address.lower() != "q":
        home_addresses.append(home_address)
        home_address = input(PROMPT)

    return home_addresses


def get_tuple_from_home_addresses(home_addresses):
    street_and_number = []
    for address in home_addresses:
        street_and_number.append(tuple(address.split()))
    return street_and_number


if __name__ == "__main__":
    main()
