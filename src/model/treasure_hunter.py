from src.model.cell import Cell
from src.model.hunter_skills import Skill


class TreasureHunter:

    def __init__(self, cell: Cell, skill: Skill):
        self._cell = cell
        self._stamina: float = 100.0
        self._carried_treasure = None
        self._skill = skill
        self._memory = {"treasures": [], "hideouts": []}
        self._survival_steps_remaining = 3
        cell.add_object(self)

    def get_cell(self) -> Cell:
        return self._cell

    def get_stamina(self) -> float:
        return self._stamina

    def get_skill(self) -> Skill:
        return self._skill

    def get_memory(self) -> dict:
        return self._memory