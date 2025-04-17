from src.model.cell import Cell
from src.model.hunter_skills import Skill
from src.model.hideout import Hideout
from src.model.treasure import Treasure
from src.model.treasure_type import TreasureType
from typing import List


class TreasureHunter:

    def __init__(self, cell: Cell, skill: Skill):
        self._cell = cell
        self._stamina: float = 100.0
        self._wealth: float = 0.0
        self._carried_treasure: Treasure | None = None
        self._skill = skill
        self._memory = {"treasures": [], "hideouts": []}
        self._survival_steps_remaining = 3
        cell.add_object(self)

    def get_cell(self) -> Cell:
        return self._cell

    def get_stamina(self) -> float:
        return self._stamina

    def get_wealth(self) -> float:
        return self._wealth

    def get_skill(self) -> Skill:
        return self._skill

    def get_memory(self) -> dict:
        return self._memory

    def get_survival_steps_remaining(self) -> int:
        return self._survival_steps_remaining

    def get_carried_treasure(self) -> Treasure | None:
        return self._carried_treasure

    def is_carrying_treasure(self) -> bool:
        return self._carried_treasure is not None

    def deposit_treasure(self) -> None:
        if self._carried_treasure:
            t_type = self._carried_treasure.get_type()
            if t_type == TreasureType.BRONZE:
                self._wealth += 3.0
            elif t_type == TreasureType.SILVER:
                self._wealth += 7.0
            elif t_type == TreasureType.GOLD:
                self._wealth += 13.0
        self._carried_treasure = None

    def move_to(self, new_cell: Cell) -> None:
        self._cell.remove_object(self)
        new_cell.add_object(self)
        self._cell = new_cell
        self._stamina -= 2.0
        if self._stamina < 0:
            self._stamina = 0

    def rest(self) -> None:
        # Only rest if in hideout
        if any(isinstance(obj, Hideout) for obj in self._cell.contents):
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

    def remember(self, treasures: List, hideouts: List[Cell]) -> None:
        for treasure in treasures:
            if treasure not in self._memory["treasures"]:
                self._memory["treasures"].append(treasure)
        for hideout in hideouts:
            if hideout not in self._memory["hideouts"]:
                self._memory["hideouts"].append(hideout)

    def share_memory(self, other: 'TreasureHunter') -> None:
        self._memory["treasures"].extend(t for t in other._memory["treasures"] if t not in self._memory["treasures"])
        self._memory["hideouts"].extend(h for h in other._memory["hideouts"] if h not in self._memory["hideouts"])