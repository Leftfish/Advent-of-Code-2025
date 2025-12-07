import os

from collections import defaultdict

DAY = 7
TEST_DATA = '''.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''

SPLITTER = '^'
EMITTER = 'S'

def parse_data(data):
    grid = defaultdict(tuple)
    start = None
    for i, line in enumerate(data.splitlines()):
        for j, chr in enumerate(line):
            grid[(i, j)] = chr
            if chr == EMITTER:
                start = (i, j)
    return grid, start

def can_move_down(ray, grid):
    i, j = ray
    return (i+1, j) in grid

def is_next_splitter(ray, grid):
    i, j = ray
    return (i+1, j) in grid and grid[(i+1, j)] == SPLITTER

def move_down(ray):
    return (ray[0] + 1, ray[1])

def split(ray):
    return [(ray[0] + 1, ray[1] - 1), (ray[0] + 1, ray[1] + 1)]
def dfs_split(grid, start):
    stack = [(start)]
    visited = set()
    n = 0
    while stack:
        current_ray = stack.pop()
        visited.add(current_ray)
        if can_move_down(current_ray, grid):
            if is_next_splitter(current_ray, grid):
                n += 1
                for new_ray in split(current_ray):
                    if new_ray not in visited:
                        stack.append(new_ray)
            else:
                new_ray = move_down(current_ray)
                if new_ray not in visited:
                    stack.append(new_ray)

    return n


print(f'Day {DAY} of Advent of Code!')
print('Testing...') 
print(dfs_split(*parse_data(TEST_DATA)))

input_path = f"{os.getcwd()}\\{str(DAY).zfill(2)}\\inp"
with open(input_path, mode='r', encoding='utf-8') as inp:
    print('Solution...')
    data = inp.read()
    print(dfs_split(*parse_data(data)))



def debug():
    to_print = [list('.' * 142) for _ in range(143)]
    for i, j in grid:
        to_print[i][j] = grid[(i, j)]

    for line in to_print:
        print(''.join(line))