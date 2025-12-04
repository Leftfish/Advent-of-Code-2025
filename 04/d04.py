import os

from collections import defaultdict

PAPER = '@'
EMPTY = '.'


def parse_data(data):
    grid = defaultdict(str)
    for i, line in enumerate(data.splitlines()):
        for j, char in enumerate(line):
            grid[(i, j)] = char

    return grid


def find_adjacent(grid, coord):
    adjacent = set()
    i, j = coord
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            adj = (i+di, j+dj)
            if (di, dj) != (0, 0) and adj in grid and grid[adj] == PAPER:
                adjacent.add((i+di, j+dj))
    return adjacent


def accessible(adjacent):
    return len(adjacent) < 4


def find_removable(grid):
    return {coord for coord in grid if grid[coord] == PAPER and accessible(find_adjacent(grid, coord))}


def count_with_pseudo_to_checkueue(grid):
    s = 0
    to_check = find_removable(grid)

    while to_check:
        current = to_check.pop()
        neighbors = find_adjacent(grid, current)
        if accessible(neighbors) and grid[current] == PAPER:
            grid[current] = EMPTY
            s += 1
            for n in neighbors:
                if grid[n] == PAPER:
                    to_check.add(n)

    return s


DAY = 4
TEST_DATA = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''


print(f'Day {DAY} of Advent of Code!')
print('Testing...')
warehouse = parse_data(TEST_DATA)
print('Initially removable:', len(find_removable(warehouse)) == 13)
print('Iteratively removed (set as pseudo-to_checkueue):', count_with_pseudo_to_checkueue(warehouse) == 43)


input_path = f"{os.getcwd()}\\{str(DAY).zfill(2)}\\inp"
with open(input_path, mode='r', encoding='utf-8') as inp:
    print('Solution...')
    data = inp.read()
    warehouse = parse_data(data)
    print('Initially removable:', len(find_removable(warehouse)))
    print('Iteratively removed (set as pseudo-to_checkueue):', count_with_pseudo_to_checkueue(warehouse))
