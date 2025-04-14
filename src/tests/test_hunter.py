import unittest
from src.model.cell import Cell
from src.model.treasure import Treasure
from src.model.treasure_type import TreasureType
from src.model.hunter_skills import Skill
from src.model.treasure_hunter import TreasureHunter


class TestTreasureHunter(unittest.TestCase):

    def setUp(self):
        self.cell = Cell(0, 0)
        self.hunter = TreasureHunter(self.cell, Skill.NAVIGATION)
        self.treasure = Treasure(TreasureType.SILVER)
        self.hideout_cell = Cell(1, 1)

    def test_initial_stamina_and_state(self):
        self.assertEqual(self.hunter.get_stamina(), 100.0)
        self.assertFalse(self.hunter.is_carrying_treasure())
        self.assertEqual(self.hunter.get_memory(), {'treasures': [], 'hideouts': []})

    def test_move_to_reduces_stamina(self):
        new_cell = Cell(0, 1)
        self.hunter.move_to(new_cell)
        self.assertEqual(self.hunter.get_stamina(), 98.0)
        self.assertEqual(self.hunter.get_cell(), new_cell)

if __name__ == '__main__':
    unittest.main()