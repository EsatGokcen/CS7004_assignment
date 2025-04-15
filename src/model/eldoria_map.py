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

    def get_adjacent_cells(self, cell: Cell) -> list:
        x, y = cell.get_x(), cell.get_y()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
        neighbours = []
        for dx, dy in directions:
            nx, ny = (x + dx) % self.get_width(), (y + dy) % self.get_height()
            neighbours.append(self.get_cell(nx, ny))
        return neighbours
