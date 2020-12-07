def main():
    with open("forms.txt") as file:
        form_lists = [[answer for answer in form_list.replace("\n", "")] for form_list in file.read().split("\n\n")]

    form_dicts = []
    for form_list in form_lists:
        form_dict = {}
        for answer in form_list:
            if answer not in form_dict:
                form_dict[answer] = form_list.count(answer)
        form_dicts.append(form_dict)

    answers_total = 0
    for form_dict in form_dicts:
        for answer in form_dict.values():
            answers_total += 1

    print(answers_total)


if __name__ == "__main__":
    main()
