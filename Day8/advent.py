from functools import reduce
from copy import deepcopy


def composite_function(*func):
    def compose(f, g):
        return lambda x: g(f(x))

    return reduce(compose, func, lambda x: x)


def read_data():
    with open('data.txt') as f:
        return f.read()


def parse_data(data: str):
    data = [instruction.split(' ') for instruction in data.split('\n')]
    return data


def emulate(instructions: list):
    accumulator = 0
    program_counter = 0
    past_stack = []
    instructions_executed = []
    while True:
        if program_counter > len(instructions):
            print(f"success + {accumulator}")
            return past_stack
        if program_counter in instructions_executed:
            past_stack.append([program_counter, instructions[program_counter], accumulator])
            return past_stack
        else:
            instructions_executed.append(program_counter)
            past_stack.append([program_counter, instructions[program_counter], accumulator])
            instruction, arg = instructions[program_counter][0], int(instructions[program_counter][1])
            if instruction == 'acc':
                accumulator += arg
                program_counter += 1
            if instruction == 'nop':
                program_counter += 1
            if instruction == 'jmp':
                program_counter += arg


def emulate_and_test(instructions: list):
    accumulator = 0
    program_counter = 0
    past_stack = []
    instructions_executed = []
    while True:
        if program_counter >= len(instructions):
            past_stack.append([program_counter, [], accumulator])
            print(f"success + {accumulator}")
            return past_stack, True
        if program_counter in instructions_executed:
            return past_stack, False
        else:
            instructions_executed.append(program_counter)
            past_stack.append([program_counter, instructions[program_counter], accumulator])
            instruction, arg = instructions[program_counter][0], int(instructions[program_counter][1])
            if instruction == 'acc':
                accumulator += arg
                program_counter += 1
            if instruction == 'nop':
                program_counter += 1
            if instruction == 'jmp':
                program_counter += arg


def modify_instructions_and_emulate(instructions: list):
    original_list = deepcopy(instructions)
    nop_index_list = get_index_list(instructions, 'nop')
    jmp_index_list = get_index_list(instructions, 'jmp')

    for index in nop_index_list:
        new_instructions = deepcopy(original_list)
        new_instructions[index][0] = 'jmp'
        call_stack, is_not_loop = emulate_and_test(new_instructions)
        if is_not_loop:
            return call_stack[-1][2]
    for index in jmp_index_list:
        new_instructions = deepcopy(original_list)
        new_instructions[index][0] = 'nop'
        call_stack, is_not_loop = emulate_and_test(new_instructions)
        if is_not_loop:
            return call_stack[-1][2]


def get_index_list(instructions: list, instruction: str):
    index_list = []
    for i in range(0, len(instructions)):
        if instructions[i][0] == instruction:
            index_list.append(i)
    return index_list


def identify_infinite_loop_accumulator_value(call_stack: list):
    return call_stack[-1][2]


advent_part_1 = composite_function(
    parse_data,
    emulate,
    identify_infinite_loop_accumulator_value,
    print
)

advent_part_2 = composite_function(
    parse_data,
    modify_instructions_and_emulate,
    print
)

advent_part_1(read_data())
advent_part_2(read_data())
