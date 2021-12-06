import pathmagic  # noqa: E402
import aoc


d5_example_string = r'''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''

d5_example_lines = aoc.process_vent_lines_string(d5_example_string)


def test_d5s1():
    danger_points = aoc.count_danger_points(d5_example_lines,
                                            include_diag=False)
    assert danger_points == 5


def test_d5s2():
    danger_points = aoc.count_danger_points(d5_example_lines,
                                            include_diag=True)
    assert danger_points == 12
