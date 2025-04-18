from src.controller.treasure_controller import find_cell_for_treasure
from src.model.hideout import Hideout
from src.model.treasure_hunter import TreasureHunter
from src.model.hunter_skills import Skill
from src.model.treasure import Treasure
from src.model.eldoria_map import EldoriaMap
from random import randint, choice
from typing import List

def place_hideouts_and_hunters(hideouts: List[Hideout], map_obj: EldoriaMap, num_hideouts: int, hunters_per_hideout_range: tuple) -> None:
    for _ in range(num_hideouts):
        x = randint(0, map_obj.get_width() - 1)
        y = randint(0, map_obj.get_height() - 1)
        cell = map_obj.get_cell(x, y)
        hideout = Hideout(cell)
        hideouts.append(hideout)

        num_hunters = randint(*hunters_per_hideout_range)
        for _ in range(num_hunters):
            skill = choice(list(Skill))
            hunter = TreasureHunter(cell, skill)
            hideout.add_hunter(hunter)


def step_hunters(hideouts: List[Hideout], map_obj: EldoriaMap) -> None:
    for hideout in hideouts:
        for hunter in hideout.get_hunters():
            if hunter.is_collapsed():
                hunter.tick_survival()
                if hunter.get_survival_steps_remaining() <= 0:
                    hideout.remove_hunter(hunter)
                    hunter.get_cell().remove_object(hunter)
                    continue

            if not hunter.can_act():
                continue

            if hunter.is_critical():
                known_hideouts = hunter.get_memory()["hideouts"]
                if known_hideouts:
                    closest = min(known_hideouts, key=lambda h: map_obj.get_distance(hunter.get_cell(), h))
                    neighbors = map_obj.get_adjacent_cells(hunter.get_cell())
                    next_step = min(neighbors, key=lambda c: map_obj.get_distance(c, closest))
                    hunter.move_to(next_step)
                else:
                    hunter.rest()
                continue

            cell = hunter.get_cell()
            neighbors = map_obj.get_adjacent_cells(cell)
            visible_objects = [obj for neighbor in neighbors for obj in neighbor.get_contents()]

            treasures = [obj for obj in visible_objects if isinstance(obj, Treasure)]
            unused_hideouts = [obj for obj in visible_objects if isinstance(obj, Hideout)]

            hunter.remember(treasures, [h.get_cell() for h in hideouts])

            if hunter.is_carrying_treasure():
                for neighbor in neighbors:
                    if any(isinstance(obj, Hideout) for obj in neighbor.get_contents()):
                        hunter.move_to(neighbor)
                        for obj in neighbor.get_contents():
                            if isinstance(obj, Hideout):
                                obj.store_treasure(hunter)
                        break
                else:
                    hunter.move_to(choice(neighbors))
            else:
                if treasures:
                    best = max(treasures, key=lambda t: t.get_value())
                    for neighbor in neighbors:
                        if best in neighbor.get_contents():
                            hunter.move_to(neighbor)
                            hunter._carried_treasure = best
                            best.mark_collected()
                            break
                else:
                    remembered = hunter.get_memory()["treasures"]
                    if remembered:
                        closest = min(
                            remembered,
                            key=lambda t: map_obj.get_distance(
                                hunter.get_cell(),
                                find_cell_for_treasure(map_obj, t) or hunter.get_cell()
                            )
                        )
                        closest_cell = find_cell_for_treasure(map_obj, closest)
                        if closest_cell:
                            next_step = min(
                                neighbors,
                                key=lambda c: map_obj.get_distance(c, closest_cell)
                            )
                            hunter.move_to(next_step)
                        else:
                            hunter.move_to(choice(neighbors))
                    else:
                        hunter.move_to(choice(neighbors))

        hideout.share_knowledge()
        hideout.recruit_new_hunter()