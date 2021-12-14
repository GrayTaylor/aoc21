import itertools


def read_file_as_string(filename):
    with open(filename, 'r') as f:
        return f.read().strip('\n')


def read_file_as_list(filename):
    with open(filename, 'r') as f:
        raw_list = f.readlines()
    return [r.strip('\n') for r in raw_list]


def read_file_as_list_of_lists(filename):
    return [r.split(',') for r in read_file_as_list(filename)]


def read_file_as_single_line_of_ints(filename):
    with open(filename, 'r') as f:
        raw_lines = f.readlines()

    if len(raw_lines) > 1:
        raise ValueError(f'Got {len(raw_lines)} lines, but expected just one!')

    return [int(x) for x in raw_lines[0].strip('\n').split(',')]


def distinct_counts(all_strings, strings_of_interest=None):
    '''
    Counts the number of times each string appears in the list,
    returning a dictionary of strings as keys and counts as values.

    By default, considers each distinct string;
    optionally, you may restrict attention to a list of strings of interest
    (if one of your supplied strings of interest does not appear,
    it gets a count of 0).
    '''
    if strings_of_interest is None:
        counts = dict.fromkeys(all_strings)
    else:
        counts = dict.fromkeys(strings_of_interest)
    for key in counts:
        counts[key] = sum([1 for s in all_strings if s == key])
    return counts


def most_common_entry(all_strings, strings_of_interest=None):
    counts = distinct_counts(all_strings, strings_of_interest)
    ordered_counts = sorted([(v, k) for k, v in counts.items()], reverse=True)
    return ordered_counts[0][1]


def least_common_entry(all_strings, strings_of_interest=None):
    counts = distinct_counts(all_strings, strings_of_interest)
    ordered_counts = sorted([(v, k) for k, v in counts.items()])
    return ordered_counts[0][1]


def interpolate_line(l):
    '''
    Assumes a quadruple of coordinates ordered x_1,y_1,x_2,y2
    such that the line from point 1 to point 2 is either
    horizontal, vertical, or a 45 degree diagonal.

    Returns all points on the line, including p1 and p2.
    '''
    start_x = l[0]
    start_y = l[1]
    end_x = l[2]
    end_y = l[3]

    if start_x == end_x:
        # Special case, vertical line
        low = min(start_y, end_y)
        high = max(start_y, end_y)
        return [(start_x, j) for j in range(low, high + 1)]

    # Otherwise, we can meaningfully talk about gradient
    m = (end_y - start_y) / (end_x - start_x)
    c = start_y - m * start_x

    left = min(start_x, end_x)
    right = max(start_x, end_x)

    all_points = [(x, m * x + c) for x in range(left, right + 1)]
    return [(p[0], int(p[1])) for p in all_points if p[1].is_integer()]


class ValueGrid:
    def __init__(self, values, neighbour_pattern='ordinal'):
        assert neighbour_pattern in ('ordinal', 'ring')
        self.neighbour_pattern = neighbour_pattern
        self.num_rows = len(values)
        self.num_cols = len(values[0])
        for row in values:
            if len(row) != self.num_cols:
                raise ValueError('Rows of different lengths')
        self.values = {(p[0], p[1]): values[p[0]][p[1]]
                       for p in itertools.product(range(self.num_rows),
                                                  range(self.num_cols))}
        self.input_values = {(p[0], p[1]): values[p[0]][p[1]]
                             for p in itertools.product(range(self.num_rows),
                                                        range(self.num_cols))}

    def value_at_point(self, p):
        return self.values[p]

    def set_value_at_point(self, p, value):
        self.values[p] = value

    def increment_value_at_point(self, p):
        self.values[p] += 1

    def neighbours_of_point(self, p):
        i = p[0]
        j = p[1]
        possible_neighbours = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

        if self.neighbour_pattern == 'ring':
            possible_diag_neighbours = [(i - 1, j - 1), (i - 1, j + 1),
                                        (i + 1, j - 1), (i + 1, j + 1)]
            possible_neighbours.extend(possible_diag_neighbours)

        return set(n for n in possible_neighbours if n in self.values)

    def periphery(self, points):
        periphery = set()
        for p in points:
            neighbours = self.neighbours_of_point(p)
            for n in neighbours:
                if n not in points and n not in periphery:
                    periphery.add(n)
        return [p for p in periphery]

    def points(self):
        return set(p for p in self.values)

    def __repr__(self):
        return f'{self.num_rows} by {self.num_cols} grid of values'

    def view_grid(self):
        for r in range(self.num_rows):
            print([self.value_at_point((r, c)) for c in range(self.num_cols)])

    def reset(self):
        self.values = {k: v for k, v in self.input_values.items()}


def int_array_from_strings(input_strings):
    return [[int(x) for x in s] for s in input_strings]


def add_dicts(x, y):
    return {k: x.get(k, 0) + y.get(k, 0) for k in set(x) | set(y)}
