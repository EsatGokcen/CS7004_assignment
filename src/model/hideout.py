from src.model.cell import Cell
from src.model.treasure_hunter import TreasureHunter
from typing import List


class Hideout:
    def __init__(self, cell: Cell):
        self._cell = cell
        self._hunters: List[TreasureHunter] = []
        cell.add_object(self)

    def get_cell(self) -> Cell:
        return self._cell

    def get_hunters(self) -> List[TreasureHunter]:
        return self._hunters.copy()

    def has_space(self) -> bool:
        return len(self._hunters) < 5

    def add_hunter(self, hunter: TreasureHunter) -> None:
        if self.has_space():
            self._hunters.append(hunter)
            if hunter not in self._cell.contents:
                self._cell.add_object(hunter)