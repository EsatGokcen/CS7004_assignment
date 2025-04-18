import tkinter as tk
from src.controller.config import *
from src.model.eldoria_map import EldoriaMap
from src.model.cell import Cell
from src.model.treasure import Treasure
from src.model.treasure_type import TreasureType



class GridView:
    def __init__(self, master: tk.Tk, map_obj: EldoriaMap):
        self.map = map_obj
        self.frame = tk.Frame(master)

        canvas_width = self.map.get_width() * CELL_SIZE
        canvas_height = self.map.get_height() * CELL_SIZE

        self.canvas = tk.Canvas(self.frame, width=canvas_width, height=canvas_height, bg="white")
        self.canvas.pack()

        self.draw_grid()

    def draw_grid(self) -> None:
        for y in range(self.map.get_height()):
            for x in range(self.map.get_width()):
                x1 = x * CELL_SIZE
                y1 = y * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                cell = self.map.get_cell(x, y)
                fill_color = self.get_color(cell)

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="gray")

    def get_color(self, cell: Cell) -> str:
        if cell.is_hideout():
            return "#228B22"  # forest green
        elif cell.contains_hunter():
            return "#1E90FF"  # dodger blue
        elif cell.contains_knight():
            return "#8B0000"  # dark red
        elif cell.contains_treasure():
            for obj in cell.get_contents():
                if isinstance(obj, Treasure):
                    t_type = obj.get_type()
                    if t_type == TreasureType.GOLD:
                        return "#FFD700"  # gold
                    elif t_type == TreasureType.SILVER:
                        return "#C0C0C0"  # silver
                    elif t_type == TreasureType.BRONZE:
                        return "#CD7F32"  # bronze
        return "#F5F5F5"  # off-white

