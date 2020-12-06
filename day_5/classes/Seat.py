from operator import attrgetter


def extract_seats(file_path):
    with open(file_path) as file:
        file = file.readlines()
        boarding_passes = [[position_char for position_char in boarding_pass.strip("\n")] for boarding_pass in file]

    seats = []
    for boarding_pass in boarding_passes:
        seat = import_list(boarding_pass)
        seats.append(seat)
    return seats


def import_list(boarding_pass):
    seat = find_seat(boarding_pass)
    seat_row = seat[0]
    seat_column = seat[1]
    seat_id = (seat_row * 8) + seat_column

    return Seat(seat_id, seat_row, seat_column)


def find_seat(boarding_pass):
    possible_rows = [*range(128)]
    possible_columns = [*range(8)]
    bp_index = 0
    seat_is_found = False
    while not seat_is_found:
        position_char = boarding_pass[bp_index]
        middle_row = int(len(possible_rows) / 2)
        middle_column = int(len(possible_columns) / 2)

        if position_char == 'F':
            possible_rows = possible_rows[:middle_row]
        elif position_char == 'B':
            possible_rows = possible_rows[middle_row:]
        elif position_char == 'L':
            possible_columns = possible_columns[:middle_column]
        elif position_char == 'R':
            possible_columns = possible_columns[middle_column:]

        bp_index += 1
        seat_is_found = len(possible_rows) == 1 and len(possible_columns) == 1

    seat = [possible_rows[0], possible_columns[0]]
    return seat


def find_highest_seat(seats):
    return max(seats, key=attrgetter("id"))


def find_missing_seat(seats):
    seats_sorted = sorted(seats, key=lambda s: getattr(s, "id"))
    previous_seat = seats_sorted[0]
    for seat in seats_sorted[1:]:
        if not previous_seat.id == seat.id - 1:
            return seat.id - 1
        previous_seat = seat
    return None


class Seat:
    def __init__(self, seat_id, row, column):
        self.id = seat_id
        self.row = row
        self.column = column

    def __str__(self):
        return "This seat has ID: " + str(self.id) + ", " +\
               "and can be found at row " + str(self.row) + " and column " + str(self.column) + "."
