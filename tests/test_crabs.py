import pathmagic  # noqa: E402
import aoc

d7_crab_positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_d7s1_fuel():
    expected_fuel_move_to_2 = {16: 14, 1: 1, 2: 0, 0: 2, 4: 2, 7: 5, 14: 12}
    for k, v in expected_fuel_move_to_2.items():
        assert aoc.crab_fuel_cost(k, 2, mode='linear') == v


def test_d7s1_locations():
    assert aoc.total_crab_fuel_costs(d7_crab_positions, 2, 'linear') == 37
    assert aoc.total_crab_fuel_costs(d7_crab_positions, 1, 'linear') == 41
    assert aoc.total_crab_fuel_costs(d7_crab_positions, 3, 'linear') == 39
    assert aoc.total_crab_fuel_costs(d7_crab_positions, 10, 'linear') == 71


def test_d7s1_best_location():
    assert aoc.cheapest_crab_target(d7_crab_positions, mode='linear') == 2


def test_d7s2_fuel():
    expected_fuel_move_to_5 = {16: 66, 1: 10, 2: 6, 0: 15, 4: 1, 7: 3, 14: 45}
    for k, v in expected_fuel_move_to_5.items():
        assert aoc.crab_fuel_cost(k, 5, mode='triangular') == v


def test_d7s2_locations():
    assert aoc.total_crab_fuel_costs(d7_crab_positions, 5, 'triangular') == 168
    assert aoc.total_crab_fuel_costs(d7_crab_positions, 2, 'triangular') == 206


def test_d7s2_best_location():
    assert aoc.cheapest_crab_target(d7_crab_positions, mode='triangular') == 5
