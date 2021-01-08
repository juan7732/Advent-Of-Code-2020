from functools import reduce


def composite_function(*func):
    def compose(f, g):
        return lambda x: g(f(x))

    return reduce(compose, func, lambda x: x)


def read_data():
    with open('data.txt') as f:
        return f.read()


def parse_data(data: str):
    return sorted([int(joltage_rating) for joltage_rating in data.split('\n')])


def connect_joltage_adapters(joltage_adapters: list):
    difference_count = {0: 0, 1: 0, 2: 0, 3: 0}
    joltage_adapters.insert(0, 0)
    for i in range(0, len(joltage_adapters) - 1):
        difference = joltage_adapters[i + 1] - joltage_adapters[i]
        difference_count[difference] += 1
    difference_count[3] += 1
    return difference_count[1] * difference_count[3]


# if no more elements, stop looking increment count
# if no step can be reached, go to next number, if number > 3, stop looking
# if the next increment doesn't exist, increase the increment
# if the increment exists, increase the index, and increase the increment
# too time complex, 3^n
def count_all_possible_configurations_recursively(joltage_adapters: list):
    possible_combinations = []
    joltage_adapters.insert(0, 0)

    def generate_possible_combinations(cur: int, tmp_combination: list):
        if cur == len(joltage_adapters) - 1:
            possible_combinations.append(1)
        if cur + 1 < len(joltage_adapters) and joltage_adapters[cur + 1] - joltage_adapters[cur] < 4:
            generate_possible_combinations(cur + 1, tmp_combination)
        if cur + 2 < len(joltage_adapters) and joltage_adapters[cur + 2] - joltage_adapters[cur] < 4:
            generate_possible_combinations(cur + 2, tmp_combination)
        if cur + 3 < len(joltage_adapters) and joltage_adapters[cur + 3] - joltage_adapters[cur] < 4:
            generate_possible_combinations(cur + 3, tmp_combination)

    generate_possible_combinations(0, [0])
    return len(possible_combinations)


def count_all_possible_configurations_dynamically(joltage_adapters: list):
    joltage_adapters.insert(0, 0)
    count_list = {0: 1}
    options = [1, 2, 3]
    for i in range(0, len(joltage_adapters)):
        target = joltage_adapters[i]
        differences = [target - x for x in options]
        for difference in differences:
            if difference >= 0:
                if difference in count_list:
                    if joltage_adapters[i] not in count_list:
                        count_list[joltage_adapters[i]] = 0
                    count_list[joltage_adapters[i]] += count_list[difference]
    return max(count_list.values())


advent_part_1 = composite_function(
    parse_data,
    connect_joltage_adapters,
    print
)

advent_part_2 = composite_function(
    parse_data,
    count_all_possible_configurations_dynamically,
    print
)

advent_part_1(read_data())
advent_part_2(read_data())
