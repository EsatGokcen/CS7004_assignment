from src.model.knight import Knight
from src.model.garrison import Garrison
from src.model.eldoria_map import EldoriaMap
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
            if not knight.get_resting() and knight.get_cell() == knight.get_garrison_origin():
                knight.patrol(map_obj)
            continue

        knight.scan(map_obj)
        target = knight.get_target()

        if target:
            # Ensure target is still valid
            if target not in target.get_cell().get_contents():
                knight._target = None
                knight.patrol(map_obj)
                continue

            stamina = knight.get_stamina()
            dist_to_hunter = map_obj.get_distance(knight.get_cell(), target.get_cell())
            hunter_wealth = target.get_wealth()

            action = decide_knight_action(stamina, dist_to_hunter, hunter_wealth)

            if action == 0:
                knight.retreat(map_obj)
            elif action == 1:
                knight.patrol(map_obj)
            elif action == 2:
                knight._target = target
                knight.chase(map_obj)

                # Refresh scan if target lost after chase
                if knight.get_target() is None:
                    knight.scan(map_obj)
            else:
                knight.patrol(map_obj)

        else:
            knight.patrol(map_obj)