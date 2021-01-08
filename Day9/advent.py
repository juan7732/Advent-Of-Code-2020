from functools import reduce


def composite_function(*func):
    def compose(f, g):
        return lambda x: g(f(x))

    return reduce(compose, func, lambda x: x)


def read_data():
    with open('data.txt') as f:
        return f.read()


def parse_data(data: str):
    return [int(encoding) for encoding in data.split('\n')]


# From Day 1
def do_two_numbers_make_sum(numbers, number):
    length = len(numbers)
    for i in range(0, length):
        for j in range(i, length):
            if numbers[i] + numbers[j] == number:
                return True
    return False


def identify_incorrect_encoding(encoding: list):
    preamble_length = 25
    preamble = encoding[:preamble_length]
    remaining_encoding = encoding[preamble_length:]
    for element in remaining_encoding:
        if do_two_numbers_make_sum(preamble, element):
            preamble.pop(0)
            preamble.append(element)
        else:
            return element


def find_contiguous_sum(encoding: list):
    target = identify_incorrect_encoding(encoding)
    target_index = find_index(encoding, target)
    for i in range(0, target_index):
        ans = try_sum(encoding[i:target_index], target)
        if ans == 0:
            pass
        else:
            return ans


def find_index(num_list: list, number: int):
    for i in range(0, len(num_list)):
        if num_list[i] > number:
            return i


def try_sum(numbers: list, target: int):
    intermediate_sum = 0
    for i in range(0, len(numbers)):
        intermediate_sum += numbers[i]
        if intermediate_sum == target:
            return numbers[:i+1]
        elif intermediate_sum > target:
            return 0
        else:
            pass
    return 0


def find_final_answer(solution_array: list):
    solution_array = sorted(solution_array)
    return solution_array[-1] + solution_array[0]


advent_part_1 = composite_function(
    parse_data,
    identify_incorrect_encoding,
    print
)

advent_part_2 = composite_function(
    parse_data,
    find_contiguous_sum,
    find_final_answer,
    print
)

advent_part_1(read_data())
advent_part_2(read_data())
