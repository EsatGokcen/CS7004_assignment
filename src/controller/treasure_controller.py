from src.model.treasure_type import TreasureType
from src.model.treasure import Treasure
from src.model.eldoria_map import EldoriaMap
from src.model.cell import Cell
from random import randint, choice

def find_cell_for_treasure(map_obj: EldoriaMap, treasure: Treasure) -> Cell | None:
    for x in range(map_obj.get_width()):
        for y in range(map_obj.get_height()):
            cell = map_obj.get_cell(x, y)
            if treasure in cell.get_contents():
                return cell
    return None

def scatter_treasures(num_treasures: int, map_obj: EldoriaMap) -> None:
    for _ in range(num_treasures):
        x = randint(0, map_obj.get_width() - 1)
        y = randint(0, map_obj.get_height() - 1)
        t_type = choice(list(TreasureType))
        treasure = Treasure(t_type)
        map_obj.get_cell(x, y).add_object(treasure)


def decay_all_treasures(map_obj: EldoriaMap) -> None:
    for x in range(map_obj.get_width()):
        for y in range(map_obj.get_height()):
            cell = map_obj.get_cell(x, y)
            for obj in cell.get_contents()[:]:
                if isinstance(obj, Treasure):
                    obj.lose_value()
                    if obj.is_depleted():
                        cell.remove_object(obj)