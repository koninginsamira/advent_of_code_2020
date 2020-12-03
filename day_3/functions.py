def extract_slope():
    with open("map.txt") as file:
        slope = [[char for char in line] for line in file.readlines()]
    return slope
