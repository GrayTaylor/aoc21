def new_point(previous_point, fold_axis, fold_index):
    assert fold_axis in ['x', 'y']
    v0 = previous_point[0]
    v1 = previous_point[1]
    if fold_axis == 'x':
        if v0 < fold_index:
            return (v0, v1)
        else:
            return (2 * fold_index - v0, v1)
    elif fold_axis == 'y':
        if v1 < fold_index:
            return (v0, v1)
        else:
            return (v0, 2 * fold_index - v1)


def generate_points(initial_points, folds):
    instructions = []
    for f in folds:
        instructions.append([f[11], int(f[13:])])

    current_points = set([p for p in initial_points])
    for i in instructions:
        current_points = set([new_point(p, i[0], i[1])
                              for p in current_points])

    return current_points


def render_code(points):
    max_x = max(p[0] for p in points)
    max_y = max(p[1] for p in points)

    for j in range(max_y + 1):
        row_j = ['X' if (i, j) in points else ' '
                 for i in range(max_x + 1)]
        print(''.join(row_j))


def generate_code(initial_points, folds):
    render_code(generate_points(initial_points, folds))
