import re


def directions_from_string(raw_directions):
    # Find anything that looks like a direction, a space, and a number
    directions = re.findall(r'(forward |up |down )(\d+)', raw_directions)
    return [[d[0].strip(), int(d[1])] for d in directions]


def generate_journey(directions, mode='d2s2'):
    '''
    Given a list of directions of the form [forward/up/down, N],
    return a list of the locations visited of the form [position, depth].

    mode is of the form dNsM, where N is the day and M is the star
    (so, currently, options are d1s1 and d1s2)
    '''
    depth = 0
    horizontal = 0
    aim = 0
    journey = []

    for step in directions:
        if len(step) == 0:
            print('skipping blank instruction ', step)
        if len(step[0]) == 0:
            print('skipping blank instruction ', step)
        elif step[0][0] == 'd':
            if mode == 'd2s1':
                depth += step[1]
            else:
                aim += step[1]
        elif step[0][0] == 'u':
            if mode == 'd2s1':
                depth -= step[1]
            else:
                aim -= step[1]
        elif step[0][0] == 'f':
            horizontal += step[1]
            if mode == 'd2s2':
                depth += aim * step[1]
        else:
            print('got unexpected instruction ', step)

        journey.append([horizontal, depth])

    return journey
