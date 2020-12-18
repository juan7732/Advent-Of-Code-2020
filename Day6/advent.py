from functools import reduce


def composite_function(*func):
    def compose(f, g):
        return lambda x: g(f(x))

    return reduce(compose, func, lambda x: x)


def read_data():
    with open('data.txt') as f:
        return f.read()


def parse_data(data):
    tmp = data.split('\n\n')
    for i in range(0, len(tmp)):
        tmp[i] = tmp[i].replace('\n', ' ')
    return tmp


def convert_to_question_count(data):
    count_list = []
    for group in data:
        string_without_whitespace = group.replace(' ', '')
        count_list.append(len(set(string_without_whitespace)))
    return count_list


def convert_to_unique_question_count(groups):
    count_list = []
    for group in groups:
        individuals = group.split()
        for i in range(0, len(individuals)):
            individuals[i] = set(individuals[i])
        count_list.append(len(reduce(lambda x, y: x.intersection(y), individuals)))
    return count_list


advent_part_1 = composite_function(
    parse_data,
    convert_to_question_count,
    sum,
    print
)

advent_part_2 = composite_function(
    parse_data,
    convert_to_unique_question_count,
    sum,
    print
)

advent_part_1(read_data())
advent_part_2(read_data())
