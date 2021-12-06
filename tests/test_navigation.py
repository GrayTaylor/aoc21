import pathmagic  # noqa: E402
import aoc


d2_example_directions = [['forward', 5],
                         ['down', 5],
                         ['forward', 8],
                         ['up', 3],
                         ['down', 8],
                         ['forward', 2]]


def test_d2s1_example():

    journey = aoc.generate_journey(d2_example_directions, 'd2s1')
    destination = journey[-1]

    assert destination == [15, 10]


def test_d2s2_example():

    journey = aoc.generate_journey(d2_example_directions, 'd2s2')
    destination = journey[-1]

    assert destination == [15, 60]
