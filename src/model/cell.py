from src.model.treasure import Treasure

class Cell:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
        self.__contents = []  # Can hold treasure, hunter, knight, etc.

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    def get_contents(self) -> list:
        return self.__contents

    def add_object(self, obj) -> None:
        self.__contents.append(obj)

    def remove_object(self, obj) -> None:
        if obj in self.__contents:
            self.__contents.remove(obj)

    def is_empty(self) -> bool:
        return len(self.__contents) == 0

    def contains_hunter(self) -> bool:
        from src.model.treasure_hunter import TreasureHunter
        return any(isinstance(obj, TreasureHunter) for obj in self.__contents)

    def contains_knight(self) -> bool:
        from src.model.knight import Knight
        return any(isinstance(obj, Knight) for obj in self.__contents)

    def contains_treasure(self) -> bool:
        return any(isinstance(obj, Treasure) for obj in self.__contents)

    def is_hideout(self) -> bool:
        from src.model.hideout import Hideout
        return any(isinstance(obj, Hideout) for obj in self.__contents)

    def is_garrison(self) -> bool:
        from src.model.garrison import Garrison
        return any(isinstance(obj, Garrison) for obj in self.__contents)

    def __repr__(self) -> str:
        return f"Cell({self.__x},{self.__y}): {self.__contents}"