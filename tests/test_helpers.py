import pathmagic  # noqa: E402
import aoc


def test_horizontal_line():
    input_coords = [0, 9, 5, 9]
    points = aoc.interpolate_line(input_coords)
    expected_points = [(0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9)]
    assert set(points) == set(expected_points)


def test_reversed_horizontal_line():
    input_coords = [5, 9, 0, 9]
    points = aoc.interpolate_line(input_coords)
    expected_points = [(0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9)]
    assert set(points) == set(expected_points)


def test_vertical_line():
    input_coords = [7, 0, 7, 4]
    points = aoc.interpolate_line(input_coords)
    expected_points = [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4)]
    assert set(points) == set(expected_points)


def test_reversed_vertical_line():
    input_coords = [7, 4, 7, 0]
    points = aoc.interpolate_line(input_coords)
    expected_points = [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4)]
    assert set(points) == set(expected_points)


def test_45_deg_line_ur():
    input_coords = [0, 0, 8, 8]
    points = aoc.interpolate_line(input_coords)
    expected_points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4),
                       (5, 5), (6, 6), (7, 7), (8, 8)]
    assert set(points) == set(expected_points)


def test_45_deg_line_dr():
    input_coords = [0, 8, 8, 0]
    points = aoc.interpolate_line(input_coords)
    expected_points = [(0, 8), (1, 7), (2, 6), (3, 5), (4, 4),
                       (5, 3), (6, 2), (7, 1), (8, 0)]
    assert set(points) == set(expected_points)


def test_45_deg_line_ul():
    input_coords = [8, 0, 0, 8]
    points = aoc.interpolate_line(input_coords)
    expected_points = [(0, 8), (1, 7), (2, 6), (3, 5), (4, 4),
                       (5, 3), (6, 2), (7, 1), (8, 0)]
    assert set(points) == set(expected_points)


def test_45_deg_line_dl():
    input_coords = [8, 8, 0, 0]
    points = aoc.interpolate_line(input_coords)
    expected_points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4),
                       (5, 5), (6, 6), (7, 7), (8, 8)]
    assert set(points) == set(expected_points)


def test_shallow_line_ur():
    input_coords = [1, 2, 5, 4]
    points = aoc.interpolate_line(input_coords)
    expected_points = [(1, 2), (3, 3), (5, 4)]
    assert set(points) == set(expected_points)


def test_shallow_line_ul():
    input_coords = [5, 1, 1, 3]
    points = aoc.interpolate_line(input_coords)
    expected_points = [(5, 1), (3, 2), (1, 3)]
    assert set(points) == set(expected_points)


def test_shallow_line_dr():
    input_coords = [1, 3, 5, 1]
    points = aoc.interpolate_line(input_coords)
    expected_points = [(1, 3), (3, 2), (5, 1)]
    assert set(points) == set(expected_points)


def test_shallow_line_dl():
    input_coords = [5, 3, 1, 1]
    points = aoc.interpolate_line(input_coords)
    expected_points = [(5, 3), (3, 2), (1, 1)]
    assert set(points) == set(expected_points)


def test_steep_line_ur():
    input_coords = [0, 0, 3, 9]
    points = aoc.interpolate_line(input_coords)
    expected_points = [(0, 0), (1, 3), (2, 6), (3, 9)]
    assert set(points) == set(expected_points)


def test_steep_line_ul():
    input_coords = [0, 0, -3, 9]
    points = aoc.interpolate_line(input_coords)
    expected_points = [(0, 0), (-1, 3), (-2, 6), (-3, 9)]
    assert set(points) == set(expected_points)


def test_steep_line_dr():
    input_coords = [1, 1, 4, -8]
    points = aoc.interpolate_line(input_coords)
    expected_points = [(1, 1), (2, -2), (3, -5), (4, -8)]
    assert set(points) == set(expected_points)


def test_steep_line_dl():
    input_coords = [10, 9, 7, 0]
    points = aoc.interpolate_line(input_coords)
    expected_points = [(10, 9), (9, 6), (8, 3), (7, 0)]
    assert set(points) == set(expected_points)
