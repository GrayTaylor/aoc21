import re
import aoc_helpers as aoc


def process_vent_lines_string(s):
    lines = re.findall(r'(\d+),(\d+) -> (\d+),(\d+)', s)
    return [[int(x) for x in line] for line in lines]


def count_danger_points(lines, include_diag=True):
    horizontal_lines = [l for l in lines if l[0] == l[2]]
    vertical_lines = [l for l in lines if l[1] == l[3]]

    valid_lines = [h for h in horizontal_lines]
    valid_lines.extend(vertical_lines)

    if include_diag:
        diagonal_lines = [l for l in lines
                          if abs(l[2]-l[0]) == abs(l[3] - l[1])]
        valid_lines.extend(diagonal_lines)

    used_points = {}
    for l in valid_lines:
        points_on_l = aoc.interpolate_line(l)
        for point in points_on_l:
            if point in used_points:
                used_points[point] += 1
            else:
                used_points[point] = 1

    danger_points = [p for p, v in used_points.items() if v > 1]

    return len(danger_points)
