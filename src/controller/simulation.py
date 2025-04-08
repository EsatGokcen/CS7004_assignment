from src.model.eldoria_map import EldoriaMap
from src.model.treasure_type import TreasureType
from src.model.treasure import Treasure
from random import randint, choice

class Simulation:

    def __init__(self, map_obj: EldoriaMap):
        self.map = map_obj

    def scatter_treasures(self, num_treasures: int) -> None:
        for _ in range(num_treasures):
            x = randint(0, self.map.get_width() - 1)
            y = randint(0, self.map.get_height() - 1)
            t_type = choice(list(TreasureType))
            treasure = Treasure(t_type)
            self.map.get_cell(x, y).add_object(treasure)

    def decay_all_treasures(self) -> None:
        for x in range(self.map.get_width()):
            for y in range(self.map.get_height()):
                cell = self.map.get_cell(x, y)
                for obj in cell.contents[:]:
                    if isinstance(obj, Treasure):
                        obj.lose_value()
                        if obj.is_depleted():
                            cell.remove_object(obj)