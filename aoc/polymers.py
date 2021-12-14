import re
from .aoc_helpers import distinct_counts, add_dicts


class Polymerizer():
    def __init__(self, insertion_rules_string):
        insertion_rules = re.findall(r'(\w\w) -> (\w)', insertion_rules_string)
        self.insertion_rules = {r[0]: r[1] for r in insertion_rules}
        self.cache = {}

    def apply_rules_to_template(self, polymer_template):
        polymer_entries = []

        for idx in range(len(polymer_template) - 1):
            polymer_entries.append((idx, polymer_template[idx]))
            pair = polymer_template[idx:idx + 2]
            if pair in self.insertion_rules:
                polymer_entries.append((idx + 0.5, self.insertion_rules[pair]))

        polymer_entries.append((idx + 1, polymer_template[-1]))
        polymer_entries.sort()

        return ''.join([p[1] for p in polymer_entries])

    def polymerize(self, polymer_template, num_steps):
        for k in range(num_steps):
            polymer_template = self.apply_rules_to_template(polymer_template)
        return polymer_template

    def polymerized_pair_count(self, pair, num_steps):
        if (pair, num_steps) in self.cache:
            return self.cache[(pair, num_steps)]

        else:

            if pair not in self.insertion_rules:
                counts = distinct_counts(pair)

            elif num_steps == 1:
                counts = distinct_counts([pair[0], pair[1],
                                          self.insertion_rules[pair]])

            else:
                insertion = self.insertion_rules[pair]
                left = self.polymerized_pair_count(pair[0] + insertion,
                                                   num_steps - 1)
                right = self.polymerized_pair_count(insertion + pair[1],
                                                    num_steps - 1)
                counts = add_dicts(left, right)
                counts[insertion] -= 1

            self.cache[(pair, num_steps)] = counts
            return counts

    def counts_after_polymerization(self, polymer_template, num_steps):
        scores = {}

        for idx in range(len(polymer_template) - 1):
            pair = polymer_template[idx: idx + 2]
            scores_idx = self.polymerized_pair_count(pair, num_steps)
            scores = add_dicts(scores, scores_idx)

        # Correct for repeated characters
        for char in polymer_template[1:-1]:
            scores[char] -= 1

        return scores

    def score_after_polymerization(self, polymer_template, num_steps):
        element_counts = self.counts_after_polymerization(polymer_template,
                                                          num_steps)
        ordered_counts = sorted([(v, k) for k, v in element_counts.items()])
        return ordered_counts[-1][0] - ordered_counts[0][0]
