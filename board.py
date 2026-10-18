class Board:
    def __init__(self, size=6):
        # TODO make this work for size other than 6
        self.size = size
        temp = [[" " for _ in range(self.size)] for _ in range(self.size)]
        temp[self.size//2 -1][self.size//2 -1] = "W"
        temp[self.size//2][self.size//2] = "W"
        temp[self.size//2 -1][self.size//2] = "B"
        temp[self.size//2][self.size//2 -1] = "B"
        self.board = temp
        self.turn = 1 # black goes first, -1 represents white

    
    def show_board(self):
        for row in self.board:
            print(row)


    def possible_moves(self):
        possible = []
        max_coord = self.size-1
        own = None
        opp = None
        emp = " "
        if self.turn == 1:
            own = "B"
            opp = "W"
        else:
            own = "W"
            opp = "B"

        def coord_incrementer(row, col, y_axis, x_axis):
            # check rows (change cols)
            checked = 0
            i = y_axis
            j = x_axis
            while  0 <= row+i <= max_coord and 0 <= col+j <= max_coord and self.board[row+i][col+j] == opp:
                i += y_axis
                j += x_axis
                checked += 1
            if 0 <= row+i <= max_coord and 0 <= col+j <= max_coord and self.board[row+i][col+j] == emp and checked >0 :
                possible.append((row+i,col+j))
                # self.board[row+i][col+j] = "X"

        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == own:
                    # check rows (change cols)
                    coord_incrementer(row, col, 0, 1)
                    coord_incrementer(row, col, 0, -1)
                    # check columns (change rows)
                    coord_incrementer(row, col, 1, 0)
                    coord_incrementer(row, col, -1, 0)
                    
                    # check diagonals (change row and -col, row and -col)
                    coord_incrementer(row, col, 1, 1)
                    coord_incrementer(row, col, 1, -1)
                    coord_incrementer(row, col, -1, 1)
                    coord_incrementer(row, col, -1, -1)
                    
        return possible


    def flipper(self, row, col, y_axis, x_axis):
        max_coord = self.size-1
        own = None
        opp = None
        emp = " "
        if self.turn == 1:
            own = "B"
            opp = "W"
        else:
            own = "W"
            opp = "B"
        checked = []
        max_coord = self.size
        i = y_axis
        j = x_axis
        while  0 <= row+i <= max_coord and 0 <= col+j <= max_coord and self.board[row+i][col+j] == opp:
            # self.board[row+i][col+j] = own
            checked.append((row+i, col+j))
            i += y_axis
            j += x_axis

        print(checked)

        if self.board[row+i][col+j] == own and len(checked) > 0:
            # print("flipping")
            for coord in checked:
                # print(coord)
                self.board[coord[0]][coord[1]] = own
        

    def move(self, row, col):
        # TODO implement pass mechanic while avoiding loop
        own = None
        opp = None
        emp = " "
        if self.turn == 1:
            own = "B"
            opp = "W"
        else:
            own = "W"
            opp = "B"
        if (row,col) in self.possible_moves():
            self.board[row][col] = own
            # flip rows
            self.flipper(row, col, 0, 1)
            self.flipper(row, col, 0, -1)
            
            # flip cols
            self.flipper(row, col, 1, 0)
            self.flipper(row, col, -1, 0)

            # flip diagonals
            self.flipper(row, col, 1, 1)
            self.flipper(row, col, -1, -1)
            self.flipper(row, col, 1, -1)
            self.flipper(row, col, -1, 1)

        self.turn *= -1
    
    def winner(self):
        # 1 -> black won
        # -1 -> white won
        # 0 -> draw
        # None -> hasn't concluded
        pass



if __name__ == "__main__":
    board = Board()
    # board.board[1][2] = "X"
    # print(board.possible_moves())
    board.show_board()
    print()
    board.move(2, 1)
    board.show_board()
    print()
    board.move(1,1)
    board.show_board()
