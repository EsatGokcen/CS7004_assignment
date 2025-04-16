from src.controller.config import *
from src.view.main_window import MainWindow
from src.model.eldoria_map import EldoriaMap
from src.model.treasure_type import TreasureType
from src.model.treasure import Treasure
from src.model.treasure_hunter import TreasureHunter
from src.model.hideout import Hideout
from src.model.hunter_skills import Skill
from random import randint, choice
from typing import List

class Simulation:

    def __init__(self, map_obj: EldoriaMap):
        self.map = map_obj
        self.__running = False
        self._hideouts: List[Hideout] = []
        self.ui = MainWindow(self.map)
        self.ui.controls.on_start = self.start
        self.ui.controls.on_pause = self.pause
        self.ui.controls.on_reset = self.reset
        self._step_count = 0

    def start(self) -> None:
        if not self.__running:
            self.__running = True
            self.run_step()

    def pause(self) -> None:
        self.__running = False

    def reset(self) -> None:
        self.__running = False
        self.map.clear()  # You'll need to implement this
        self._hideouts.clear()
        self._step_count = 0
        self.ui.info_panel.update_info(0, 0, 0, 0)
        self.scatter_treasures(NUM_INITIAL_TREASURES)
        self.place_hideouts_and_hunters(NUM_HIDEOUTS, INITIAL_HUNTERS_PER_HIDEOUT)
        self.ui.grid_view.draw_grid()

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

    def step_hunters(self) -> None:
        for hideout in self._hideouts:
            for hunter in hideout.get_hunters():
                if not hunter.can_act():
                    hunter.tick_survival()
                    continue

                if hunter.is_critical():
                    hunter.rest()
                    continue

                cell = hunter.get_cell()
                neighbors = self.map.get_adjacent_cells(cell)
                visible_objects = [obj for neighbor in neighbors for obj in neighbor.contents]

                treasures = [obj for obj in visible_objects if isinstance(obj, Treasure)]
                hideouts = [obj for obj in visible_objects if isinstance(obj, Hideout)]

                hunter.remember(treasures, [h.get_cell() for h in self._hideouts])

                if hunter.is_carrying_treasure():
                    # Go to closest hideout if visible
                    for neighbor in neighbors:
                        if any(isinstance(obj, Hideout) for obj in neighbor.contents):
                            hunter.move_to(neighbor)
                            for obj in neighbor.contents:
                                if isinstance(obj, Hideout):
                                    obj.store_treasure(hunter)
                            break
                    else:
                        hunter.move_to(choice(neighbors))
                else:
                    # Pick best treasure
                    if treasures:
                        best = max(treasures, key=lambda t: t.get_value())
                        for neighbor in neighbors:
                            if best in neighbor.contents:
                                hunter.move_to(neighbor)
                                hunter._carried_treasure = best
                                best.mark_collected()
                                break
                    else:
                        hunter.move_to(choice(neighbors))

            hideout.share_knowledge()
            hideout.recruit_new_hunter()

    def run_step(self) -> None:
        if not self.__running:
            return
        self._step_count += 1
        self.decay_all_treasures()
        self.step_hunters()
        self.ui.grid_view.draw_grid()
        hunters = sum(len(h.get_hunters()) for h in self._hideouts)
        knights = 0  # Update this when knight logic is added
        collected = sum(h.get_total_treasure_int() for h in self._hideouts)
        self.ui.info_panel.update_info(self._step_count, hunters, knights, collected)
        self.ui.root.after(500, self.run_step)  # delay in ms

    def run(self) -> None:
        self.scatter_treasures(NUM_INITIAL_TREASURES)
        self.place_hideouts_and_hunters(NUM_HIDEOUTS, INITIAL_HUNTERS_PER_HIDEOUT)
        self.ui.grid_view.draw_grid()
        self.ui.run()

