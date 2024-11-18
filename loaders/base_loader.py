from sudoku import Sudoku
from typing import Tuple


class BaseLoader:
    def load(self) -> Tuple[Sudoku, Sudoku]:
        raise NotImplementedError('load not implemented')
