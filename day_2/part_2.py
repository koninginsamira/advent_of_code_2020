from day_2.functions import extract_passwords

PASSWORD_REGEX = "(\\d+)-(\\d+) (.): (.+)"


def main():
    passwords = extract_passwords()
    valid_counter = count_valid_passwords(passwords)

    print(valid_counter)


def count_valid_passwords(passwords):
    valid_counter = 0
    for password in passwords:
        first_index_matches = get_character(password.password, password.min_length - 1) == password.required_symbol
        second_index_matches = get_character(password.password, password.max_length - 1) == password.required_symbol
        something_matches = first_index_matches or second_index_matches
        everything_matches = first_index_matches and second_index_matches

        if something_matches and not everything_matches:
            valid_counter += 1
    return valid_counter


def get_character(string, index, placeholder=None):
    try:
        character = string[index]
    except IndexError:
        character = placeholder

    return character


if __name__ == "__main__":
    main()
