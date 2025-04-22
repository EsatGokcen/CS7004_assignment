import unittest
from src.model.knight import Knight
from src.model.eldoria_map import EldoriaMap
from src.model.treasure_hunter import TreasureHunter
from src.model.hunter_skills import Skill

class MockTreasureHunter(TreasureHunter):
    def __init__(self, cell, wealth=10):
        super().__init__(cell, Skill.NAVIGATION)
        self._wealth = wealth

    def modify_stamina(self, num):
        self._stamina += num

class TestKnight(unittest.TestCase):

    def setUp(self):
        self.map = EldoriaMap(10, 10)
        self.start_cell = self.map.get_cell(5, 5)
        self.knight = Knight(self.start_cell)

    def test_patrol_spiral_movement(self):
        prev_x, prev_y = self.knight.get_cell().get_x(), self.knight.get_cell().get_y()
        self.knight.patrol(self.map)
        new_x, new_y = self.knight.get_cell().get_x(), self.knight.get_cell().get_y()
        self.assertNotEqual((prev_x, prev_y), (new_x, new_y))

    def test_scan_selects_wealthiest(self):
        c1 = self.map.get_cell(6, 5)
        c2 = self.map.get_cell(5, 6)
        h1 = MockTreasureHunter(c1, wealth=5)
        h2 = MockTreasureHunter(c2, wealth=20)
        self.knight.scan(self.map)
        self.assertEqual(self.knight.get_target(), h2)