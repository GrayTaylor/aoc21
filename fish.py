import aoc_helpers as aoc


class LanternfishSchool:
    def __init__(self, initial_states):
        self.possible_states = [k for k in range(9)]
        self.initial_states = initial_states
        self.reset()

    def reset(self):
        self.state_counts = {s: 0 for s in self.possible_states}
        self.initial_state_counts = aoc.distinct_counts(self.initial_states)
        for state, count in self.initial_state_counts.items():
            self.state_counts[state] = count
        self.num_days = 0

    def total_fish(self):
        return sum([c for _, c in self.state_counts.items()])

    def __repr__(self):
        summary = f'After {self.num_days} days, {self.total_fish()} fish:\n'
        return summary + str(self.state_counts)

    def advance_day(self):
        new_state_counts = {k: 0 for k in range(9)}
        for k in range(1, 9):
            new_state_counts[k - 1] = self.state_counts[k]
        new_state_counts[8] = self.state_counts[0]
        new_state_counts[6] += self.state_counts[0]
        self.num_days += 1
        self.state_counts = new_state_counts

    def set_to_day_n(self, n):
        self.reset()
        for _ in range(n):
            self.advance_day()
