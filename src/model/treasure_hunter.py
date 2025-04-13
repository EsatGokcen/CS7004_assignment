from src.model.cell import Cell


class TreasureHunter:

    def __init__(self, cell: Cell, skill):
        self._cell = cell
        self._stamina: float = 100.0
        self._carried_treasure = None
        self._skill = skill
        self._memory = {"treasures": [], "hideouts": []}
        self._survival_steps_remaining = 3
        cell.add_object(self)