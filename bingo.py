class bingo_board:
    def __init__(self, board_entries):
        self.board_entries = board_entries
        self.reset()

    def __repr__(self):
        out_lines = ''
        for row in range(self.grid_size):
            out_row = [' ' + str(e) for e in self.board_entries[row]]
            for column in range(self.grid_size):
                if (row, column) in self.used_locations:
                    out_row[column] = ' X'
            out_line = ' '.join([e[-2:] for e in out_row])
            out_lines += out_line + '\n'
        return out_lines

    def reset(self):
        self.used_total = 0
        self.unused_total = 0
        self.value_locations = {}
        self.used_locations = {}

        self.grid_size = len(self.board_entries)  # assume square!
        for row in range(self.grid_size):
            for column in range(self.grid_size):
                entry = self.board_entries[row][column]
                self.unused_total += entry
                self.value_locations[entry] = (row, column)

    def process_call(self, call):
        if call in self.value_locations:
            self.used_total += call
            self.unused_total -= call
            location = self.value_locations[call]
            self.used_locations[location] = call

    def row_complete(self, row):
        for column in range(self.grid_size):
            if (row, column) not in self.used_locations:
                return False
        return True

    def column_complete(self, column):
        for row in range(self.grid_size):
            if (row, column) not in self.used_locations:
                return False
        return True

    def board_wins(self):
        for row in range(self.grid_size):
            if self.row_complete(row):
                return True

        for column in range(self.grid_size):
            if self.column_complete(column):
                return True

        return False


def score_winning_board(calls, bingo_boards):
    for b in bingo_boards:
        b.reset()  # ensures calls from any previous games are removed
    for idx, call in enumerate(calls):
        print(f'Round {idx} call {call}')

        for b in bingo_boards:
            b.process_call(call)

        winning_boards = [b for b in bingo_boards if b.board_wins()]
        if len(winning_boards) > 0:
            print('\nwinning board:')
            for b in winning_boards:
                print(b)
                print(f'Unmarked total {b.unused_total}')

            # Assume a single winner!
            return winning_boards[0].unused_total * call


def score_last_winning_board(calls, bingo_boards, verbose=False):
    for b in bingo_boards:
        b.reset()

    num_boards = len(bingo_boards)
    remaining_boards = bingo_boards
    winning_boards = []

    for idx, call in enumerate(calls):
        if verbose:
            print(f'Round {idx} call {call}')

        for b in remaining_boards:
            b.process_call(call)

        for b in remaining_boards:
            if b.board_wins:
                winning_boards.append(b)
        remaining_boards = [b for b in remaining_boards if not b.board_wins()]

        if len(remaining_boards) == 0:
            last_board = winning_boards[-1]
            if verbose:
                print('No boards left')
                print('Final entry was')
                print(last_board)
                print(f'Unmarked total {last_board.unused_total}')
            return last_board.unused_total * call

        else:
            if verbose:
                print(f'{len(remaining_boards)} boards remain')
