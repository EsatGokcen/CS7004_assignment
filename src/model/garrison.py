from src.model.cell import Cell
from src.model.knight import Knight

class Garrison:

    def __init__(self, cell: Cell):
        self.__cell = cell
        self.__knights: list[Knight] = []
        self.__cell.add_object(self)

    def get_cell(self) -> Cell:
        return self.__cell

    def get_knights(self) -> list[Knight]:
        return self.__knights

    def has_space(self) -> bool:
        return len(self.__knights) < 5

    def add_knight(self, knight: Knight) -> None:
        if self.has_space():
            self.__knights.append(knight)
            if knight not in self.__cell.get_contents():
                self.__cell.add_object(knight)

    def remove_knight(self, knight: Knight) -> None:
        if knight in self.__knights:
            self.__knights.remove(knight)
            self.__cell.remove_object(knight)