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

m = 0
for r in rectangles:
    if rectangle_in_convex(r, row_to_border) and area(r) > m:
        m = area(r)

print(m)

'''
1. lista punktów jest już wystarczająco posortowana! wystarczy patrzeć do następnego, a na koniec połączyć ostatni z pierwszym
- jeśli ten sam x, to y-i pomiędzy do zielonych, jak ten sam y, to x-y pomiędzy do zielonych
2. posortować aktualne zielone i czerwone według y-a (to są wszystkie punkty w figurze)
3. iterować przez nie i dla każdego y-a dodać do zielonych wszystkie punkty pomiędzy min-x a max-x
4. jeszcze raz przez pary czerwonych ale:
    - zrobić zbiór wszystkich punktów w prostokącie
    - sprawdzić czy zbiór zawiera się w zbiorze "figura": if tak, dodać pole
    - ale to będzie strasznie niewydajne!!!!! MemoryError
    - może iterować od najwyższego pola i odrzucać po kolei?
    - czyli:
        - set coloured (red i green)
        - wygeneruj wszystkie pary, posortuj od najwyższego pola
        - skanuj każdy prostokąt linia po linii i jeśli zbiór linia nie zawiera się cały w zbiorze coloured to odrzuć prostokąt
        - wtedy skanujesz w najgorszym razie 100 000 razy (tyle linii) per prostokąt, ale czy za każdym razem budując zbiór 100 000 elementów???
        - czy da się inaczej sprawdzić? da się! trzeba sprawdzić, czy w danym wierszu najbardziej lewy koord prostokątu jest na lewo od najbardziej lewego
          koorda w figurze
        - więc nie trzeba budować zbioru
    - worst case scenario to nadal 122 000 * 100 000 linii czyli 12 mld iteracji :(((( ale w praktyce to musi być mniej
    
    
    - A MOŻE DLA KAŻDEGO PO PROSTU SPRAWDZAĆ 4 ROGI!!!
    - ZBUDUJ PARĘ, DOBUDUJ ROGI, SPRAWDŹ CZY CZTERY ROGI SĄ W ŚRODKU I VOILA!!!!!!
    - nadal potrzebny zbiór zielonych i czerwonych!

'''


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


m = 0
for r in rectangles:
    if rectangle_in_convex(r, row_to_border) and area(r) > m:
        m = area(r)
    else:
        print(f'{r} not in convex')

print(m)
