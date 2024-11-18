import unittest
import numpy as np
from sudoku import Sudoku

test_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


class Sudoku_test(unittest.TestCase):
    def test_sudoku(self):
        sudoku = Sudoku(np.array(test_board))
        sudoku.print_board()
        value = sudoku.get_value(pos=(3, 2))
        expected_value = test_board[3][2]
        self.assertEqual(first=value, second=expected_value)
        self.assertTrue(expr=sudoku.set_value(pos=(0, 2), value=5))
        self.assertFalse(expr=sudoku.set_value(pos=(0, 4), value=7))
        self.assertFalse(expr=sudoku.is_valid(pos=(0, 4), value=7))
