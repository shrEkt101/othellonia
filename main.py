# goal: use minmax to figure out which moves are optimal
from board import Board


def ask_input(turn):
    x, y = None, None
    while True:
        try:
            coord = input(
                f"for {turn}, enter a coordinate in the format (row, col), zero-indexed: "
            ).split(",")
            x, y = int(coord[0]), int(coord[1])
            break
        except Exception:
            pass
    return (x, y)


def main():
    """
    Main flow:
    1. play move (flip)
    2. check winner
        2.1 update turn
    """
    board = Board()
    board.board = [
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", "W", "B", " ", " "],
        [" ", " ", "B", "B", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
    ]
    winner = None
    while winner is None:

        board.show_board()
        possible_moves = board.possible_moves()
        print(possible_moves)

        x, y = None, None
        while True:
            if board.turn == 1:
                x, y = ask_input("white")
            else:
                x, y = ask_input("black")
            if (x, y) in possible_moves:
                break
        board.move(x, y)
        winner = board.winner()
        board.turn *= -1
    board.show_board()
    print(winner)


if __name__ == "__main__":
    main()
