from src.controller.config import *
from src.controller.treasure_controller import *
from src.controller.hunter_and_hideout_controller import *
from src.controller.knight_and_garrison_controller import *
from src.view.main_window import MainWindow
from src.model.eldoria_map import EldoriaMap
from src.model.hideout import Hideout
from src.model.garrison import Garrison
from src.model.knight import Knight
from typing import List, Optional

class Simulation:

    def __init__(self, map_obj: EldoriaMap):
        self.map = map_obj
        self.__running = False
        self._hideouts: List[Hideout] = []
        self.ui = MainWindow(self.map)
        self._garrison: Optional[Garrison] = None
        self._knights: List[Knight] = []
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
        self.map.clear()
        self._hideouts.clear()
        self._step_count = 0
        self.ui.info_panel.update_info(0, 0, 0, NUM_HIDEOUTS, 0, 0, 0, 0)
        scatter_treasures(NUM_INITIAL_TREASURES, self.map)
        place_hideouts_and_hunters(self._hideouts, self.map, NUM_HIDEOUTS, INITIAL_HUNTERS_PER_HIDEOUT)
        self._garrison, self._knights = place_garrison_with_knights(self.map, NUM_KNIGHTS)
        self.ui.grid_view.draw_grid()

    def run_step(self) -> None:
        if not self.__running:
            return
        self._step_count += 1
        decay_all_treasures(self.map)
        step_hunters(self._hideouts, self.map)
        step_knights(self._knights, self.map)
        self.ui.grid_view.draw_grid()

        hunters = sum(len(h.get_hunters()) for h in self._hideouts)
        knights = len(self._knights)
        hideouts = len(self._hideouts)
        garrisons = 1 if self._garrison else 0

        bronze = silver = gold = 0
        for h in self._hideouts:
            b, s, g = h.count_treasure_types()
            bronze += b
            silver += s
            gold += g

        self.ui.info_panel.update_info(
            self._step_count, hunters, knights, hideouts, garrisons, bronze, silver, gold
        )
        self.ui.root.after(500, self.run_step)  # delay in ms

    def run(self) -> None:
        scatter_treasures(NUM_INITIAL_TREASURES, self.map)
        place_hideouts_and_hunters(self._hideouts, self.map, NUM_HIDEOUTS, INITIAL_HUNTERS_PER_HIDEOUT)
        self._garrison, self._knights = place_garrison_with_knights(self.map, NUM_KNIGHTS)
        self.ui.grid_view.draw_grid()
        self.ui.run()

