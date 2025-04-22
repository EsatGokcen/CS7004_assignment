from src.model.knight import Knight
from src.model.garrison import Garrison
from src.model.eldoria_map import EldoriaMap

def place_garrison_with_knights(map_obj: EldoriaMap, num_knights: int) -> tuple[Garrison, list[Knight]]:
    center_cell = map_obj.get_cell(map_obj.get_width() // 2, map_obj.get_height() // 2)
    garrison = Garrison(center_cell)
    knights = []
    for _ in range(num_knights):
        knight = Knight(center_cell)
        knights.append(knight)
        garrison.add_knight(knight)
    return garrison, knights