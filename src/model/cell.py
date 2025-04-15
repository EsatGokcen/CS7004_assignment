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

    def __repr__(self) -> str:
        return f"Cell({self.__x},{self.__y}): {self.contents}"