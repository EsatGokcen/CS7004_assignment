from src.model.cell import Cell
from src.model.treasure_hunter import TreasureHunter
from src.model.eldoria_map import EldoriaMap
from typing import Optional
import math
import random

class Knight:

    def __init__(self, cell: Cell):
        self.__cell = cell
        self.__stamina: float = 100.0
        self.__target: Optional[TreasureHunter] = None
        self.__resting: bool = False
        self.__angle: float = 0.0
        self.__orbit_radius: int = 1
        self.__garrison_origin: Cell = cell
        self.__direction = None
        self.__step_count: int = 0

    def get_cell(self) -> Cell:
        return self.__cell

    def get_stamina(self) -> float:
        return self.__stamina

    def get_resting(self) -> bool:
        return self.__resting

    def get_target(self) -> Optional[TreasureHunter]:
        return self.__target

    def patrol(self, map_obj: EldoriaMap) -> None:
        if self.__resting or self.__target:
            return

        self.__direction = random.uniform(0, 2 * math.pi)
        self.__step_count = 0

        # Change direction occasionally for variety
        if self.__step_count % 8 == 0:
            angle_variation = random.uniform(-math.pi / 6, math.pi / 6)
            self.__direction += angle_variation

        # Small outward bias from garrison origin
        gx, gy = self.__garrison_origin.get_x(), self.__garrison_origin.get_y()
        cx, cy = self.__cell.get_x(), self.__cell.get_y()
        vec_x, vec_y = cx - gx, cy - gy
        outward_bias = 0.2  # how much to push outward
        self.__direction += outward_bias * math.atan2(vec_y, vec_x)

        # Calculate new position
        step_size = 1
        dx = int(round(step_size * math.cos(self.__direction)))
        dy = int(round(step_size * math.sin(self.__direction)))
        new_x = (cx + dx) % map_obj.get_width()
        new_y = (cy + dy) % map_obj.get_height()

        # Move knight
        self.__cell.remove_object(self)
        self.__cell = map_obj.get_cell(new_x, new_y)
        self.__cell.add_object(self)

        self.__step_count += 1

    def scan(self, map_obj: EldoriaMap) -> None:
        if self.__resting:
            return

        x0, y0 = self.__cell.get_x(), self.__cell.get_y()
        nearby_hunters = []

        for dx in range(-3, 4):
            for dy in range(-3, 4):
                if abs(dx) + abs(dy) <= 3:
                    x, y = (x0 + dx) % map_obj.get_width(), (y0 + dy) % map_obj.get_height()
                    cell = map_obj.get_cell(x, y)
                    for obj in cell.get_contents():
                        if isinstance(obj, TreasureHunter):
                            nearby_hunters.append(obj)

        if nearby_hunters:
            self.__target = max(nearby_hunters, key=lambda h: h.get_wealth(), default=None)

    def chase(self, map_obj: EldoriaMap) -> None:
        if self.__resting or not self.__target or self.__stamina < 20:
            return

        current_x, current_y = self.__cell.get_x(), self.__cell.get_y()
        target_x, target_y = self.__target.get_cell().get_x(), self.__target.get_cell().get_y()

        if (current_x, current_y) == (target_x, target_y):
            action = random.choice([self.detain, self.challenge])
            action()
            self.__target = None
            return

        dx = (target_x - current_x + map_obj.get_width()) % map_obj.get_width()
        dy = (target_y - current_y + map_obj.get_height()) % map_obj.get_height()

        if dx > map_obj.get_width() // 2:
            dx -= map_obj.get_width()
        if dy > map_obj.get_height() // 2:
            dy -= map_obj.get_height()

        step_x = 1 if dx > 0 else -1 if dx < 0 else 0
        step_y = 1 if dy > 0 else -1 if dy < 0 else 0

        new_x = (current_x + step_x) % map_obj.get_width()
        new_y = (current_y + step_y) % map_obj.get_height()

        self.__cell.remove_object(self)
        self.__cell = map_obj.get_cell(new_x, new_y)
        self.__cell.add_object(self)
        self.__stamina -= 20

    def detain(self) -> None:
        if self.__target:
            self.__target.lose_stamina(-5)
            self.__target.drop_treasure()
            print("Hunter detained")

    def challenge(self) -> None:
        if self.__target:
            self.__target.lose_stamina(-20)
            self.__target.drop_treasure()
            print("Hunter challenged")

    def retreat(self, map_obj: EldoriaMap) -> None:
        if self.__stamina <= 20 and not self.__resting:
            current_x, current_y = self.__cell.get_x(), self.__cell.get_y()
            garrison_x, garrison_y = self.__garrison_origin.get_x(), self.__garrison_origin.get_y()

            dx = (garrison_x - current_x + map_obj.get_width()) % map_obj.get_width()
            dy = (garrison_y - current_y + map_obj.get_height()) % map_obj.get_height()

            if dx > map_obj.get_width() // 2:
                dx -= map_obj.get_width()
            if dy > map_obj.get_height() // 2:
                dy -= map_obj.get_height()

            step_x = 1 if dx > 0 else -1 if dx < 0 else 0
            step_y = 1 if dy > 0 else -1 if dy < 0 else 0

            new_x = (current_x + step_x) % map_obj.get_width()
            new_y = (current_y + step_y) % map_obj.get_height()

            self.__cell.remove_object(self)
            self.__cell = map_obj.get_cell(new_x, new_y)
            self.__cell.add_object(self)

            if self.__cell == self.__garrison_origin:
                self.__resting = True
                self.__angle = 0.0
                self.__orbit_radius = 1

    def rest(self) -> None:
        if self.__resting and self.__cell == self.__garrison_origin:
            self.__stamina = min(100.0, self.__stamina + 10.0)
            if self.__stamina == 100.0:
                self.__resting = False