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


def sum_paper(grid):
    return sum(1 for fld in grid if grid[fld] == PAPER)


def count_iteratively_removed(grid):
    s = 0
    while True:
        removable = find_removable(grid)
        if not removable:
            break
        pre_remove = sum_paper(grid)
        for coord in removable:
            grid[coord] = EMPTY
        s += abs(sum_paper(grid) - pre_remove)
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
print('Initially removable:', sum(1 for fld in warehouse if warehouse[fld] == PAPER and len(find_adjacent(warehouse, fld)) < 4) == 13)
print('Iteratively removed:', count_iteratively_removed(warehouse) == 43)


input_path = f"{os.getcwd()}\\{str(DAY).zfill(2)}\\inp"
with open(input_path, mode='r', encoding='utf-8') as inp:
    print('Solution...')
    data = inp.read()
    warehouse = parse_data(data)
    print('Initially removable:', sum(1 for fld in warehouse if warehouse[fld] == PAPER and len(find_adjacent(warehouse, fld)) < 4))
    print('Iteratively removed:', count_iteratively_removed(warehouse))
