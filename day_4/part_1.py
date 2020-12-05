from day_4.classes.Passport import import_block
from day_4.exceptions.MissingRequiredField import MissingRequiredField


def main():
    passports = extract_passports("passports.txt")
    amount_of_valid_passports = len(passports)

    print(amount_of_valid_passports)


def extract_passports(file_path):
    with open(file_path) as file:
        passports = []
        passport_blocks = file.read().split("\n\n")
        for passport_block in passport_blocks:
            passport_block = passport_block.replace("\n", " ")

            try:
                passport = import_block(passport_block)
                passports.append(passport)
            except MissingRequiredField:
                pass
    return passports


if __name__ == "__main__":
    main()
