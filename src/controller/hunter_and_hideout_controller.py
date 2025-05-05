from src.model.knight import Knight
from src.model.garrison import Garrison
from src.model.eldoria_map import EldoriaMap
from src.model.treasure_hunter import TreasureHunter
from src.model.hunter_skills import HunterSkill
from src.controller.knight_ai import decide_knight_action

def place_garrison_with_knights(map_obj: EldoriaMap, num_knights: int) -> tuple[Garrison, list[Knight]]:
    center_cell = map_obj.get_cell(map_obj.get_width() // 2, map_obj.get_height() // 2)
    garrison = Garrison(center_cell)
    knights = []
    for _ in range(num_knights):
        knight = Knight(center_cell)
        knights.append(knight)
        garrison.add_knight(knight)
    return garrison, knights

def step_knights(knights: list[Knight], map_obj: EldoriaMap) -> None:
    for knight in knights:
        if knight.get_resting():
            knight.rest()
            continue

        # Find closest hunter info
        closest_hunter = None
        min_dist = 999
        for x in range(map_obj.get_width()):
            for y in range(map_obj.get_height()):
                cell = map_obj.get_cell(x, y)
                for obj in cell.get_contents():
                    if isinstance(obj, TreasureHunter):
                        dist = map_obj.get_distance(knight.get_cell(), cell)
                        if dist < min_dist:
                            closest_hunter = obj
                            min_dist = dist

        if closest_hunter:
            stamina = knight.get_stamina()
            dist_to_hunter = min_dist
            hunter_stealth = 1 if closest_hunter.get_skill() == HunterSkill.STEALTH else 0
            hunter_wealth = closest_hunter.get_wealth()
            is_adjacent = 1 if dist_to_hunter == 1 else 0

            action = decide_knight_action(stamina, dist_to_hunter, hunter_stealth, hunter_wealth, is_adjacent)

            if action == 0:
                knight.retreat(map_obj)

            elif action == 1:
                knight.patrol(map_obj)

            elif action == 2:
                knight._target = closest_hunter
                knight.chase(map_obj)

            elif action == 3 and is_adjacent:
                knight._target = closest_hunter
                knight.challenge() if random.random() < 0.5 else knight.detain()
                knight._target = None

            else:
                knight.patrol(map_obj)

        else:
            knight.patrol(map_obj)