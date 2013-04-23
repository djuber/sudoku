import unittest
from sudoku import *

class SudokuTests(unittest.TestCase):
    def setUp(self):
        self.puzzle = Sudoku()
    def test_class_exists(self):
        "this test verifies a class Sudoku exists"
        self.assertTrue(self.puzzle)
    def test_initialized_to_zero(self):
        self.assertEqual(0, self.puzzle.row(0)[0])
        self.assertEqual(0, self.puzzle.row(8)[8])
    def test_cols_gives_an_answer(self):
        self.assertEqual(9, len(self.puzzle.cols()))
    def test_col(self):
        self.assertEqual(0, self.puzzle.col(4)[0])

if __name__ == '__main__':
    unittest.main()