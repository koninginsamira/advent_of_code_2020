import math

TREE_SYMBOL = '#'


def main():
    with open("map.txt") as file:
        slope = [[char for char in line] for line in file.readlines()]

    tree_counts = [
        count_trees(slope, 1, 1),
        count_trees(slope, 3, 1),
        count_trees(slope, 5, 1),
        count_trees(slope, 7, 1),
        count_trees(slope, 1, 2)
    ]

    print(math.prod(tree_counts))


def count_trees(slope, h_step_size, v_step_size):
    tree_counter = 0
    slope_height = len(slope)
    slope_width = (len(slope[0]) - 1)
    v_pos = 0 + v_step_size
    h_pos = 0 + h_step_size
    while v_pos < slope_height:
        if slope[v_pos][h_pos % slope_width] == TREE_SYMBOL:
            tree_counter += 1

        v_pos += v_step_size
        h_pos += h_step_size
    return tree_counter


if __name__ == "__main__":
    main()
