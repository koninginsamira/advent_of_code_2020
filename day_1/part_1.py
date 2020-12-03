import sys

with open("expenses.txt") as file:
    expenses = {int(expense): True for expense in file.readlines()}

# TODO: Will also succeed on one number if it's 1010 (because it checks itself)
for expense1 in expenses:
    for expense2, could_make_2020 in expenses.items():
        if could_make_2020:
            if expense1 + expense2 == 2020:
                print(expense1 * expense2)
                sys.exit("The answer has been found!")

    expenses[expense1] = False
