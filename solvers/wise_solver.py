from .base_solver import BaseSolver
from sudoku import Sudoku
from collections import defaultdict


class WiseSolver(BaseSolver):
    def __init__(self, sudoku: Sudoku):
        super().__init__(sudoku=sudoku)
        self._possible_values = defaultdict(lambda: [i + 1 for i in range(len(self._sudoku))])

    def run(self) -> bool:
        """Solves the Sudoku board using constraint propagation and backtracking."""
        empty_pos = self._find_next_empty_pos()
        if not empty_pos:
            return True  # Solved

        # Get possible values for the current cell
        row, col = empty_pos
        self._update_possible_values()  # Update domains for all cells
        candidates = self._possible_values[(row, col)]

        for value in candidates:
            if not self._sudoku.set_value((row, col), value):
                continue  # Skip invalid values

            if self.run():
                return True  # Solved

        self._sudoku.set_value((row, col), 0)  # Backtrack
        return False

    def solve_with_steps(self):
        """Solves the Sudoku board step-by-step for visualization."""
        empty_pos = self._find_next_empty_pos()
        if not empty_pos:
            yield self._sudoku, None
            return

        row, col = empty_pos
        self._update_possible_values()  # Update domains for all cells
        candidates = self._possible_values[(row, col)]

        for value in candidates:
            if not self._sudoku.set_value((row, col), value):
                continue  # Skip invalid values

            yield self._sudoku, (col, row)  # Yield intermediate step
            for result in self.solve_with_steps():
                yield result  # Continue solving with steps

        self._sudoku.set_value((row, col), 0)
        yield self._sudoku, None  # Yield backtrack step

    def _update_possible_values(self):
        """Updates possible values for each cell based on current board state."""
        for row in range(len(self._sudoku)):
            for col in range(len(self._sudoku)):
                if self._sudoku.get_value((row, col)) == 0:  # Empty cell
                    self._possible_values[(row, col)] = [
                        value for value in range(1, 10) if self._sudoku.is_valid((row, col), value)
                    ]

    def _find_next_empty_pos(self):
        """Finds the next empty position using Minimum Remaining Values (MRV)."""
        empty_cells = [(row, col) for row in range(len(self._sudoku)) for col in range(len(self._sudoku))
                       if self._sudoku.get_value((row, col)) == 0]
        if not empty_cells:
            return None

        # Prioritize cells with the fewest possible values (MRV heuristic)
        return min(empty_cells, key=lambda pos: len(self._possible_values[pos]))
