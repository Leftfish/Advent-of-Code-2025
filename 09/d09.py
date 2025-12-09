import os

import math
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


def get_corners(pair):
    a, b = pair[0]
    c, d = pair[1]
    return ((a, b), (c, d), (a, d), (c, b))

def get_polygon_shape(reds, edges):
    in_polygon_shape = set(reds)

    for edge in edges:
        same_col = edge[0][0] == edge[1][0]
        same_row = edge[0][1] == edge[1][1]

        # Horizontal edge
        if same_row:
            start = min(edge[0][0], edge[1][0])
            stop = max(edge[0][0], edge[1][0])
            for x in range(start, stop + 1):
                pt = (x, edge[0][1])
                in_polygon_shape.add(pt)
        # Vertical edge
        elif same_col:
            start = min(edge[0][1], edge[1][1])
            stop = max(edge[0][1], edge[1][1])
            for y in range(start, stop + 1):
                pt = (edge[0][0], y)
                in_polygon_shape.add(pt)
    return in_polygon_shape


def get_sorted_edges(reds):
    edges = list(zip(reds, reds[1:])) + [(reds[-1], reds[0])]
    l = lambda edge: 1 + abs(edge[0][0] - edge[1][0]) + abs(edge[0][1] - edge[1][1])
    return sorted(edges, key=l, reverse=True)


def edge_intrudes_rect(poly_edge, rectangle):
    edge_start, edge_stop = poly_edge
    (x1, y1) = edge_start
    (x2, y2) = edge_stop
    edge_xs = sorted([x1, x2])
    edge_ys = sorted([y1, y2])

    rect_xs = [p[0] for p in rectangle]
    xmin, xmax = min(rect_xs), max(rect_xs)
    rect_ys = [p[1] for p in rectangle]
    ymin, ymax = min(rect_ys), max(rect_ys)

    horizontal = y1 == y2
    vertical = x1 == x2

    if horizontal:
        if not ymin < y1 < ymax:
            return False
        e_from, e_to = edge_xs
        L = max(e_from, xmin)
        R = min(e_to, xmax)
        return L < R
    
    if vertical:
        if not xmin < x1 < ymax:
            return False
        e_from, e_to = edge_ys
        B = max(e_from, ymin)
        T = min(e_to, ymax)
        return B < T


def point_in_or_on_polygon(px, py, polygon):
    def point_on_segment(px, py, x1, y1, x2, y2):
        if x1 == x2:  # vertical
            return px == x1 and min(y1, y2) <= py <= max(y1, y2)
        if y1 == y2:  # horizontal
            return py == y1 and min(x1, x2) <= px <= max(x1, x2)
        return False

    inside = False
    n = len(polygon)

    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]

        # is the point on the border (horizontal or vertical)
        if point_on_segment(px, py, x1, y1, x2, y2):
            return True

        # ray casting
        if y1 != y2:  # vertical-ish crossing only
            # detect if py is between y1 and y2
            if min(y1, y2) <= py < max(y1, y2):
                if px < x1:  # vertical edge at x1
                    inside = not inside

    return inside


def rectangle_in_poly(rectangle, poly_edges, reds):
    for x, y in rectangle:
        if not point_in_or_on_polygon(x, y, reds):
            return False

    for poly_e in poly_edges:
        if edge_intrudes_rect(poly_e, rectangle):
            return False
    return True


def find_largest_in_polygon_raw(pairs, reds):
    edges = get_sorted_edges(reds)
    rectangles = sorted([get_corners(pair) for pair in pairs],
                            key=lambda r: area((r[0], r[1])), reverse=True)
    for r in rectangles:
        if rectangle_in_poly(r, edges, reds):
            return area(r)

def find_largest_in_polygon_shapely(reds, pairs):
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
print('Largest within the polygon (shapely):', find_largest_in_polygon_shapely(reds, pairs) == 24)
print('Largest within the polygon (raw):', find_largest_in_polygon_raw(pairs, reds) == 24)

input_path = f"{os.getcwd()}\\{str(DAY).zfill(2)}\\inp"
with open(input_path, mode='r', encoding='utf-8') as inp:
    print('Solution...')
    data = inp.read()
    reds = parse_data(data)
    pairs = list(combinations(reds, 2))
    print('Largest rectangle:', find_largest(pairs))
    print('Largest within the polygon (shapely):', find_largest_in_polygon_shapely(reds, pairs))
    print('Largest within the polygon (raw):', find_largest_in_polygon_raw(pairs, reds))
