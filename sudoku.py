

class Grid():
    def __init__(self):
        self._rows = self.empty_grid()
    def empty_grid(self):
        "answer 9 lists of length 9, initialized to 0"
        result = []
        for i in range(9):
            result += [[0] * 9 ]
        return result
    def empty_square(self):
        "answer 3 lists of length 3, initialized to 0"
        result = []
        for i in range(3):
            result += [[0] * 3]
        return result
    def empty_squares(self):
        "answer a list of 9 squares"
        return [self.empty_square()] * 9
    def cols(self):
        cols = self.empty_grid()
        for col in range(9):
            for row in range(9):
                cols[col][row] = self[row][col]
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
        squares = []
        for n in range(9):
            squares.append(self.square(n))
        return squares
    def square(self, n):
        if n < 0 or n > 8:
            raise IndexError
        else:
            col_offset = 3 * (n % 3)
            row_offset = 3 * (n // 3)
            square = self.empty_square()
            for row in range(3):
                for col in range(3):
                    square[row][col] = self[row + row_offset][col + col_offset]
            return square

class Sudoku(Grid):
    def unique_non_zero(self, box):
        for i in range(len(box)):
            if box[i] != 0 and box[i] in box[i+1:]:
                return False
        return True
    def row_consistent(self, row):
        "any non-zero entry should be unique"
        return self.unique_non_zero(self[row])
    def col_consistent(self, col):
        return self.unique_non_zero(self.col(col))
    def square_consistent(self, square):
        sq = self.square(square)
        box = []
        for i in sq:
            for j in i:
                box.append( j)
        return self.unique_non_zero(box)