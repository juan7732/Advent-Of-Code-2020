from functools import reduce
import re


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


def validate_passport(passport):
    req_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    opt_keys = ['cid']
    for req_key in req_keys:
        if req_key in passport.keys():
            pass
        else:
            return False
    return True


def validate_passport_complex(passport):
    req_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for req_key in req_keys:
        if req_key not in passport.keys():
            return False
    if re.search('(19[2-9][0-9]|200[1-2])', passport['byr']) is None:
        return False
    if re.search('(201[0-9]|2020)', passport['iyr']) is None:
        return False
    if re.search('(202[0-9]|2030)', passport['eyr']) is None:
        return False
    if re.search('(59in|6[0-9]in|7[0-6]in|1[5-8][0-9]cm|19[0-3]cm)', passport['hgt']) is None:
        return False
    if re.search('(#[0-f]{6})', passport['hcl']) is None:
        return False
    if re.search('(amb|blu|brn|gry|grn|hzl|oth)', passport['ecl']) is None:
        return False
    if re.search('([0-9]{9})', passport['pid']) is None:
        return False
    return True


def validate_passports(passports):
    valid_passports = 0
    invalid_passports = 0
    for passport in passports:
        passport_dictionary = process_data_to_dict(passport)
        if validate_passport(passport_dictionary):
            valid_passports += 1
        else:
            invalid_passports += 1
    return valid_passports, invalid_passports


def validate_passports_complex(passports):
    valid_passports = 0
    invalid_passports = 0
    for passport in passports:
        passport_dictionary = process_data_to_dict(passport)
        if validate_passport_complex(passport_dictionary):
            valid_passports += 1
        else:
            invalid_passports += 1
    return valid_passports, invalid_passports


def process_data_to_dict(passport):
    passport_kvp = {}
    passport_list = passport.split(' ')
    for passport_element in passport_list:
        kvp = passport_element.split(':')
        passport_kvp[kvp[0]] = kvp[1]
    return passport_kvp


advent_part_1 = composite_function(
    parse_data,
    validate_passports,
    print
)

advent_part_2 = composite_function(
    parse_data,
    validate_passports_complex,
    print
)

advent_part_1(read_data())
advent_part_2(read_data())
