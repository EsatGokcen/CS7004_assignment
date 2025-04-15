from src.model.treasure_hunter import TreasureHunter
from src.model.treasure import Treasure
from src.model.hideout import Hideout

# Mock Knight class for now
class Knight: pass

class Cell:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
        self.contents = []  # Can hold treasure, hunter, knight, etc.

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    def add_object(self, obj) -> None:
        self.contents.append(obj)

    def remove_object(self, obj) -> None:
        if obj in self.contents:
            self.contents.remove(obj)

    def is_empty(self) -> bool:
        return len(self.contents) == 0

    def contains_hunter(self) -> bool:
        return any(isinstance(obj, TreasureHunter) for obj in self.contents)

    def contains_knight(self) -> bool:
        return any(isinstance(obj, Knight) for obj in self.contents)

    def contains_treasure(self) -> bool:
        return any(isinstance(obj, Treasure) for obj in self.contents)

    def is_hideout(self) -> bool:
        return any(isinstance(obj, Hideout) for obj in self.contents)

    def __repr__(self) -> str:
        return f"Cell({self.__x},{self.__y}): {self.contents}"