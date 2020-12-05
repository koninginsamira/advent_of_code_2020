from day_4.classes.Data import is_integer, is_in_range
from day_4.exceptions.InvalidValue import InvalidValue


def check_year(year, min_year=None, max_year=None):
    if is_integer(year):
        year = int(year)
    else:
        raise ValueError("An issue year must consist of four digits.")

    if not is_in_range(year, min_year, max_year):
        raise InvalidValue(
            "The provided year can be at least " + str(min_year) + " and at most " + str(max_year) + ".")

    return year
