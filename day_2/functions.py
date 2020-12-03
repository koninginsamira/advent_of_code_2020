import re

from day_2.classes import Password

PASSWORD_REGEX = "(\\d+)-(\\d+) (.): (.+)"


def extract_passwords():
    passwords = []
    with open("passwords.txt") as file:
        for line in file.readlines():
            password = Password()
            matched_line = re.match(PASSWORD_REGEX, line)

            password.import_match(matched_line.groups())
            passwords.append(password)
    return passwords
