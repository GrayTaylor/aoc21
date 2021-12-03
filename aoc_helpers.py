def read_file_as_string(filename):
    with open(filename, 'r') as f:
        return f.read().strip('\n')


def read_file_as_list(filename):
    with open(filename, 'r') as f:
        raw_list = f.readlines()
    return [r.strip('\n') for r in raw_list]


def read_file_as_list_of_lists(filename):
    return [r.split(',') for r in read_file_as_list(filename)]


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
