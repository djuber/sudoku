import unittest
from sudoku import Grid, Sudoku, SudokuSolver

class GridTests(unittest.TestCase):
    def setUp(self):
        "wherein we create a board with numbers in it"
        self.puzzle = Grid()
        self.empty = Grid()
        for row in range(9):
            for col in range(9):
                self.puzzle[row][col] = (1 + (row + col) % 9)
    def test_class_exists(self):
        "verifies a class Sudoku exists"
        self.assertTrue(self.puzzle)
    def test_rows_gives_an_answer(self):
        self.assertEqual(9, len(self.puzzle.rows()))
    def test_initialized_to_zero(self):
        "verifies initially zeroed board"
        self.assertEqual([0] * 9, self.empty[0])
    def test_puzzle_row_initialized(self):
        self.assertEqual([1,2,3,4,5,6,7,8,9], self.puzzle[0])
    def test_row_access_raises_IndexError(self):
        self.assertRaises(IndexError, self.puzzle.row, 10)
    def test_col_access_raises_IndexErro(self):
        self.assertRaises(IndexError, self.empty.col, 9)
    def test_puzzle_element_initialized(self):
        self.assertEqual(1, self.puzzle[0][0])
        self.assertEqual(8, self.puzzle[8][8])
    def test_puzzle_is_symmetric(self):
        self.assertEqual(self.puzzle.col(4), self.puzzle.row(4))
    def test_cols_gives_an_answer(self):
        self.assertEqual(9, len(self.puzzle.cols()))
    def test_empty_col(self):
        self.assertEqual([0]*9, self.empty.col(0))
    def test_col(self):
        self.assertEqual([1,2,3,4,5,6,7,8,9], self.puzzle.col(0))
        self.assertEqual(5, self.puzzle.col(4)[0])
    def test_getitem_returns_row(self):
        self.assertEqual(self.puzzle.row(0), self.puzzle[0])
    def test_getitem_sufficient_for_setitem(self):
        """
        since getitem returns row as a list, setitem on the list should
        be transparent. Test is trivial, if it didn't work, we'd see a syntax error.
        """
        self.puzzle[0][0] = 1
        self.assertEqual(1, self.puzzle[0][0])
    def test_empty_square(self):
        self.assertEqual(3, len(self.puzzle.empty_square()))
        self.assertEqual(3, len(self.puzzle.empty_square()[0]))
    def test_empty_squares(self):
        self.assertEqual(9, len(self.puzzle.empty_squares()))
    def test_squares_gives_answer(self):
        self.assertTrue(self.puzzle.squares())
    def test_squares_access(self):
        self.assertEqual(1, self.puzzle.squares()[0][0][0])

class SudokuTest(unittest.TestCase):
    def setUp(self):
        self.puzzle = Sudoku()
        self.empty = Sudoku()
        for row in range(9):
            for col in range(9):
                self.puzzle[row][col] = 1 + (row + col) % 9
    def test_puzzle_initialized(self):
        self.assertEqual([1,2,3,4,5,6,7,8,9], self.puzzle[0])
        self.assertEqual([1,2,3,4,5,6,7,8,9], self.puzzle.col(0))
    def test_empty_initialized(self):
        self.assertEqual([0,0,0,0,0,0,0,0,0], self.empty[0])
        self.assertEqual([0,0,0,0,0,0,0,0,0], self.empty.col(0))
    def test_puzzle_rows_are_consistent(self):
        for row in range(9):
            self.assertTrue(self.puzzle.row_consistent(row))
    def test_puzzle_cols_are_consisten(self):
        for col in range(9):
            self.assertTrue(self.puzzle.col_consistent(col))
    def test_consistent_ignores_zero_entries(self):
        for index in range(9):
            self.assertTrue(self.empty.row_consistent(index))
            self.assertTrue(self.empty.col_consistent(index))
    def test_consistent_returns_false(self):
        self.puzzle[0][0] = 8
        self.assertFalse(self.puzzle.row_consistent(0))
        self.assertFalse(self.puzzle.col_consistent(0))
        self.puzzle[0][0] = 1
    def test_consistent_plays_nice_with_index(self):
        "this test doesn't check what it needs to"
        tmp = self.puzzle[8][8]
        self.puzzle[8][8] = 1
        self.assertFalse(self.puzzle.row_consistent(8))
        self.assertFalse(self.puzzle.col_consistent(8))
        self.puzzle[8][8] = tmp
    def test_squares_are_all_inconsistent(self):
        for i in range(9):
            self.assertFalse(self.puzzle.square_consistent(i))
    def test_squares_of_empty_are_consistent(self):
        for i in range(9):
            self.assertTrue(self.empty.square_consistent(i))
    def test_square_can_be_consistent(self):
        tmp = Sudoku()
        self.assertTrue(tmp.square_consistent(0))
        tmp[0][0] = 1
        tmp[0][1] = 2
        tmp[0][2] = 3
        self.assertTrue(tmp.square_consistent(0))
        tmp[1][0] = 4
        tmp[1][1] = 5
        tmp[1][2] = 3
        self.assertFalse(tmp.square_consistent(0))
        tmp[1][2] = 6
        self.assertTrue(tmp.square_consistent(0))
        tmp[2][0] = 7
        tmp[2][0] = 8
        self.assertTrue(tmp.square_consistent(0))
        tmp[2][2] = 5
        self.assertFalse(tmp.square_consistent(0))
    def test_puzzle_inconsistent(self):
        self.assertFalse(self.puzzle.consistent())
    def test_empty_consistent(self):
        self.assertTrue(self.empty.consistent())
    def test_puzzle_has_no_zero(self):
        self.assertFalse(self.puzzle.has_zero())
    def test_empty_has_zero(self):
        self.assertTrue(self.empty.has_zero())
    def test_puzzle_not_solved(self):
        self.assertFalse(self.puzzle.solved())
    def test_empty_not_solved(self):
        self.assertFalse(self.empty.solved())
    def test_solved_puzzle_is_solved(self):
        """example taken from http://www.sudokugame.com/rules.php"""
        tmp = Sudoku()
        tmp[0] = [2,4,8,3,9,5,7,1,6]
        tmp[1] = [5,7,1,6,2,8,3,4,9]
        tmp[2] = [9,3,6,7,4,1,5,8,2]
        tmp[3] = [6,8,2,5,3,9,1,7,4]
        tmp[4] = [3,5,9,1,7,4,6,2,8]
        tmp[5] = [7,1,4,8,6,2,9,5,3]
        tmp[6] = [8,6,3,4,1,7,2,9,5]
        tmp[7] = [1,9,5,2,8,6,4,3,7]
        tmp[8] = [4,2,7,9,5,3,8,6,1]
        self.assertTrue(tmp.solved())
        self.assertFalse(tmp.has_zero())
        self.assertTrue(tmp.consistent())


class SudokuSolverTests(unittest.TestCase):
    def setUp(self):
        pass
    def test_empty_puzzle_has_all_possible(self):
        tmp = Sudoku()
        solver = SudokuSolver()
        nine = [1,2,3,4,5,6,7,8,9]
        for row in range(9):
            for col in range(9):
                self.assertEqual(nine, solver.possible(tmp, row, col))
    


if __name__ == '__main__':
    unittest.main()
