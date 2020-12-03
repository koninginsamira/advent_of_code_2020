import sys

def main():
    expenses = []
    with open("expenses.txt") as file:
        expenses = [int(line) for line in file.readlines()]

    for expense1 in expenses:
        for expense2 in expenses:
            if expense1 != expense2:
                for expense3 in expenses:
                    if expense1 != expense3 and expense2 != expense3:
                        if expense1 + expense2 + expense3 == 2020:
                            print(expense1 * expense2 * expense3)
                            sys.exit("The answer has been found!")

if __name__ == "__main__":
    main()

