from .base_solver import BaseSolver
from sudoku import Sudoku
from typing import Generator, Tuple, Optional


class NaiveSolver(BaseSolver):
    def __init__(self, sudoku: Sudoku):
        super().__init__(sudoku=sudoku)

    def run(self) -> bool:
        """Solves the Sudoku board using backtracking."""
        empty_pos = self._find_next_empty_pos()
        if not empty_pos:
            return True  # Solved

        row, col = empty_pos
        for value in range(1, 10):  # Try all values from 1 to 9
            if self._sudoku.set_value((row, col), value):
                if self.run():
                    return True  # Solved

        self._sudoku.set_value((row, col), 0)  # Backtrack
        return False

    def solve_with_steps(self) -> Generator[Tuple[Sudoku, Optional[Tuple[int, int]]], None, None]:
        """
        Solves the Sudoku board step-by-step for visualization.
        Yields the current board state and the cell being solved.
        """
        empty_pos = self._find_next_empty_pos()
        if not empty_pos:
            yield self._sudoku, None  # Board solved
            return

        row, col = empty_pos
        for value in range(1, 10):  # Try all values from 1 to 9
            if self._sudoku.set_value((row, col), value):
                yield self._sudoku, (col, row)  # Yield intermediate step

                # Recursive call with propagated results
                for result in self.solve_with_steps():
                    yield result  # Continue solving

        self._sudoku.set_value((row, col), 0)  # Backtrack
        yield self._sudoku, (col, row)  # Yield backtracking step

    def _find_next_empty_pos(self) -> Optional[Tuple[int, int]]:
        """Finds the next empty position on the board."""
        for row in range(len(self._sudoku)):
            for col in range(len(self._sudoku)):
                if self._sudoku.get_value((row, col)) == 0:
                    return row, col
        return None
