

class Grid():
    def __init__(self):
        self._rows = self.empty_grid()
    def empty_grid(self):
        "answer 9 lists of length 9, initialized to 0"
        return [[0] * 9 ] * 9
    def empty_square(self):
        "answer 3 lists of length 3, initialized to 0"
        return [[0] * 3] * 3
    def empty_squares(self):
        "answer a list of 9 squares"
        return [self.empty_square()] * 9
    def cols(self):
        cols = self.empty_grid()
        for col in range(9):
            for row in range(9):
                cols[col][row] = self.row(row)[col]
        return cols
    def col(self, n):
        if 0 <= n and n < 9:
            return self.cols()[n]
        else:
            raise IndexError
    def __getitem__(self, index):
        return self._rows[index]
    def rows(self):
        return self._rows
    def row(self, n):
        if 0 <= n and n < 9:
            return self._rows[n]
        else:
            raise IndexError
    def squares(self):
        squares = self.empty_squares()
        for square in range(9):
            row_offset = square / 3
            col_offset = (square % 3) * 3 - 1
            for row in range(3):
                for col in range(3):
                    squares[square][row][col] = self[row_offset + row][col_offset + col]
        return squares

        


class Sudoku(Grid):
    pass