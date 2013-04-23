import unittest
from sudoku import *

class SudokuTests(unittest.TestCase):
    def setUp(self):
        self.puzzle = Sudoku()
    def test_class_exists(self):
        "verifies a class Sudoku exists"
        self.assertTrue(self.puzzle)
    def test_rows_gives_an_answer(self):
        self.assertEqual(9, len(self.puzzle.rows()))
    def test_initialized_to_zero(self):
        "verifies initially zeroed board"
        self.assertEqual(0, self.puzzle.row(0)[0])
        self.assertEqual(0, self.puzzle.row(8)[8])
    def test_cols_gives_an_answer(self):
        self.assertEqual(9, len(self.puzzle.cols()))
    def test_col(self):
        self.assertEqual(0, self.puzzle.col(4)[0])
    def test_getitem_returns_row(self):
        self.assertEqual(self.puzzle.row(0), self.puzzle[0])
    def test_getitem_sufficient_for_setitem(self):
        """
        since getitem returns row as a list, setitem on the list should
        be transparent
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


if __name__ == '__main__':
    unittest.main()