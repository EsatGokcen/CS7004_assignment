from src.model.cell import Cell
from src.model.treasure_hunter import TreasureHunter
from src.model.eldoria_map import EldoriaMap
from typing import Optional
import math

class Knight:

    def __init__(self, cell: Cell):
        self.__cell = cell
        self.__stamina: float = 100.0
        self.__target: Optional[TreasureHunter] = None
        self.__resting: bool = False
        self.__angle: float = 0.0
        self.__orbit_radius: int = 1
        self.__garrison_origin: Cell = cell

    def get_cell(self) -> Cell:
        return self.__cell

    def get_stamina(self) -> float:
        return self.__stamina

    def patrol(self, map_obj: EldoriaMap) -> None:
        if self.__resting or self.__target:
            return

        # Spiral motion outward from garrison origin
        self.__angle += math.pi / 6  # increment angle
        self.__orbit_radius += 0.05  # slowly increase radius

        x0, y0 = self.__garrison_origin.get_x(), self.__garrison_origin.get_y()
        dx = int(round(self.__orbit_radius * math.cos(self.__angle)))
        dy = int(round(self.__orbit_radius * math.sin(self.__angle)))
        new_x = (x0 + dx) % map_obj.get_width()
        new_y = (y0 + dy) % map_obj.get_height()
        self.__cell = map_obj.get_cell(new_x, new_y)

    def scan(self, map_obj: EldoriaMap) -> None:
        # Detects and chooses the wealthiest hunter within 3 cells
        if self.__resting:
            return

        x0, y0 = self.__cell.get_x(), self.__cell.get_y()
        nearby_hunters = []

        for dx in range(-3, 4):
            for dy in range(-3, 4):
                if abs(dx) + abs(dy) <= 3:
                    x, y = (x0 + dx) % map_obj.get_width(), (y0 + dy) % map_obj.get_height()
                    cell = map_obj.get_cell(x, y)
                    for obj in cell.get_contents():
                        if isinstance(obj, TreasureHunter):
                            nearby_hunters.append(obj)

        if nearby_hunters:
            self.__target = max(nearby_hunters, key=lambda h: h.get_wealth(), default=None)

    def chase(self):
        # focus on a single hunter after patrol
        # limited range pn chase
        # lose 20% of energy after each chase
        pass

    def detain(self):
        # drains 5% of hunter stamina
        # forces hunter to drop any treasure they are carrying
        pass

    def challenge(self):
        # reduces 20% of hunter stamina
        # forces hunter to drop treasure
        pass

    def retreat(self):
        # if stamina is 20% or below retreat to garrison
        pass

    def rest(self):
        # rest until stamina fully restored
        # start patrolling again once stamina fully restored
        pass