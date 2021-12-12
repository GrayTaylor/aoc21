def dumbo_step(grid):
    flashed_this_step = []

    for p in grid.points():
        grid.increment_value_at_point(p)

    propagators = [p for p in grid.points() if grid.value_at_point(p) > 9]

    while len(propagators) > 0:
        for p in propagators:
            if p not in flashed_this_step:
                flashed_this_step.append(p)
                for n in grid.neighbours_of_point(p):
                    grid.increment_value_at_point(n)
        propagators = [p for p in grid.points()
                       if grid.value_at_point(p) > 9
                       and p not in flashed_this_step]

    for p in flashed_this_step:
        grid.set_value_at_point(p, 0)

    return len(flashed_this_step)


def count_total_flashes(grid, num_steps):
    grid.reset()
    total_flashes = 0
    for k in range(num_steps):
        total_flashes += dumbo_step(grid)
    return total_flashes


def detect_sync(grid):
    target_flashes = grid.num_rows * grid.num_cols
    grid.reset()
    steps = 1
    while dumbo_step(grid) != target_flashes:
        steps += 1
    return steps
