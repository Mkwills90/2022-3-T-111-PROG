def extract_first_number_from_string(string_to_search):
    number_string = ""
    last_character_was_digit = False
    for character in string_to_search:
        if character.isdigit():
            number_string += character
            last_character_was_digit = True
        elif last_character_was_digit:
            break

    if number_string:
        return int(number_string)
    else:
        return -1
