from day_5.classes.Seat import extract_seats, find_highest_seat, find_missing_seat


def main():
    seats = extract_seats("boarding_passes.txt")

    print("The highest seat ID is: " + str(find_highest_seat(seats).id))

    print("The missing seat ID is: " + str(find_missing_seat(seats)))


if __name__ == "__main__":
    main()
