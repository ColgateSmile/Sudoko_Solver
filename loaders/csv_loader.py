from .base_loader import BaseLoader
import os
from sudoku import Sudoku
import random
from typing import Tuple
import numpy as np


class CsvLoader(BaseLoader):
    def __init__(self):
        self._file = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'input', 'sudoku.csv')
        self._length = 10000
        self._sudoku_size = 9

    def load(self) -> Tuple[Sudoku, Sudoku]:
        """
        takes a random row from, the csv file and return it as 2 numpy 9*9 matrix
        :return: Unsolved Sudoku, solved Sudoku
        """
        with open(self._file, 'r') as file:
            chosen_line = file.readlines()[random.randint(0, 10000)]
        unsolved_line, solved_line = tuple(chosen_line.split(','))
        total_board_size = self._sudoku_size * self._sudoku_size
        one_dim_unsolved_array = np.fromstring(string=' '.join(unsolved_line), dtype=int, count=total_board_size,
                                               sep=' ')
        one_dim_solved_array = np.fromstring(string=' '.join(solved_line), dtype=int, count=total_board_size, sep=' ')
        return Sudoku(
            board=one_dim_unsolved_array.reshape((self._sudoku_size, self._sudoku_size))), Sudoku(
            board=one_dim_solved_array.reshape((self._sudoku_size, self._sudoku_size)))
