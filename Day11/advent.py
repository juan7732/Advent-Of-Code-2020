from functools import reduce
from copy import deepcopy
import time
import subprocess as sp


def composite_function(*func):
    def compose(f, g):
        return lambda x: g(f(x))

    return reduce(compose, func, lambda x: x)


def read_data():
    with open('data.txt') as f:
        return f.read()


def parse_data(data: str):
    game = data.split('\n')
    for row in range(0, len(game)):
        tmp_list = []
        for letter in game[row]:
            tmp_list.append(letter)
        game[row] = tmp_list
    return game


def print_state_life(game_state: list):
    for row in game_state:
        for col in row:
            print(col, end='')
        print()


def tick_game(game_state: list):
    previous_game_state = []
    i = 0
    while previous_game_state != game_state:
        i += 1
        print()
        print(f'Run # {i}')
        print_state_life(game_state)
        time.sleep(.5)
        # only clears in linux terminal
        sp.call('clear', shell=True)
        previous_game_state = deepcopy(game_state)
        game_state = deepcopy(simulate_game(game_state))

    return game_state


def simulate_game(initial_game_state: list):
    new_state = deepcopy(initial_game_state)
    for row in range(0, len(initial_game_state)):
        for column in range(0, len(initial_game_state[row])):
            new_state[row][column] = check_neighbors(initial_game_state, row, column)
    return new_state


def check_neighbors(game_state: list, x_index, y_index):
    current_state = game_state[x_index][y_index]
    if current_state == '.':
        return '.'
    neighbors = get_neighbors(game_state, x_index, y_index)
    if current_state == 'L':
        if '#' not in neighbors:
            return '#'
    if current_state == '#':
        if neighbors.count('#') >= 4:
            return 'L'
    return current_state


def get_neighbors(game_state: list, x_index: int, y_index: int):
    neighbors = []
    top_slice = (y_index - 1, y_index + 1)
    mid_slice = [[x_index, y_index - 1], [x_index, y_index + 1]]
    bottom_slice = (y_index -1, y_index + 1)
    if x_index - 1 >= 0:
        for index in range(top_slice[0], top_slice[1] + 1):
            if 0 <= index < len(game_state[0]):
                neighbors.append(game_state[x_index - 1][index])
    for coord in mid_slice:
        if 0 <= coord[1] < len(game_state[0]):
            neighbors.append(game_state[coord[0]][coord[1]])
    if x_index + 1 < len(game_state):
        for index in range(bottom_slice[0], bottom_slice[1] + 1):
            if 0 <= index < len(game_state[0]):
                neighbors.append(game_state[x_index + 1][index])
    return neighbors


def get_empty_seat_count(game_state):
    count = 0
    for row in game_state:
        for i in range(0, len(row)):
            if row[i] == '#':
                count += 1
    return count


advent_part_1 = composite_function(
    parse_data,
    tick_game,
    get_empty_seat_count,
    print
)

advent_part_1(read_data())