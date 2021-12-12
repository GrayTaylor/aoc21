import pathmagic  # noqa: E402
import aoc


examples = ['[({(<(())[]>[[{[]{<()<>>',
            '[(()[<>])]({[<{<<[]>>(',
            '{([(<{}[<>[]}>{[]{[(<()>',
            '(((({<>}<{<{<>}{[]{[]{}',
            '[[<[([]))<([[{}[[()]]]',
            '[{[{({}]{}}([{[{{{}}([]',
            '{<[[]]>}<{[{[{[]{()[[[]',
            '[<(<(<(<{}))><([]([]()',
            '<{([([[(<>()){}]>(<<{{',
            '<{([{{}}[<[[[<>{}]]]>[]]']


def test_corrupted():
    test_cases = {'{([(<{}[<>[]}>{[]{[(<()>': '}',
                  '[[<[([]))<([[{}[[()]]]': ')',
                  '[{[{({}]{}}([{[{{{}}([]': ']',
                  '[<(<(<(<{}))><([]([]()': ')',
                  '<{([([[(<>()){}]>(<<{{': '>'}

    for case, char in test_cases.items():
        assert aoc.first_illegal_char(case) == char


def test_score():
    assert aoc.score_illegal_first_chars(examples) == 26397


def test_autocomplete():
    test_cases = {'[({(<(())[]>[[{[]{<()<>>': '}}]])})]',
                  '[(()[<>])]({[<{<<[]>>(': ')}>]})',
                  '(((({<>}<{<{<>}{[]{[]{}': '}}>}>))))',
                  '{<[[]]>}<{[{[{[]{()[[[]': ']]}}]}]}>',
                  '<{([{{}}[<[[[<>{}]]]>[]]': '])}>'
                  }
    for case, completion in test_cases.items():
        assert ''.join(aoc.complete_line(case)) == completion


def test_autocomplete_scores():
    test_cases = {'}}]])})]': 288957,
                  ')}>]})': 5566,
                  '}}>}>))))': 1480781,
                  ']]}}]}]}>': 995444,
                  '])}>': 294}
    for completion, score in test_cases.items():
        assert aoc.score_autocomplete(completion) == score


def test_autocomplete_scores_all():
    example_incomplete = aoc.incomplete_lines(examples)
    assert aoc.score_incomplete_lines(example_incomplete) == 288957
