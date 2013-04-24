

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
    def __setitem__(self, index, value):
        self._rows[index] = value
        return self
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
    def square_to_box(self, square):
        sq = self.square(square)
        box = []
        for i in sq:
            for j in i:
                box.append( j)
        return box
    def row_consistent(self, row):
        "any non-zero entry should be unique"
        return self.unique_non_zero(self[row])
    def col_consistent(self, col):
        return self.unique_non_zero(self.col(col))
    def square_consistent(self, square):
        return self.unique_non_zero(self.square_to_box(square))
    def has_zero_in(self, box):
        for i in box:
            if i == 0:
                return True
        return False
    def consistent(self):
        for i in range(9):
            if not self.row_consistent(i):
                return False
            if not self.col_consistent(i):
                return False
            if not self.square_consistent(i):
                return False
        return True
    def has_zero(self):
        for i in range(9):
            if self.has_zero_in(self.row(i)):
                return True
        return False
    def zeros(self):
        result = []
        if self.has_zero():
            for row in range(9):
                for col in range(9):
                    if self[row][col] == 0:
                        result.append( (row, col))
        return result
    def solved(self):
        if self.consistent() and not self.has_zero():
            return True
        else:
            return False


class SudokuSolver():
    def possible(self, puzzle, row, col):
        if puzzle[row][col] != 0:
            return [puzzle[row][col]]
        else:
            possibilities = []
            for i in range(1,10):
                puzzle[row][col] = i
                if puzzle.consistent():
                    possibilities.append(i)
            puzzle[row][col] = 0
            return possibilities
    def try_value(self, puzzle, row, col, value):
        if 0 > row or 0 > col or 8 < row or 8 < col:
            raise IndexError
        if puzzle[row][col] != 0:
            raise ValueError
        elif value < 1 or value > 9:
            raise ValueError
        else:
            puzzle[row][col] = value
            if puzzle.consistent():
                return (puzzle, True)
            else:
                puzzle[row][col] = 0
                return (puzzle, False)
    def solve(self, puzzle):
        # todo : refactor this mess!
        """ goal : if puzzle solved, stop, return puzzle.
        otherwise : find a zero cell [row][col] with smallest number of possibilities
        and for each p in possibilities, try_value p on that cell.
        if second value was true, solve puzzle
        otherwise, it was false, try next value.
        we only need to check the shortest possible list, since if we can't satisfy this,
        we can't succeed at all.
        """
        # base case : just push this back up the stack
        if puzzle.solved():
            return puzzle
        if not puzzle.consistent():
            return None
        possibilities = []
        min_list = None
        min_location = (None, None)
        for row, col in puzzle.zeros():
            current = self.possible(puzzle, row, col)
            """ if there is only one possibility for a cell, try it. If it fails, we've gone the wrong way"""
            if len(current) == 1:
                puzzle[row][col] = current[0]
                check = self.solve(puzzle)
                if check:
                    return check
                else: 
                    # reset this guess and go up the stack
                    puzzle[row][col] = 0
                    return None
            if not min_list or len(current) < len(min_list):
                min_list = current
                min_location = (row, col)
            possibilities.append( (row, col, current))
        """ now we have all the unsolved locations, and the shortest one """
        row, col  = min_location
        for p in min_list:
            puzz, worked = self.try_value(puzzle, row, col, p)
            if worked:
                if self.solve(puzz):
                    return puzz
        puzzle[row][col] = 0
        return None

def SudokuReader(fileobj):
        """fileobj should be open and readable. You've been warned.
        I won't close it, so you have to."""
        result = Sudoku()
        counter = 0
        for line in fileobj:
            if counter > 8:
                break
            line_list = []
            for char in line:
                if char and char != '\n':
                    line_list.append(int(char))
            if len(line_list) == 9:
                result[counter] = line_list
                counter += 1
            else:
                raise ValueError("Not enough values in line " + str(counter))
        return result

def SudokuWriter(fileobj, puzzle):
    for row in range(9):
        for col in range(9):
            fileobj.write(str(puzzle[row][col]))
        fileobj.write('\n')
    return True