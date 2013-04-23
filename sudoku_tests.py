import unittest
from sudoku import *

class GridTests(unittest.TestCase):
    def setUp(self):
        "wherein we create a board with numbers in it"
        self.puzzle = Grid()
        self.empty = Grid()
        for row in range(9):
            for col in range(9):
                self.puzzle[row][col] = (1 + (row + col) % 9)
                print(str(1 + (row + col) % 9) + " at " + str(row) +", "+str(col))
        print(str(self.puzzle))
        print(str(self.puzzle.rows()))
        print(str(self.puzzle.cols()))
        print(str(self.puzzle.squares()))


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
    def test_squares_access(self):
        self.assertEqual(1, self.puzzle.squares()[0][0][0])
    def test_print_data(self):
        print(str(self.puzzle))
        print(str(self.puzzle.rows()))
        print(str(self.puzzle.cols()))
        print(str(self.puzzle.squares()))
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
