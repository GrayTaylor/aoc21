import aoc.aoc_helpers as aoch


def rate(list_of_bit_strings, rate):
    assert rate in ['gamma', 'epsilon']
    num_bits = len(list_of_bit_strings[0])

    if rate == 'gamma':
        bits = [aoch.most_common_entry([s[k] for s in list_of_bit_strings])
                for k in range(num_bits)]
    elif rate == 'epsilon':
        bits = [aoch.least_common_entry([s[k] for s in list_of_bit_strings])
                for k in range(num_bits)]
    else:
        bits = ['0']

    bit_string = ''.join([d for d in bits])
    return int(bit_string, base=2)


def rating(list_of_bit_strings, rating, verbose=False):
    assert rating in ['oxygen_generator', 'co2_scrubber']

    found_bits = ''
    candidates = [s for s in list_of_bit_strings]

    while len(candidates) > 1:
        if rating == 'co2_scrubber':
            desired_bit = aoch.least_common_entry([c[0] for c in candidates])
        else:
            desired_bit = aoch.most_common_entry([c[0] for c in candidates])

        candidates = [c[1:] for c in candidates if c[0] == desired_bit]
        found_bits += desired_bit
        if verbose:
            msg = f'Starting condition {found_bits}'
            msg += f' leaves {len(candidates)} strings'
            print(msg)

    final_string = found_bits + candidates[0]
    if verbose:
        print(f'Conditioning on {found_bits} leaves one string {final_string}')
    return int(final_string, base=2)
