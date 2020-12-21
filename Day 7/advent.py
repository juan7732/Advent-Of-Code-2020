from functools import reduce


def composite_function(*func):
    def compose(f, g):
        return lambda x: g(f(x))

    return reduce(compose, func, lambda x: x)


def read_data():
    with open('data.txt') as f:
        return f.read()


def parse_data(data: str):
    data = data.replace('.', '')
    data = data.replace('bags', '')
    data = data.replace('bag', '')
    return data.split('\n')


def parse_rules(rules: list):
    rule_dict = {}
    for rule in rules:
        kvp = rule.split('contain')
        rule_key, rule_values = kvp[0].strip(), kvp[1]
        if 'no other bags' in rule_values:
            rule_dict[rule_key] = [rule_values.strip()]
        elif ',' in rule_values:
            rule_dict[rule_key] = [rul.strip() for rul in rule_values.split(',')]
        else:
            rule_dict[rule_key] = [rule_values.strip()]
    return rule_dict


def parse_rules_backwards(rules: list):
    rule_dict = {}
    for rule in rules:
        kvp = rule.split('contain')
        rule_keys, rule_value = [r.strip()[2:] for r in kvp[1].split(',')], kvp[0].strip()
        for rule_key in rule_keys:
            if 'other' in rule_key:
                pass
            else:
                if rule_key in rule_dict.keys():
                    rule_dict[rule_key].append(rule_value)
                else:
                    rule_dict[rule_key] = [rule_value]
    return rule_dict


def traverse_dict_for_bag(rules: dict):
    bag_key = 'light red'
    unique_bags = set()
    traverse(rules, bag_key, unique_bags)
    return unique_bags


def traverse_dict_with_key(rules: dict, key: str):
    tmp_dict = rules
    routes = []
    try:
        for i in tmp_dict[key]:
            routes.append(i)
    finally:
        return routes


def traverse(rules: dict, key: str, results: set):
    try:
        for bag in rules[key]:
            traverse(rules, bag, results)
            results.add(bag)
    except KeyError:
        return
    

advent_part_1 = composite_function(
    parse_data,
    parse_rules_backwards,
    traverse_dict_for_bag,
    print
)

advent_part_1(read_data())
