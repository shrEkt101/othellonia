"""
We want to use the minmax algorithm as a starter to find which moves lead to optimal play.
It would be nice if we could display what coordinates leds to winning or losing by X pieces.

Problems:
- how do we handle passes?
- board winner is not statically evaluated right now

ideas:
- In the base case, we should get that winner is not None
    - return the winner, along with the piece counts: (winner, (black_count, white_count))
- Otherwise (if winner undecided), for each move, make that move on a copy and evaluate each move.
"""

from board import Board
import copy


class MinMax:
    def __init__(self):
        self.table = {}

    def move_evals(self, board: Board, maximizer=True, verbose=False):
        """
        minmax using absolute evaluation of board state.
        That is, a terminal board state gives the same eval regarless of pov.
            e.g. all black -> evaluates to 1 for both black and white pov.

        black is the maximizer and white is the minimizer.

        usecase:
            board = Board()
            minmax = MinMax()
            print(minmax.move_evals())

            >>> ( (0, (1,2), (16,16)), ...)
            (eval, move, counts)
        """
        if verbose:
            board.show_board()
            print()

        if str(board.board) in self.table:
            return self.table[str(board.board)]
        else:
            winner = board.winner()
            if winner is not None:
                # base case
                # if maximizer:
                #     # current POV is black's
                #     return winner
                # else:
                #     # current POV is white's
                #     return -winner
                self.table[str(board.board)] = winner
                return winner
            else:
                # evaluate for each move available and return the max or min
                next_player = None
                if maximizer:
                    next_player = False
                else:
                    next_player = True
                possible = board.possible_moves()

                if len(possible) == 0:
                    # need to pass
                    temp = copy.deepcopy(board)
                    temp.turn *= -1
                    result = self.move_evals(temp, next_player, verbose)
                    self.table[str(board.board)] = result
                    return result

                # print(possible)
                evals = []
                for move in possible:
                    temp = copy.deepcopy(board)
                    temp.move(move[0], move[1])
                    temp.turn *= -1
                    result = self.move_evals(temp, next_player, verbose)
                    self.table[str(temp.board)] = result
                    evals.append(result)
                final = None
                if maximizer:
                    final = max(evals)
                else:
                    final = min(evals)
                return final


if __name__ == "__main__":
    board = Board()
    board.board = [
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", "W", "W", " ", " "],
        [" ", " ", "W", "W", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
    ]
    minmax = MinMax()
    print(minmax.move_evals(board, True, True))
    print(minmax.table.values())
