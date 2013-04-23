

class Grid():
    def __init__(self):
        self._rows = self.empty_grid()
    def empty_grid(self):
        return [[0] * 9 ] * 9
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

class Sudoku(Grid):
    pass