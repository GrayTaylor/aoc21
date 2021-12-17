def get_packets(packet_string, verbose=False):
    packets = []
    while len(packet_string) >= 11:
        new_packet, packet_string = get_next_packet_and_tail(packet_string,
                                                             verbose)
        packets.append(new_packet)
    return packets


def get_next_packet_and_tail(packet_string, verbose=False):

    version = int(packet_string[:3], 2)
    type_ID = int(packet_string[3:6], 2)

    if type_ID == 4:

        locator = 6

        bits_of_literal = ''
        while packet_string[locator] == '1':
            bits_of_literal += packet_string[locator + 1: locator + 5]
            locator += 5
        # one more set of bits for literal
        bits_of_literal += packet_string[locator + 1: locator + 5]
        locator += 5

        literal = int(bits_of_literal, 2)

        if verbose:
            print(f'This packet is a literal with bits {bits_of_literal}')

        packet = {'version': version, 'type_ID': type_ID, 'type': 'literal',
                  'literal': literal}
        tail = packet_string[locator:]
        return packet, tail

    else:
        length_type_ID = packet_string[6]

        if length_type_ID == '0':
            sub_packet_length = int(packet_string[7:22], 2)
            if verbose:
                print(f'Operator with {sub_packet_length} bits as subpackets')

            sub_packet_bits = packet_string[22: 22 + sub_packet_length]
            sub_packets = get_packets(sub_packet_bits)

            packet = {'version': version, 'type_ID': type_ID,
                      'type': 'operator', 'sub_packets': sub_packets}
            tail = packet_string[22 + sub_packet_length:]
            return packet, tail

        else:
            num_sub_packets = int(packet_string[7:18], 2)
            if verbose:
                print(f'Operator with {num_sub_packets} sub_packets')

            tail = packet_string[18:]
            sub_packets = []

            for k in range(num_sub_packets):
                next_sub_packet, tail = get_next_packet_and_tail(tail)
                sub_packets.append(next_sub_packet)

            packet = {'version': version, 'type_ID': type_ID,
                      'type': 'operator', 'sub_packets': sub_packets}
            return packet, tail


def version_sum(packet):
    if packet['type'] == 'literal':
        return packet['version']

    elif packet['type'] == 'operator':
        return packet['version'] + sum([version_sum(p)
                                        for p in packet['sub_packets']])


def packets_version_sum(packets):
    return sum([version_sum(p) for p in packets])


def value_packet(packet):
    if packet['type'] == 'literal':
        return packet['literal']
    elif packet['type'] == 'operator':
        sub_packet_values = [value_packet(p) for p in packet['sub_packets']]
        if packet['type_ID'] == 0:
            return sum(sub_packet_values)
        elif packet['type_ID'] == 1:
            product = 1
            for v in sub_packet_values:
                product *= v
            return product
        elif packet['type_ID'] == 2:
            return min(sub_packet_values)
        elif packet['type_ID'] == 3:
            return max(sub_packet_values)
        elif packet['type_ID'] == 5:
            if sub_packet_values[0] > sub_packet_values[1]:
                return 1
            else:
                return 0
        elif packet['type_ID'] == 6:
            if sub_packet_values[0] < sub_packet_values[1]:
                return 1
            else:
                return 0
        elif packet['type_ID'] == 7:
            if sub_packet_values[0] == sub_packet_values[1]:
                return 1
            else:
                return 0
        else:
            raise ValueError(f"Unexpected type_ID={packet['type_ID']}")
