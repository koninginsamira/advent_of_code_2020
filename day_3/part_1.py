from day_3.functions import extract_slope

TREE_SYMBOL = '#'
H_STEP_SIZE = 3
V_STEP_SIZE = 1


def main():
    slope = extract_slope()

    tree_count = count_trees(slope)

    print(tree_count)


def count_trees(slope):
    tree_counter = 0
    slope_height = len(slope)
    slope_width = (len(slope[0]) - V_STEP_SIZE)
    v_pos = 0 + V_STEP_SIZE
    h_pos = 0 + H_STEP_SIZE
    while v_pos < slope_height:
        if slope[v_pos][h_pos % slope_width] == TREE_SYMBOL:
            tree_counter += 1

        v_pos += V_STEP_SIZE
        h_pos += H_STEP_SIZE
    return tree_counter


if __name__ == "__main__":
    main()
