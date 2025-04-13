from src.model.cell import Cell
from src.model.hunter_skills import Skill
from src.model.treasure import Treasure
from typing import List


class TreasureHunter:

    def __init__(self, cell: Cell, skill: Skill):
        self._cell = cell
        self._stamina: float = 100.0
        self._carried_treasure: List[Treasure] = []
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

    def get_carried_treasure(self) -> List[Treasure]:
        return self._carried_treasure

    def is_carrying_treasure(self) -> bool:
        return self._carried_treasure is not None

    def deposit_treasure(self) -> None:
        self._carried_treasure = [] # deposit logic happens in hideout class store_treasure() method

    def move_to(self, new_cell: Cell) -> None:
        self._cell.remove_object(self)
        new_cell.add_object(self)
        self._cell = new_cell
        self._stamina -= 2.0
        if self._stamina < 0:
            self._stamina = 0

    def rest(self) -> None:
        if self._stamina < 100.0:
            self._stamina += 1.0
            if self._stamina > 100.0:
                self._stamina = 100.0

    def is_critical(self) -> bool:
        return self._stamina <= 6.0

    def is_collapsed(self) -> bool:
        return self._stamina <= 0.0

    def tick_survival(self) -> None:
        if self.is_collapsed():
            self._survival_steps_remaining -= 1

    def can_act(self) -> bool:
        return not self.is_collapsed() or self._survival_steps_remaining > 0

    def share_memory(self, other: 'TreasureHunter') -> None:
        self._memory["treasures"].extend(t for t in other._memory["treasures"] if t not in self._memory["treasures"])
        self._memory["hideouts"].extend(h for h in other._memory["hideouts"] if h not in self._memory["hideouts"])