import os

from itertools import combinations
from collections import defaultdict

def parse_data(raw_data):
    return [tuple([int(i) for i in box.split(',')]) for box in raw_data.splitlines()]


DAY = 9
TEST_DATA = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''



area = lambda pair: (abs(pair[0][0] - pair[1][0]) + 1) * (abs(pair[0][1] - pair[1][1]) + 1)

def get_biggest_rectangle(pairs):
    m = 0
    for p in pairs:
        a = area(p)
        if a > m:
            m = a
    return m

def get_convex(reds, edges):
    in_convex = set(reds)
    row_to_border = defaultdict(list)
    for edge in edges:
        same_col = edge[0][0] == edge[1][0]
        same_row = edge[0][1] == edge[1][1]
        if same_row:
            start = min(edge[0][0], edge[1][0])
            stop = max(edge[0][0], edge[1][0])
            for x in range(start, stop+1):
                pt = (x, edge[0][1])
                in_convex.add(pt)
                if row_to_border[x]:
                    row_to_border[x][0] = min(pt[1], row_to_border[x][0])
                    row_to_border[x][1] = max(pt[1], row_to_border[x][1])
                else:
                    row_to_border[x] = [pt[1], pt[1]]
        elif same_col:
            start = min(edge[0][1], edge[1][1])
            stop = max(edge[0][1], edge[1][1])
            for y in range(start, stop+1):
                pt = (edge[0][0], y)
                in_convex.add(pt)
                x = edge[0][0]
                if row_to_border[x]:
                    row_to_border[x][0] = min(pt[1], row_to_border[x][0])
                    row_to_border[x][1] = max(pt[1], row_to_border[x][1])
                else:
                    row_to_border[x] = [pt[1], pt[1]]

    return in_convex, row_to_border

def get_corners(pair):
    a, b = pair[0]
    c, d = pair[1]
    return ((a, b), (c, d), (a, d), (c, b))

def rectangle_in_convex(rectangle, row_to_border):
    for corner in rectangle:
        x, y = corner
        if not row_to_border[x][0] <= y <= row_to_border[x][1]:
            return False
    return True

reds = parse_data(TEST_DATA)
edges = list(zip(reds, reds[1:])) + [(reds[-1], reds[0])]
convex, row_to_border = get_convex(reds, edges)
pairs = list(combinations(reds, 2))
rectangles = [get_corners(p) for p in pairs]

### DOES NOT WORK FOR CONCAVES!!!
def part2_wrong():
    m = 0
    for r in rectangles:
        if rectangle_in_convex(r, row_to_border) and area(r) > m:
            m = area(r)

    print(m)

part2_wrong()

from shapely.geometry import Polygon, box
import matplotlib.pyplot as plt



def plot_geom(ax, geom, face_alpha=0.2, label=None):
    # Polygon (with possible holes)
    if geom.geom_type == "Polygon":
        x, y = geom.exterior.xy
        ax.fill(x, y, alpha=face_alpha, label=label)
        ax.plot(x, y)

        for hole in geom.interiors:
            hx, hy = hole.xy
            ax.fill(hx, hy, color="white")   # punch the hole visually
            ax.plot(hx, hy)
    # MultiPolygon etc.
    else:
        for g in geom.geoms:
            plot_geom(ax, g, face_alpha=face_alpha, label=label)

poly = Polygon(reds)
rrs = []
for r in rectangles:
    xs = [p[0] for p in r]
    ys = [p[1] for p in r]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    rr = box(xmin, ymin, xmax, ymax)
    if poly.covers(rr):
        rrs.append(rr)

m = 0
s = None
for rr in rrs:
    if rr.area > m:
        s = rr
        m = rr.area

xmin, ymin, xmax, ymax = s.bounds
opposite1 = (xmin, ymin)
opposite2 = (xmax, ymax)

print(area((opposite1,opposite2)))



print(f'Day {DAY} of Advent of Code!')
print('Testing...')
reds = parse_data(TEST_DATA)
print('Biggest rectangle:', get_biggest_rectangle(combinations(reds, 2)))


input_path = f"{os.getcwd()}\\{str(DAY).zfill(2)}\\inp"
with open(input_path, mode='r', encoding='utf-8') as inp:
    print('Solution...')
    data = inp.read()
reds = parse_data(data)
print('Biggest rectangle:', get_biggest_rectangle(combinations(reds, 2)))

edges = list(zip(reds, reds[1:])) + [(reds[-1], reds[0])]
convex, row_to_border = get_convex(reds, edges)
pairs = list(combinations(reds, 2))

rectangles = [get_corners(p) for p in pairs]


reds = parse_data(data)
poly = Polygon(reds)
rrs = []
for r in rectangles:
    xs = [p[0] for p in r]
    ys = [p[1] for p in r]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    rr = box(xmin, ymin, xmax, ymax)
    if poly.covers(rr):
        rrs.append(rr)

m = 0
s = None
for rr in rrs:
    if rr.area > m:
        s = rr
        m = rr.area

xmin, ymin, xmax, ymax = s.bounds
opposite1 = (xmin, ymin)
opposite2 = (xmax, ymax)

print(area((opposite1,opposite2)))


fig, ax = plt.subplots()


plot_geom(ax, poly, face_alpha=0.15, label="polygon")
plot_geom(ax, s, face_alpha=0.35, label=f"res")

ax.set_aspect("equal", adjustable="box")
ax.legend()
ax.grid(True, alpha=0.3)
plt.show()
