# Advent of Code 2025

For the eight time I'm going to try to find out how far I can make it in [Advent of Code](https://adventofcode.com/2025/). Results for previous editions:
* 2018: 9 days
* 2019: 13 days
* [2020](https://github.com/Leftfish/Advent-of-Code-2020): 25 days for the first time!
* [2021](https://github.com/Leftfish/Advent-of-Code-2021): 25 days for the second time!
* [2022](https://github.com/Leftfish/Advent-of-Code-2022): 25 days for the third time!
* [2023](https://github.com/Leftfish/Advent-of-Code-2023): 25 days for the fourth time!
* [2024](https://github.com/Leftfish/Advent-of-Code-2024): 25 days for the fifth time!

For years I've been telling myself that I've had enough, that I no longer have time, that I have other stuff to do. So far, AoC won with everything, although ususally I had a couple of stars left to collect at the end of the regular AoC schedule. We'll see how it goes this time. It's going to be only 12 days, so I anticipate the difficulty to rise far quicker. Self-imposed rules for LLM usage:
1) The use of AI is limited but not excluded.
2) AI inline autocomplete is DISABLED.
3) AI may be used as a rubber duck or turbocharged Stack Overflow/wikipedia.
4) AI may not be used to solve the entire task.
5) AI may not be used before honest attempts to solve the task without external information (i.e., before running into a brick wall).
6) AI may be used more freely to improve the solution after getting a star.
7) AI-generated code must be re-written to understand what each line does.

Day 3 part 2 was a big challenge (I used dynamic programming which is one of my weaker skills). Day 8 required some researching of stuff that I'd had only a vague idea about, but I was mostly on the right trail even before using external sources. Day 9 part 2 was tough to solve without an external library. 

Things I **L**earned, **R**evised or **I**mproved at in 2025:

* [Day 1 Python](01/d01.py): modulo arithmetic (**R**)
* [Day 2 Python](02/d02.py): using log10 to count the number of digits (**R**)
* [Day 3 Python](03/d03.py): DFS (**R**), dynamic programming (**L**/**I**)
* [Day 4 Python](04/d04.py): set operations (**R**), representing grids as dictionaries (**R**), queues (**R**)
* [Day 5 Python](05/d05.py): flattening ranges of integers (**I**)
* [Day 6 Python](06/d06.py): reduce (**R**) and zip(**I**) in an alternative solution to part 2
* [Day 7 Python](07/d07.py): DFS (**R**), memoization (**I**), Pascal's triangle (**R**) and that you don't need to generate everything that you need to count because you may run ouf of memory (**R**)
* [Day 8 Python](08/d08.py): minimum spanning trees (**L**) and Kruskal's algorithm (**L**)
* [Day 9 Python](09/d09.py): itertools.combinations (**R**) and shapely (**L**) because my original solution did not work for concave polygons (the final does it without external libraries, using ray casting (**L**))