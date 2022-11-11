MIN_PASSWORD_LENGTH = 8
MIN_DIGITS = 3


def main():
    valid_password_list = []
    invalid_password_list = []

    password = input("Enter password: ")
    while password != 'quit':
        valid_password = is_valid_password(password)
        if valid_password:
            print("Password is valid")
            valid_password_list.append(password)
        else:
            print("Password is invalid")
            invalid_password_list.append(password)

        password = input("Enter password: ")
        
    if (len(valid_password_list) > 0):
        print_info_on_passwords("Valid passwords:", valid_password_list)
    if (len(invalid_password_list) > 0):
        print_info_on_passwords("Invalid passwords:", invalid_password_list)


def is_valid_password(password):
    '''Returns True if the password is valid, otherwise False'''
    if len(password) < MIN_PASSWORD_LENGTH:
        return False
    if num_digits(password) < MIN_DIGITS:
        return False
    
    return True


def num_digits(string):
    '''Returns the number of digits in the given string'''
    count = 0
    for ch in string:
        if ch.isdigit():
            count += 1
    return count


def print_info_on_passwords(header, password_list):
    print()
    print(header)
    print_passwords(password_list)

    password_lengths = [len(password) for password in password_list]
    digit_counts = [num_digits(password) for password in password_list]

    print("Average length: {:.1f}".format(average(password_lengths)))
    print("Average # of digits: {:.1f}".format(average(digit_counts)))


def print_passwords(password_list):
    for password in password_list:
        print(password, end=' ')
    print()


def average(number_list):
    '''Returns the average of the numbers in the given list'''
    return sum(number_list) / len(number_list)

# Main program starts here
if __name__ == "__main__":
    main()