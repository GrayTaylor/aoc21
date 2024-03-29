import pathmagic  # noqa: E402
import aoc


d3_example_input = ['00100', '11110', '10110', '10111',
                    '10101', '01111', '00111', '11100',
                    '10000', '11001', '00010', '01010']


def test_d3s1_gamma():
    assert aoc.rate(d3_example_input, 'gamma') == 22


def test_d3s1_epsilon():
    assert aoc.rate(d3_example_input, 'epsilon') == 9


def test_d3s2_oxygen():
    assert aoc.rating(d3_example_input, 'oxygen_generator') == 23


def test_d3s2_co2():
    assert aoc.rating(d3_example_input, 'co2_scrubber') == 10
