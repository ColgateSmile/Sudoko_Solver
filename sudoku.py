import numpy as np


class Sudoku:

    def __init__(self, board: np.array) -> object:
        self._board = board

    def __len__(self):
        return len(self._board)

    def set_value(self, pos: tuple, value: int) -> bool:
        if not self.is_valid(pos=pos, value=value):
            return False
        self._board[pos] = value
        return True

    def get_value(self, pos: tuple) -> int:
        return self._board[pos]

    def is_valid(self, pos: tuple, value: int) -> bool:
        """
        this function checks the Constrains on every number that we try in the way to the solution
        :param pos:
        :param value:
        :return:
        //check if one of the values is 1-9//
        """
        if value == 0:
            return True

        for i in range(len(self._board[0])):
            if self._board[pos[0]][i] == value and pos[1] != i:
                return False

        # check COL
        for i in range(len(self._board)):
            if self._board[i][pos[1]] == value and pos[0] != i:
                return False

        # check BOX (the 3*3 must contain all integer's from 1-9 no duplicates)
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self._board[i][j] == value and (i, j) != pos:
                    return False

        return True

    def print_board(self):
        for i in range(len(self._board)):

            # after every 3 rows it will draw horizontal line
            if i % 3 == 0:
                print("="*25)

            for j in range(len(self._board[0])):

                # after every 3 Columns it will draw a diagonal line
                if j % 3 == 0 and j != 0:
                    print(" || ", end="")

                if j == 8:
                    print(self._board[i][j])
                else:
                    print(str(self._board[i][j]) + " ", end="")

        print("="*25)


    def get_board(self)-> object:
        return self._board