from src.controller.treasure_controller import find_cell_for_treasure
from src.model.hideout import Hideout
from src.model.treasure_hunter import TreasureHunter
from src.model.hunter_skills import Skill
from src.model.treasure import Treasure
from src.model.eldoria_map import EldoriaMap
from src.model.hunter_ai import decide_action
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

            found_positions = hunter.scan_for_treasure(map_obj)
            found_treasures = []
            for pos in found_positions:
                cell = map_obj.get_cell(pos[0], pos[1])
                for obj in cell.get_contents():
                    if isinstance(obj, Treasure):
                        found_treasures.append(obj)

            hunter.remember(found_treasures, [h.get_cell() for h in hideouts])

            stamina = hunter.get_stamina()
            known_hideouts = hunter.get_memory()["hideouts"]
            known_treasures = hunter.get_memory()["treasures"]
            dist_to_hideout = (
                min(map_obj.get_distance(hunter.get_cell(), h) for h in known_hideouts)
                if known_hideouts else 10
            )
            dist_to_treasure = (
                min(map_obj.get_distance(hunter.get_cell(), find_cell_for_treasure(map_obj, t) or hunter.get_cell())
                    for t in known_treasures)
                if known_treasures else 10
            )

            knight_nearby = 0
            for neighbor in map_obj.get_adjacent_cells(hunter.get_cell()):
                if any(obj.__class__.__name__ == "Knight" for obj in neighbor.get_contents()):
                    knight_nearby = 1
                    break

            action = decide_action(stamina, dist_to_treasure, dist_to_hideout, knight_nearby)
            cell = hunter.get_cell()
            neighbors = map_obj.get_adjacent_cells(cell)
            visible_objects = [obj for neighbor in neighbors for obj in neighbor.get_contents()]

            treasures = [obj for obj in visible_objects if isinstance(obj, Treasure)]

            if action == 0:
                hunter.rest()

            elif action == 1 and not hunter.is_carrying_treasure():
                if treasures:
                    best = max(treasures, key=lambda t: t.get_value())
                    for neighbor in neighbors:
                        if best in neighbor.get_contents():
                            hunter.move_to(neighbor)
                            hunter._carried_treasure = best
                            best.mark_collected()
                            break
                elif known_treasures:
                    closest = min(
                        known_treasures,
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

            elif action == 2 and hunter.is_carrying_treasure():
                for neighbor in neighbors:
                    if any(obj.__class__.__name__ == "Hideout" for obj in neighbor.get_contents()):
                        hunter.move_to(neighbor)
                        for obj in neighbor.get_contents():
                            if isinstance(obj, Hideout):
                                obj.store_treasure(hunter)
                        break
                else:
                    hunter.move_to(choice(neighbors))

            elif action == 3:
                knight_cells = [
                    neighbor for neighbor in neighbors
                    if any(obj.__class__.__name__ == "Knight" for obj in neighbor.get_contents())
                ]
                safe_cells = [n for n in neighbors if n not in knight_cells]
                if safe_cells:
                    hunter.move_to(choice(safe_cells))
                else:
                    hunter.move_to(choice(neighbors))

            else:
                hunter.move_to(choice(neighbors))

        hideout.share_knowledge()
        hideout.recruit_new_hunter()