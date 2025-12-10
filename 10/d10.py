import os

import re
from collections import deque


def parse_data(data):
    machines = []
    for line in data.splitlines():
        machine = []
        regex = r'^\[(.+?)\]\s+((?:\([^)]*\)\s*)+)\{([^}]*)\}$'
        parsed = re.findall(regex, line)[0]
        machine = [0 if c == '.' else 1 for c in parsed[0]]
        buttons = []
        for button in parsed[1].split(' '):
            button = button.strip()
            if not button: continue
            val = eval(button)
            if not isinstance(val, tuple):
                val = (val,)
            buttons.append(val)
        joltages = [int(j) for j in parsed[2].split(',')]
        machines.append((machine, buttons, joltages))
    return machines


def reset_machine(result):
    return [0 for j in result]


def machine_ready(machine, result):
    return machine == result


def neg(val):
    return 1 if val == 0 else 0


def press_button(machine, button):
    new_machine = machine.copy()
    for idx in button:
        new_machine[idx] = neg(machine[idx])
    return new_machine


def bfs(start, result, buttons):
    Q = deque([(start, 0)])
    visited = {tuple(start)}

    while Q:
        current, steps = Q.popleft()
        if current == result:
            return steps

        for button in buttons:
            new = press_button(current, button)
            k = tuple(new)
            if k not in visited:
                visited.add(k)
                Q.append((new, steps+1))


def count_buttons_no_joltage(machines):
    s = 0
    for m in machines:
        result, buttons, _ = m
        start = reset_machine(result)
        s += bfs(start, result, buttons)
    return s


DAY = 10
TEST_DATA = '''[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}'''


print(f'Day {DAY} of Advent of Code!')
print('Testing...')
machines = parse_data(TEST_DATA)
print(f'Total pushes:', count_buttons_no_joltage(machines) == 7)

input_path = f"{os.getcwd()}\\{str(DAY).zfill(2)}\\inp"
with open(input_path, mode='r', encoding='utf-8') as inp:
    print('Solution...')
    data = inp.read()
    machines = parse_data(data)
    print(f'Total pushes:', count_buttons_no_joltage(machines))
