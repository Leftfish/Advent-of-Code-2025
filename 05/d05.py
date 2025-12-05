import os


def parse_data(data):
    raw_all_rngs, raw_ingredients = data.split('\n\n')
    all_rngs = []
    for rng in raw_all_rngs.split('\n'):
        start, stop = rng.split('-')
        all_rngs.append([int(start), int(stop)])

    ingredients = [int(ingredient) for ingredient in raw_ingredients.split('\n')]

    return sorted(all_rngs, key=lambda r: r[0]), ingredients


def merge(all_rngs):
    merged = [all_rngs[0]]
    for r in all_rngs[1:]:
        current = merged[-1]
        if r[0] <= current[1]:
            all_borders = current + r
            current[0] = min(all_borders)
            current[1] = max(all_borders)
        else:
            merged.append(r)
    return merged


def check_ingredient(ingredient, all_rngs):
    for rng in all_rngs:
        if rng[0] <= ingredient <= rng[1]:
            return True
    return False


def count_fresh(ingredients, all_rngs):
    s = 0
    for ingredient in ingredients:
        s += check_ingredient(ingredient, all_rngs)
    return s


def sum_all_fresh(all_rngs):
    return sum(r[1] - r[0] + 1 for r in merge(all_rngs))


DAY = 5
TEST_DATA = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''


print(f'Day {DAY} of Advent of Code!')
print('Testing...')

rngs, ings = parse_data(TEST_DATA)
print('Fresh ingredients:', count_fresh(ings, rngs) == 3)
print('All potentially fresh ingredients:', sum_all_fresh(rngs) == 14)


input_path = f"{os.getcwd()}\\{str(DAY).zfill(2)}\\inp"
with open(input_path, mode='r', encoding='utf-8') as inp:
    print('Solution...')
    data = inp.read()
    rngs, ings = parse_data(data)
    print('Fresh ingredients:', count_fresh(ings, rngs))
    print('All potentially fresh ingredients:', sum_all_fresh(rngs))
