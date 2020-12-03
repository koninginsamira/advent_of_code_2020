import re

from day_2.functions import extract_passwords


def main():
    passwords = extract_passwords()
    valid_counter = count_valid_passwords(passwords)

    print(valid_counter)


def count_valid_passwords(passwords):
    valid_counter = 0
    for password in passwords:
        found_symbols = re.findall(password.required_symbol, password.password)
        if password.min_length <= len(found_symbols) <= password.max_length:
            valid_counter += 1
    return valid_counter


if __name__ == "__main__":
    main()
