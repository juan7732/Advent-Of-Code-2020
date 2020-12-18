from functools import reduce


def composite_function(*func):
    def compose(f, g):
        return lambda x: g(f(x))

    return reduce(compose, func, lambda x: x)


def read_data():
    with open('data.txt') as f:
        return f.read()


def parse_data(data):
    tmp = data.split('\n')
    for i in range(0, len(tmp)):
        tmp[i] = tmp[i].replace('B', '1')
        tmp[i] = tmp[i].replace('F', '0')
        tmp[i] = tmp[i].replace('R', '1')
        tmp[i] = tmp[i].replace('L', '0')
    return tmp


def get_max(seats):
    seat_id = 0
    for seat in seats:
        if seat[2] > seat_id:
            seat_id = seat[2]
    return seat_id


def sort_seat_data(seats):
    return sorted(seats, key=lambda x: x[2])


def find_missing_seats(seats):
    missing_seats = []
    just_ids = list(map(lambda x: x[2], seats))
    for i in range(0, 1024):
        if i not in just_ids:
            missing_seats.append(i)
    for missing_seat in missing_seats:
        if (missing_seat - 1) not in missing_seats and (missing_seat + 1) not in missing_seats:
            return missing_seat


def get_seat_data(seat_info):
    seat_info_list = []
    for seat in seat_info:
        seat_row = int(seat[0:7], 2)
        seat_col = int(seat[7:], 2)
        seat_info_list.append([seat_row, seat_col, (seat_row * 8) + seat_col])
    return seat_info_list


advent_part_1 = composite_function(
    parse_data,
    get_seat_data,
    get_max,
    print
)

advent_part_2 = composite_function(
    parse_data,
    get_seat_data,
    sort_seat_data,
    find_missing_seats,
    print
)

advent_part_1(read_data())
advent_part_2(read_data())