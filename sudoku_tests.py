import unittest
from sudoku import *

class SudokuTests(unittest.TestCase):
    def test_class_exists(self):
        "this test verifies a class Sudoku exists"
        self.puzzle = Sudoku()
        self.assertTrue(self.puzzle)
    


if __name__ == '__main__':
    unittest.main()