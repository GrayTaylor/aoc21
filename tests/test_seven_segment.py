import pathmagic  # noqa: E402
import aoc

d8_example = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
d8_example_symbol_list = aoc.get_symbol_list(d8_example)
d8_output_symbols = aoc.get_output_symbols(d8_example)


def check_parsing():
    expected_set = set('acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab',
                       'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab')
    expected_output = set('cdfeb', 'fcadb', 'cdfeb', 'cdbaf')
    assert set(d8_example_symbol_list) == expected_set
    assert set(d8_output_symbols) == expected_output


def test_wiring():
    wiring = aoc.determine_wiring(d8_example_symbol_list)
    assert wiring['d'] == 'a'
    assert wiring['e'] == 'b'
    assert wiring['a'] == 'c'
    assert wiring['f'] == 'd'
    assert wiring['g'] == 'e'
    assert wiring['b'] == 'f'
    assert wiring['c'] == 'g'


def test_decoding():
    wiring = aoc.determine_wiring(d8_example_symbol_list)
    assert aoc.decode_output('cdfeb', wiring) == 5
    assert aoc.decode_output('fcadb', wiring) == 3
    assert aoc.decode_output('cdbaf', wiring) == 3


def test_valuing():
    assert aoc.get_line_value(d8_example) == 5353
