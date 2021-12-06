import pathmagic  # noqa: E402
import aoc

d6_example_counts = [3, 4, 3, 1, 2]
example_school = aoc.LanternfishSchool(d6_example_counts)


def test_d6s1():
    example_school.set_to_day_n(18)
    assert example_school.total_fish() == 26

    example_school.set_to_day_n(80)
    assert example_school.total_fish() == 5934


def test_d6s2():
    example_school.set_to_day_n(256)
    assert example_school.total_fish() == 26984457539
