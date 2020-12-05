def xstr(data):
    if data is None:
        return "undefined"
    return str(data)


def is_integer(string):
    try:
        int(string)
    except ValueError:
        return False
    return True


def is_in_range(number, min_number, max_number):
    if min_number <= number <= max_number:
        return True
    else:
        return False


def is_accepted(value, *, required):
    if required:
        if value:
            return True
        else:
            return False
    else:
        return True
