import os

from collections import defaultdict, deque
from math import prod


def parse_data(data):
    graph = defaultdict(list)
    for line in data.splitlines():
        start, stops = line.split(':')
        graph[start] = [stop for stop in stops.strip().split(' ')]

    return graph


def bfs(g, start, stop):
    Q = deque([start])
    c = 0
    while Q:
        current = Q.popleft()
        if current == stop:
            c += 1
        else:
            for neighbor in g[current]:
                Q.append(neighbor)
    return c


def dfs(g, current, stop, cache):
    if current == stop:
        #print(f'Reached goal, cache is {cache}')
        return 1

    if current in cache:
        #print(f'Found {current} in cache with {cache[current]}')
        return cache[current]
    s = 0
    for neighbor in g[current]:
        #print(f'    checking {current}->{neighbor}')
        s += dfs(g, neighbor, stop, cache)
    #print(f'Updating cache for {current} to {s}')
    cache[current] = s
    #print(f'At {current} returning {cache[current]} from cache, cache is {cache}')
    return cache[current]


DAY = 11
TEST_DATA = '''aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out'''

TEST_DATA_2 = '''svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out'''


print(f'Day {DAY} of Advent of Code!')
print('Testing...')
g = parse_data(TEST_DATA)
g2 = parse_data(TEST_DATA_2)

print(dfs(g2, 'svr', 'out', {}))

print('From us to out:', bfs(g, 'you', 'out') == 5)
print('Server connections:', prod([dfs(g2, 'svr', 'fft', {}),
                                   dfs(g2, 'fft', 'dac', {}),
                                   dfs(g2, 'dac', 'out', {})]) +
                             prod([dfs(g2, 'svr', 'dac', {}),
                                   dfs(g2, 'dac', 'fft', {}),
                                   dfs(g2, 'fft', 'out', {})]) == 2)


input_path = f"{os.getcwd()}\\{str(DAY).zfill(2)}\\inp"
with open(input_path, mode='r', encoding='utf-8') as inp:
    print('Solution...')
    data = inp.read()
    g = parse_data(data)
    g2 = parse_data(data)

    print('From us to out:', bfs(g, 'you', 'out'))
    print('Server connections:', prod([dfs(g2, 'svr', 'fft', {}),
                                       dfs(g2, 'fft', 'dac', {}),
                                       dfs(g2, 'dac', 'out', {})]) +
                                 prod([dfs(g2, 'svr', 'dac', {}),
                                       dfs(g2, 'dac', 'fft', {}),
                                       dfs(g2, 'fft', 'out', {})]))
