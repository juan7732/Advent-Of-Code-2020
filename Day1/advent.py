from functools import reduce
from operator import mul


def composite_function(*func):
    def compose(f, g):
        return lambda x: g(f(x))

    return reduce(compose, func, lambda x: x)


def read_data():
    with open('data.txt') as f:
        return f.read()


def prepare_data(data):
    return [int(number) for number in data.split('\n')]


def find_two_numbers_that_make_sum(numbers):
    length = len(numbers)

    for i in range(0, length):
        for j in range(i, length):
            if numbers[i] + numbers[j] == 2020:
                return [numbers[i], numbers[j]]


def find_three_numbers_that_make_sum(numbers):
    length = len(numbers)

    for i in range(0, length):
        for j in range(i, length):
            for k in range(j, length):
                if sum([numbers[i], numbers[j], numbers[k]]) == 2020:
                    return [numbers[i], numbers[j], numbers[k]]


def find_product(numbers):
    return reduce(mul, numbers)


advent_part_1 = composite_function(
    prepare_data,
    find_two_numbers_that_make_sum,
    find_product,
    print
)

advent_part_2 = composite_function(
    prepare_data,
    find_three_numbers_that_make_sum,
    find_product,
    print
)

advent_part_1(read_data())

advent_part_2(read_data())
