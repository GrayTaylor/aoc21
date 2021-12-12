import pathmagic  # noqa: E402
import aoc


example_dumbo = ['5483143223',
                 '2745854711',
                 '5264556173',
                 '6141336146',
                 '6357385478',
                 '4167524645',
                 '2176841721',
                 '6882881134',
                 '4846848554',
                 '5283751526']

example_grid = aoc.ValueGrid(aoc.int_array_from_strings(example_dumbo),
                             neighbour_pattern='ring')


def test_num_flashes():
    assert aoc.count_total_flashes(example_grid, 10) == 204
    assert aoc.count_total_flashes(example_grid, 100) == 1656


def test_sync():
    assert aoc.detect_sync(example_grid) == 195
