import pathmagic  # noqa: E402
import aoc

example_network1 = ['start-A',
                    'start-b',
                    'A-c',
                    'A-b',
                    'b-d',
                    'A-end',
                    'b-end']

example_network2 = ['dc-end',
                    'HN-start',
                    'start-kj',
                    'dc-start',
                    'dc-HN',
                    'LN-dc',
                    'HN-end',
                    'kj-sa',
                    'kj-HN',
                    'kj-dc']

example_network3 = ['fs-end',
                    'he-DX',
                    'fs-he',
                    'start-DX',
                    'pj-DX',
                    'end-zg',
                    'zg-sl',
                    'zg-pj',
                    'pj-he',
                    'RW-he',
                    'fs-DX',
                    'pj-RW',
                    'zg-RW',
                    'start-pj',
                    'he-WI',
                    'zg-he',
                    'pj-fs',
                    'start-RW']

example_cave1 = aoc.CaveNetwork(example_network1)
example_cave2 = aoc.CaveNetwork(example_network2)
example_cave3 = aoc.CaveNetwork(example_network3)


def test_num_paths_s1():
    assert len(example_cave1.find_start_to_end(mode='d12s1')) == 10
    assert len(example_cave2.find_start_to_end(mode='d12s1')) == 19
    assert len(example_cave3.find_start_to_end(mode='d12s1')) == 226


def test_num_paths_s2():
    assert len(example_cave1.find_start_to_end(mode='d12s2')) == 36
    assert len(example_cave2.find_start_to_end(mode='d12s2')) == 103
    assert len(example_cave3.find_start_to_end(mode='d12s2')) == 3509
