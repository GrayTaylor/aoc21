def low_points(grid):
    low_points = set()
    for p in grid.points():
        neighbour_vals = [grid.value_at_point(n)
                          for n in grid.neighbours_of_point(p)]
        if grid.value_at_point(p) < min(neighbour_vals):
            low_points.add(p)
    return low_points


def risk_level(point, grid):
    return 1 + grid.value_at_point(point)


def grow_basin(basin_points, grid):
    return [p for p in grid.periphery(basin_points)
            if grid.value_at_point(p) < 9]


def get_basin(low_point, grid):
    search = True
    basin = [low_point]
    while search:
        new_points = grow_basin(basin, grid)
        if len(new_points) == 0:
            search = False
        else:
            basin.extend(new_points)
    return basin
