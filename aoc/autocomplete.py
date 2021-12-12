from .aoc_helpers import *


def first_illegal_char(line):
    closes = {']': '[', ')': '(', '}': '{', '>': '<'}
    pending = [line[0]]
    for char in line[1:]:
        if char in ['[', '{', '(', '<']:
            pending.append(char)
        else:
            if pending[-1] != closes[char]:
                return char
            else:
                pending = pending[:-1]
    return None


def score_illegal_first_chars(lines):
    first_illegal_chars = [first_illegal_char(l) for l in lines]
    first_illegal_chars = [c for c in first_illegal_chars if c is not None]
    char_counts = distinct_counts(first_illegal_chars)
    scores = {']': 57, ')': 3, '}': 1197, '>': 25137}
    return sum([scores[c]*char_counts[c] for c in char_counts])


def incomplete_lines(lines):
    return [l for l in lines if first_illegal_char(l) is None]


def build_pending_queue(line):
    closes = {']': '[', ')': '(', '}': '{', '>': '<'}
    pending = [line[0]]
    for char in line[1:]:
        if char in ['[', '{', '(', '<']:
            pending.append(char)
        else:
            if pending[-1] != closes[char]:
                raise ValueError('line was corrupt, not incomplete')
            else:
                pending = pending[:-1]
    return pending


def complete_line(line):
    pending = build_pending_queue(line)
    pending.reverse()
    closer = {'[': ']', '(': ')', '{': '}', '<': '>'}
    return [closer[char] for char in pending]


def score_autocomplete(completion):
    score = 0
    char_score = {']': 2, ')': 1, '}': 3, '>': 4}
    for char in completion:
        score *= 5
        score += char_score[char]
    return score


def score_incomplete_line(line):
    return score_autocomplete(complete_line(line))


def score_incomplete_lines(lines):
    scores = [score_incomplete_line(l) for l in lines]
    scores.sort()
    return scores[int((len(scores) - 1) / 2)]
