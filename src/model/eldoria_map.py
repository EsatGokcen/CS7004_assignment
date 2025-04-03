from src.model.cell import Cell

class EldoriaMap:

    def __init__(self, width: int = 30, height: int = 30):
        self.__width = width
        self.__height = height
        self.grid = [[Cell(x, y) for y in range(height)] for x in range(width)]

    def get_cell(self, x: int, y: int) -> Cell:
        # Wrap-around behavior
        x %= self.__width
        y %= self.__height
        return self.grid[x][y]

    def get_width(self) -> int:
        return self.__width

    def get_height(self) -> int:
        return self.__height
