import unittest
from minmax import MinMax
from board import Board


class MinMaxTest(unittest.TestCase):
    # def testTermination1(self):
    #     board = Board()
    #     board.board = [
    #         [" ", " ", " ", " ", " ", " "],
    #         [" ", " ", " ", " ", " ", " "],
    #         [" ", " ", "B", "B", " ", " "],
    #         [" ", " ", "B", "B", " ", " "],
    #         [" ", " ", " ", " ", " ", " "],
    #         [" ", " ", " ", " ", " ", " "],
    #     ]
    #     minmax = MinMax()
    #     # eval from B's POV
    #     output = minmax.move_evals(board, True)
    #     self.assertEqual(output, (1, None, (4, 0)))

    #     # eval from W's POV
    #     output = minmax.move_evals(board, False)
    #     self.assertEqual(output, (-1, None, (4, 0)))

    def testTermination2(self):
        board = Board()
        board.board = [
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", "B", "B", " ", " "],
            [" ", " ", "B", "B", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
        ]
        minmax = MinMax()
        # eval from B's POV
        output = minmax.move_evals(board, True)
        self.assertEqual(output, 1)

        # eval from W's POV
        output = minmax.move_evals(board, False)
        self.assertEqual(output, -1)

    def testTermination3(self):
        board = Board()
        board.board = [
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", "W", "B", " ", " "],
            [" ", " ", "B", "B", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
        ]
        minmax = MinMax()
        # eval from B's POV
        output = minmax.move_evals(board, True)
        self.assertEqual(output, 1)

        # eval from W's POV
        # output = minmax.move_evals(board, False)
        # self.assertEqual(output, 1)
