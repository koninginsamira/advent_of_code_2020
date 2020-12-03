import re

from day_2.classes import Password

PASSWORD_REGEX = "(\\d+)-(\\d+) (.): (.+)"


def main():
    passwords = []
    with open("passwords.txt") as file:
        for line in file.readlines():
            password = Password()
            matched_line = re.match(PASSWORD_REGEX, line)

            password.import_match(matched_line.groups())
            passwords.append(password)

    valid_counter = 0
    for password in passwords:
        found_symbols = re.findall(password.required_symbol, password.password)
        if password.min_length <= len(found_symbols) <= password.max_length:
            valid_counter += 1

    print(valid_counter)


if __name__ == "__main__":
    main()
