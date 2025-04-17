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

    def get_distance(self, cell1: Cell, cell2: Cell) -> int:
        x1, y1 = cell1.get_x(), cell1.get_y()
        x2, y2 = cell2.get_x(), cell2.get_y()

        dx = min(abs(x1 - x2), self.__width - abs(x1 - x2))
        dy = min(abs(y1 - y2), self.__height - abs(y1 - y2))
        return dx + dy

    def clear(self):
        for x in range(self.__width):
            for y in range(self.__height):
                self.grid[x][y].contents.clear()

