from day_4.classes.Passport import extract_passports


def main():
    passports = extract_passports("passports.txt")
    amount_of_valid_passports = len(passports)

    print(amount_of_valid_passports)


if __name__ == "__main__":
    main()
