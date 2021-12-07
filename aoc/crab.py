def crab_fuel_cost(crab_location, target_location, mode='linear'):
    if mode == 'linear':
        return abs(crab_location - target_location)
    elif mode == 'triangular':
        d = abs(crab_location - target_location)
        return d * (d + 1) / 2
    else:
        raise ValueError(f'Unexpected mode {mode}')


def total_crab_fuel_costs(crab_locations, target_location, mode='linear'):
    return sum([crab_fuel_cost(l, target_location, mode)
                for l in crab_locations])


def cheapest_crab_target(crab_locations, mode='linear'):
    start_location = min(crab_locations)
    end_location = max(crab_locations)
    best_cost = total_crab_fuel_costs(crab_locations, start_location, mode)
    best_target = start_location

    for t in range(start_location + 1, end_location + 1):
        fuel_cost = total_crab_fuel_costs(crab_locations, t, mode)
        if fuel_cost < best_cost:
            best_cost = fuel_cost
            best_target = t

    return best_target
