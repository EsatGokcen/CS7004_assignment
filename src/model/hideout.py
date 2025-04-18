from src.model.cell import Cell
from src.model.treasure_hunter import TreasureHunter
from src.model.treasure import Treasure
from src.model.treasure_type import TreasureType
from typing import List
import random


class Hideout:
    def __init__(self, cell: Cell):
        self._cell = cell
        self._hunters: List[TreasureHunter] = []
        self._stored_treasure: List[Treasure] = []
        cell.add_object(self)

    def get_cell(self) -> Cell:
        return self._cell

    def get_hunters(self) -> List[TreasureHunter]:
        return self._hunters.copy()

    def has_space(self) -> bool:
        return len(self._hunters) < 5

    def add_hunter(self, hunter: TreasureHunter) -> None:
        if self.has_space():
            self._hunters.append(hunter)
            if hunter not in self._cell.get_contents():
                self._cell.add_object(hunter)

    def remove_hunter(self, hunter: TreasureHunter) -> None:
        if hunter in self._hunters:
            self._hunters.remove(hunter)
            self._cell.remove_object(hunter)

    def share_knowledge(self) -> None:
        for i, h1 in enumerate(self._hunters):
            for j, h2 in enumerate(self._hunters):
                if i != j:
                    h1.share_memory(h2)

    def recruit_new_hunter(self) -> TreasureHunter | None:
        if not self.has_space():
            return None

        skills_present = set(h.get_skill() for h in self._hunters)
        if len(skills_present) > 1 and random.random() < 0.2:
            skill_choice = random.choice(list(skills_present))
            new_hunter = TreasureHunter(self._cell, skill_choice)
            self.add_hunter(new_hunter)
            return new_hunter
        return None

    def store_treasure(self, hunter: TreasureHunter) -> None:
        if hunter.is_carrying_treasure():
            treasure = hunter.get_carried_treasure()
            self._stored_treasure.append(treasure)
            hunter.deposit_treasure()

    def get_stored_treasure(self) -> List[Treasure]:
        return self._stored_treasure.copy()

    def count_treasure_types(self) -> tuple[int, int, int]:
        bronze = silver = gold = 0
        for t in self._stored_treasure:
            if t.get_type() == TreasureType.BRONZE:
                bronze += 1
            elif t.get_type() == TreasureType.SILVER:
                silver += 1
            elif t.get_type() == TreasureType.GOLD:
                gold += 1
        return bronze, silver, gold
