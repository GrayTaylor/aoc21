def read_file_as_list_of_lists(filename):
    with open(filename, 'r') as f:
        raw_list = f.readlines()
    stripped_list = [r.strip('\n') for r in raw_list]
    return [r.split(',') for r in stripped_list]


def read_file_as_string(filename):
    with open(filename, 'r') as f:
        return f.read().strip('\n')
