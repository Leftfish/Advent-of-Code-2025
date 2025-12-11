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
3) AI may be used as a rubber duck or turbocharged Stack Overflow/wikipedia to look up for algorithms etc.
4) AI may not be used to solve the entire task.
5) AI may not be used before honest attempts to solve the task without external information (i.e., before running into a brick wall). If in the previous years I would have given up and looked up how others solve it, I can instead try to use an LLM to get to a solution.
6) AI may be used more freely to improve the solution after getting a star, if that amounts to me learning something new.
7) AI-generated code must be re-written to understand what each line does, so no blatant copy-pasting.

Day 3 part 2 was a big challenge (I used dynamic programming which is one of my weaker skills). Day 8 required some researching of stuff that I'd had only a vague idea about, but I was mostly on the right trail even before using external sources. Day 9 part 2 was tough to solve without an external library. Day 10 part 2 was BRUTAL because of linear algebra (I immediately noticed that the problem is extremely hard to compute and I see that a lot of people struggled with it).

Things I **L**earned, **R**evised or **I**mproved at in 2025, as well as AI usage log (**H** when it helped get at least one star, **U** when I used it to upgrade the solution after getting the stars without AI, **N** when no AI tools were used):

* [Day 1 Python](01/d01.py) **N** : modulo arithmetic (**R**)
* [Day 2 Python](02/d02.py) **U** (LLM used to see how to upgrade the solution to avoid manipulating strings) : using log10 to count the number of digits (**R**)
* [Day 3 Python](03/d03.py) **H** (LLM used to debug the DP solution): DFS (**R**), dynamic programming (**L**/**I**)
* [Day 4 Python](04/d04.py) **N** : set operations (**R**), representing grids as dictionaries (**R**), queues (**R**)
* [Day 5 Python](05/d05.py) **N** : flattening ranges of integers (**I**)
* [Day 6 Python](06/d06.py) **N** : reduce (**R**) and zip(**I**) in an alternative solution to part 2
* [Day 7 Python](07/d07.py) **U** (LLM used to debug the upgrade that used memoization): DFS (**R**), memoization (**I**), Pascal's triangle (**R**) and that you don't need to generate everything that you need to count because you may run ouf of memory (**R**)
* [Day 8 Python](08/d08.py) **U** (LLM used to debug the upgrade that did not rely on external libraries): minimum spanning trees (**L**) and Kruskal's algorithm (**L**)
* [Day 9 Python](09/d09.py) **U** (LLM used to debug the upgrade that did not rely on external libraries): itertools.combinations (**R**) and shapely (**L**) because my original solution did not work for concave polygons (the final does it without external libraries, using ray casting (**L**))
* [Day 10 Python](10/d10.py) **H** (LLM shamefully used to get out of the rabbit hole of trying to use DFS): BFS (**R**) because my original approach for part 1 did not make sense, linear programming (**L**) and first steps with scipy (**L**) for part 2 which was WAY above my weight category
* [Day 11 Python](11/d11.py) **N** : iterative BFS (**R**) and recursive DFS with memoization (**I**)