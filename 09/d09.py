import os

from itertools import combinations

from shapely.geometry import Polygon, box

def parse_data(raw_data):
    return [tuple([int(i) for i in box.split(',')]) for box in raw_data.splitlines()]


area = lambda pair: (abs(pair[0][0] - pair[1][0]) + 1) * (abs(pair[0][1] - pair[1][1]) + 1)


def find_largest(pairs):
    m = 0
    for p in pairs:
        a = area(p)
        if a > m:
            m = a
    return m


def get_convex(reds, edges): # unused in the final solution, needs collision detection (some ray casting and intersection checks?)
    in_convex = set(reds)
    for edge in edges:
        same_col = edge[0][0] == edge[1][0]
        same_row = edge[0][1] == edge[1][1]
        if same_row:
            start = min(edge[0][0], edge[1][0])
            stop = max(edge[0][0], edge[1][0])
            for x in range(start, stop+1):
                pt = (x, edge[0][1])
                in_convex.add(pt)
        elif same_col:
            start = min(edge[0][1], edge[1][1])
            stop = max(edge[0][1], edge[1][1])
            for y in range(start, stop+1):
                pt = (edge[0][0], y)
                in_convex.add(pt)
    return in_convex


def get_corners(pair):
    a, b = pair[0]
    c, d = pair[1]
    return ((a, b), (c, d), (a, d), (c, b))


def find_largest_in_polygon(reds, pairs):
    poly = Polygon(reds)
    rectangles = sorted([get_corners(pair) for pair in pairs],
                        key=lambda r: area((r[0], r[1])), reverse=True)

    for rectangle in rectangles:
        xs = [p[0] for p in rectangle]
        ys = [p[1] for p in rectangle]
        xmin, xmax = min(xs), max(xs)
        ymin, ymax = min(ys), max(ys)
        to_check = box(xmin, ymin, xmax, ymax)
        if poly.covers(to_check):
            xmin, ymin, xmax, ymax = to_check.bounds
            return int(area(((xmin, ymin), (xmax, ymax))))
    return 0


DAY = 9
TEST_DATA = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''


print(f'Day {DAY} of Advent of Code!')
print('Testing...')
reds = parse_data(TEST_DATA)
pairs = list(combinations(reds, 2))
print('Largest rectangle:', find_largest(pairs) == 50)
print('Largest within the polygon:', find_largest_in_polygon(reds, pairs) == 24)

input_path = f"{os.getcwd()}\\{str(DAY).zfill(2)}\\inp"
with open(input_path, mode='r', encoding='utf-8') as inp:
    print('Solution...')
    data = inp.read()
    reds = parse_data(data)
    pairs = list(combinations(reds, 2))
    print('Largest rectangle:', find_largest(pairs))
    print('Largest within the polygon:', find_largest_in_polygon(reds, pairs))
