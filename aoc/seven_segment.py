def get_symbol_list(wire_line):
    return wire_line.split(' | ')[0].split(' ')


def get_output_symbols(wire_line):
    return wire_line.split(' | ')[1].split(' ')


def determine_wiring(symbols_seen):
    one_segments = [l for l in [s for s in symbols_seen if len(s) == 2][0]]
    seven_segments = [l for l in [s for s in symbols_seen if len(s) == 3][0]]
    four_segments = [l for l in [s for s in symbols_seen if len(s) == 4][0]]
    eight_segments = [l for l in [s for s in symbols_seen if len(s) == 7][0]]

    # a is the only segment used by seven but not one, so we can learn a
    a_map = [seg for seg in seven_segments if seg not in one_segments][0]

    # 3 symbols use 6 segments
    # zero uses all except d, six all except c, nine all except e
    # So we can find the set (c,d,e).
    # Of those, c and d appear in four but e does not, so we can learn e
    length_6_symbols = [s for s in symbols_seen if len(s) == 6]
    cde_candidates = []
    for s in length_6_symbols:
        cde_candidates.extend([l for l in 'abcdefg' if l not in s])
    e_map = [seg for seg in cde_candidates if seg not in four_segments][0]

    # 3 symbols use 5 segments
    # two is missing b,f; three is missing b,e; five is missing c,e
    # so the only 5 segment symbol with an e is two
    # and we know what e maps to, so we can identify the symbol for two
    length_5_symbols = [s for s in symbols_seen if len(s) == 5]
    length_5_symbols_with_e = [s for s in length_5_symbols if e_map in s][0]
    two_segments = [seg for seg in length_5_symbols_with_e]

    # f is the segment used in one but not in two
    # c is the other segment of one
    f_map = [seg for seg in one_segments if seg not in two_segments][0]
    c_map = [seg for seg in one_segments if seg != f_map][0]

    # we know 2 segments of four, the others must be b and d
    # d is in two, but b is not
    bd_candidates = [seg for seg in four_segments if seg not in [c_map, f_map]]
    d_map = [seg for seg in bd_candidates if seg in two_segments][0]
    b_map = [seg for seg in bd_candidates if seg not in two_segments][0]

    # g is whatever is still left
    g_map = [seg for seg in 'abcdefg'
             if seg not in [a_map, b_map, c_map, d_map, e_map, f_map]][0]

    # return a dictionary that translates _back_ to correct segments from
    # segments observed after this rewiring
    return {a_map: 'a', b_map: 'b', c_map: 'c', d_map: 'd',
            e_map: 'e', f_map: 'f', g_map: 'g'}


def decode_output(output, correct_wire):
    unscrambled_segments = ''.join(sorted([correct_wire[c] for c in output]))
    standard_segments = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf',
                         'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    if unscrambled_segments not in standard_segments:
        raise ValueError(f"can't parse {unscrambled_segments}")
    else:
        return standard_segments.index(unscrambled_segments)


def get_line_value(wire_line):
    symbols = get_symbol_list(wire_line)
    outputs = get_output_symbols(wire_line)
    correct_wiring = determine_wiring(symbols)
    output_values = [decode_output(s, correct_wiring) for s in outputs]
    return sum([output_values[k] * 10**(3-k) for k in range(4)])
