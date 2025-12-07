import os

from collections import defaultdict


SPLITTER = '^'
EMITTER = 'S'


def parse_data(data):
    grid = defaultdict(tuple)
    start = None
    for i, line in enumerate(data.splitlines()):
        for j, char in enumerate(line):
            grid[(i, j)] = char
            if char == EMITTER:
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


def get_all_paths_horrible(grid, start):
    # HORRIBLY INEFFICIENT AND WILL NOT WORK WITH PRODUCTION PUZZLE INPUT
    stack = [((start),)]
    visited = set()
    paths = set()
    while stack:
        current_path = stack.pop()
        visited.add(current_path)
        current_ray = current_path[-1]
        if not can_move_down(current_ray, grid):
            paths.add(current_path)
        else:
            if is_next_splitter(current_ray, grid):
                for new_ray in split(current_ray):
                    new_path = tuple(list(current_path) + [new_ray])
                    if new_path not in visited:
                        stack.append(new_path)
            else:
                new_ray = move_down(current_ray)
                new_path = tuple(list(current_path) + [new_ray])
                if new_ray not in visited:
                    stack.append(new_path)
    return paths


def count_all_paths(data):
    parsed = [list(line) for line in data.splitlines()]
    tape = [0 for _ in range(len(parsed[0]))]
    tape[''.join(parsed[0]).find(EMITTER)] = 1

    for i, line in enumerate(parsed):
        next_tape = tape[::]
        if i == len(parsed) - 1:
            break
        for j in range(len(line)):
            current = tape[j]
            down = parsed[i+1][j]
            if down == SPLITTER and current:
                next_tape[j] = 0
                if j - 1 >= 0:
                    next_tape[j-1] += current
                if j + 1 < len(line):
                    next_tape[j+1] += current
            else:
                next_tape[j] = tape[j]
            tape = next_tape
    return sum(tape)


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


print(f'Day {DAY} of Advent of Code!')
print('Testing...')
print('Total splits in one pass:', dfs_split(*parse_data(TEST_DATA)) == 21)
print('Total timelines (inefficient DFS-approach):', len(get_all_paths_horrible(*parse_data(TEST_DATA))) == 40)
print('Total timelines (Pascal-triangle-like approach):', count_all_paths(TEST_DATA) == 40)

input_path = f"{os.getcwd()}\\{str(DAY).zfill(2)}\\inp"
with open(input_path, mode='r', encoding='utf-8') as inp:
    print('Solution...')
    data = inp.read()
    print('Total splits in one pass:', dfs_split(*parse_data(data)))
    print('Total timelines (Pascal-triangle-like approach):', count_all_paths(data))
