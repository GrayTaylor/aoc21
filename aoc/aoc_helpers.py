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
