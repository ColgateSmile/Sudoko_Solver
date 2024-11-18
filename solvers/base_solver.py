from sudoku import Sudoku
import time


class BaseSolver:
    def __init__(self, sudoku: Sudoku):
        self._sudoku = sudoku

    def run(self):
        raise NotImplementedError('run not implemented')

    def run_with_time_analysis(self):
        start_time = time.time()
        self.run()
        return time.time() - start_time
