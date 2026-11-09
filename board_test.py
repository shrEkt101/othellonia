import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def testBoardInit(self):
        board = Board()
        expected = [
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", "W", "B", " ", " "],
            [" ", " ", "B", "W", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
        ]
        self.assertEqual(board.board, expected)

    def testBoardFlip1(self):
        board = Board()
        board.move(4, 3)
        expected = [
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", "W", "B", " ", " "],
            [" ", " ", "B", "B", " ", " "],
            [" ", " ", " ", "B", " ", " "],
            [" ", " ", " ", " ", " ", " "],
        ]
        self.assertEqual(board.board, expected)

    def testBoardFlip2(self):
        board = Board()
        board.board = [
            [" ", "W", "W", "W", "W", "B"],
            ["W", "W", " ", " ", " ", " "],
            ["W", " ", "W", " ", " ", " "],
            ["W", " ", " ", "W", " ", " "],
            ["W", " ", " ", " ", "W", " "],
            ["B", " ", " ", " ", " ", "B"],
        ]
        board.move(0, 0)
        expected = [
            ["B", "B", "B", "B", "B", "B"],
            ["B", "B", " ", " ", " ", " "],
            ["B", " ", "B", " ", " ", " "],
            ["B", " ", " ", "B", " ", " "],
            ["B", " ", " ", " ", "B", " "],
            ["B", " ", " ", " ", " ", "B"],
        ]
        self.assertEqual(board.board, expected)

    def testBoardFlip3(self):
        board = Board()
        board.board = [
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", "W", "W", "W", " "],
            [" ", " ", "B", "B", " ", " "],
            [" ", " ", " ", "B", " ", " "],
            [" ", " ", " ", " ", " ", " "],
        ]
        expected = [
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", "B"],
            [" ", " ", "W", "W", "B", " "],
            [" ", " ", "B", "B", " ", " "],
            [" ", " ", " ", "B", " ", " "],
            [" ", " ", " ", " ", " ", " "],
        ]
        board.move(1, 5)
        self.assertEqual(board.board, expected)

    def testBoardFlip4(self):
        board = Board()
        board.turn = -1
        board.board = [
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", "W", " ", " ", " "],
            [" ", "W", "B", "B", "B", " "],
            ["W", "W", "B", "W", "W", " "],
            [" ", "B", " ", "B", " ", " "],
            [" ", "B", "W", " ", "B", " "],
        ]
        expected = [
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", "W", " ", " ", " "],
            [" ", "W", "W", "B", "B", " "],
            ["W", "W", "W", "W", "W", " "],
            [" ", "B", "W", "B", " ", " "],
            [" ", "B", "W", " ", "B", " "],
        ]
        board.move(4, 2)
        self.assertEqual(board.board, expected)

    def testBoardFlip5(self):
        board = Board()
        board.turn = -1
        board.board = [
            [" ", "B", "B", "B", "B", " "],
            ["W", " ", "B", " ", "W", " "],
            ["W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "B", "W"],
            [" ", "W", "W", "B", "W", "W"],
            ["W", "W", "W", "W", "W", "W"],
        ]
        expected = []
        self.assertEqual(board.possible_moves(), expected)

    def testBoardFlip5(self):
        board = Board()
        board.board = [
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", "B", " ", " "],
            [" ", " ", " ", "W", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", "B", "W", " ", " "],
        ]
        board.move(4, 3)
        expected = [
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", "B", " ", " "],
            [" ", " ", " ", "B", " ", " "],
            [" ", " ", " ", "B", " ", " "],
            [" ", " ", "B", "W", " ", " "],
        ]
        self.assertEqual(board.board, expected)

    def testWinner1(self):
        """
        if neither side can play anything, winner can be decided
        --> calculate possible moves for each perspective and see they are both empty.
        """
        board = Board()
        board.board = [
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", "B", "B", " ", " "],
            [" ", " ", "B", "B", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
        ]
        self.assertEqual(board.winner(), 1)


if __name__ == "__main__":
    unittest.main()
