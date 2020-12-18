from functools import reduce


def composite_function(*func):
    def compose(f, g):
        return lambda x: g(f(x))

    return reduce(compose, func, lambda x: x)


def read_data():
    with open('data.txt') as f:
        return f.read()


def parse_data(data):
    return data.split('\n')


def traverse_hill(data):
    x_pos = 3
    tree_count = 0
    if data[0][0] == '#':
        tree_count += 1
    for i in range(1, len(data)):
        if data[i][x_pos] == '#':
            tree_count += 1
        x_pos = (x_pos + 3) % len(data[i])
    return tree_count


def traverse_hill_with_slope(data, x_slope, y_slope):
    tree_count = 0
    x_pos = 0
    for i in range(0, len(data), y_slope):
        if data[i][x_pos] == '#':
            tree_count += 1
        x_pos = (x_pos + x_slope) % len(data[0])
    return tree_count


def traverse_hill_multiple_slopes(data):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    total = 1
    for slope in slopes:
        count = traverse_hill_with_slope(data, slope[0], slope[1])
        total *= count
    return total


advent_part_1 = composite_function(
    parse_data,
    traverse_hill,
    print
)

advent_part_2 = composite_function(
    parse_data,
    traverse_hill_multiple_slopes,
    print
)

advent_part_1(read_data())

advent_part_2(read_data())
