from src.controller.config import *
from src.model.eldoria_map import EldoriaMap
from src.model.treasure_type import TreasureType
from src.model.treasure import Treasure
from src.model.treasure_hunter import TreasureHunter
from src.model.hideout import Hideout
from src.model.hunter_skills import Skill
from random import randint, choice

class Simulation:

    def __init__(self, map_obj: EldoriaMap):
        self.map = map_obj
        self.__running = False
        self._hideouts = []

    def scatter_treasures(self, num_treasures: int) -> None:
        for _ in range(num_treasures):
            x = randint(0, self.map.get_width() - 1)
            y = randint(0, self.map.get_height() - 1)
            t_type = choice(list(TreasureType))
            treasure = Treasure(t_type)
            self.map.get_cell(x, y).add_object(treasure)

    def decay_all_treasures(self) -> None:
        for x in range(self.map.get_width()):
            for y in range(self.map.get_height()):
                cell = self.map.get_cell(x, y)
                for obj in cell.contents[:]:
                    if isinstance(obj, Treasure):
                        obj.lose_value()
                        if obj.is_depleted():
                            cell.remove_object(obj)

    def place_hideouts_and_hunters(self, num_hideouts: int, hunters_per_hideout_range: tuple) -> None:

        for _ in range(num_hideouts):
            x = randint(0, self.map.get_width() - 1)
            y = randint(0, self.map.get_height() - 1)
            cell = self.map.get_cell(x, y)
            hideout = Hideout(cell)
            self._hideouts.append(hideout)

            num_hunters = randint(*hunters_per_hideout_range)
            for _ in range(num_hunters):
                skill = choice(list(Skill))
                hunter = TreasureHunter(cell, skill)
                hideout.add_hunter(hunter)

    def run(self):
        self.scatter_treasures(NUM_INITIAL_TREASURES)
        self.place_hideouts_and_hunters(NUM_HIDEOUTS, INITIAL_HUNTERS_PER_HIDEOUT)
        self.__running = True
        while self.__running:
            self.decay_all_treasures()