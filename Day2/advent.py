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


def validate_passwords_within_range(password_data):
    return sum(map(validate_rules_within_range, password_data))


def validate_passwords_xor_position(password_data):
    return sum(map(validate_rules_xor_position, password_data))


def validate_rules_within_range(data):
    minimum_count, maximum_count, letter, password = parse_line_data(data)

    character_count = 0
    for character in password:
        if character == letter:
            character_count += 1

    if minimum_count <= character_count <= maximum_count:
        return 1
    else:
        return 0


def validate_rules_xor_position(data):
    first_position, second_position, letter, password = parse_line_data(data)
    first_position -= 1
    second_position -= 1
    if (password[first_position] == letter) ^ (password[second_position] == letter):
        return 1
    else:
        return 0


def parse_line_data(line_data):
    line_data = line_data.split(' ')
    positional_rules = line_data[0].split('-')
    first_position = int(positional_rules[0])
    second_position = int(positional_rules[1])
    letter = line_data[1][0]
    password = line_data[2]

    return first_position, second_position, letter, password


advent_part_1 = composite_function(
    parse_data,
    validate_passwords_within_range,
    print
)

advent_part_2 = composite_function(
    parse_data,
    validate_passwords_xor_position,
    print
)

advent_part_1(read_data())

advent_part_2(read_data())
