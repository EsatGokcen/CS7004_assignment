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

    def test_chase_moves_toward_target(self):
        hunter_cell = self.map.get_cell(6, 5)
        hunter = MockTreasureHunter(hunter_cell)
        self.knight._Knight__target = hunter
        self.knight.chase(self.map)
        self.assertEqual(self.knight.get_cell(), hunter_cell)

    def test_retreat_moves_towards_garrison(self):
        self.knight._Knight__stamina = 15
        self.knight.retreat(self.map)
        # Should move one cell toward garrison
        self.assertNotEqual(self.knight.get_cell(), self.start_cell)

    def test_rest_increases_stamina(self):
        self.knight._Knight__resting = True
        self.knight._Knight__stamina = 50
        self.knight.rest()
        self.assertEqual(self.knight.get_stamina(), 60)

if __name__ == '__main__':
    unittest.main()
