def main():
    forms = extract_forms("forms.txt")
    answer_counts = get_answer_counts(forms)

    sum_of_answers_per_group = calculate_sum_of_total_answers_in_group(answer_counts)
    print("The total of positive answers: " + str(sum_of_answers_per_group))

    sum_of_answers_from_entire_group = calculate_sum_of_answers_from_entire_group(answer_counts)
    print("The total of positive answers from everyone in a group is: " + str(sum_of_answers_from_entire_group))


def extract_forms(file_path):
    with open(file_path) as file:
        groups = [group for group in file.read().rstrip().split("\n\n")]
        forms = [group.split("\n") for group in groups]
    return forms


def calculate_sum_of_answers_from_entire_group(answer_counts):
    sum_of_answers = 0
    for group in answer_counts:
        group_size = len(group)
        total_answer_counts = calculate_total_answer_counts_in_group(group)
        for answer_count in total_answer_counts.values():
            if answer_count == group_size:
                sum_of_answers += 1
    return sum_of_answers


def calculate_sum_of_total_answers_in_group(answer_counts):
    sum_of_total_answers = 0
    for group in answer_counts:
        sum_of_total_answers += len(calculate_total_answer_counts_in_group(group))
    return sum_of_total_answers


def calculate_total_answer_counts_in_group(group):
    total_answer_counts = {}
    for form in group:
        for answer, count in form.items():
            if answer in total_answer_counts:
                total_answer_counts[answer] += count
            else:
                total_answer_counts[answer] = count
    return total_answer_counts


def get_answer_counts(forms):
    answer_counts = []
    for group in forms:
        answer_counts.append(count_group_answers(group))
    return answer_counts


def count_group_answers(group):
    group_answer_count = []
    for form in group:
        answer_count = {}
        for answer in form:
            if answer in answer_count:
                answer_count[answer] += 1
            else:
                answer_count[answer] = 1
        group_answer_count.append(answer_count)
    return group_answer_count


if __name__ == "__main__":
    main()
