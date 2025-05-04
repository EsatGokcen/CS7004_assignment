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
    blocked_positions = set()

    # Collect all blocked positions (radius 3 around hideouts)
    for x in range(map_obj.get_width()):
        for y in range(map_obj.get_height()):
            cell = map_obj.get_cell(x, y)
            if any(obj.__class__.__name__ == "Hideout" for obj in cell.get_contents()):
                for dx in range(-3, 4):
                    for dy in range(-3, 4):
                        if abs(dx) + abs(dy) <= 3:
                            bx = (x + dx) % map_obj.get_width()
                            by = (y + dy) % map_obj.get_height()
                            blocked_positions.add((bx, by))

    # Drop treasures only in allowed cells
    width = map_obj.get_width()
    height = map_obj.get_height()

    attempts = 0
    placed = 0
    while placed < num_treasures and attempts < num_treasures * 10:
        x = randint(0, width - 1)
        y = randint(0, height - 1)
        if (x, y) in blocked_positions:
            attempts += 1
            continue
        t_type = choice(list(TreasureType))
        treasure = Treasure(t_type)
        map_obj.get_cell(x, y).add_object(treasure)
        placed += 1

def decay_all_treasures(map_obj: EldoriaMap) -> None:
    for x in range(map_obj.get_width()):
        for y in range(map_obj.get_height()):
            cell = map_obj.get_cell(x, y)
            for obj in cell.get_contents()[:]:
                if isinstance(obj, Treasure):
                    obj.lose_value()
                    if obj.is_depleted():
                        cell.remove_object(obj)