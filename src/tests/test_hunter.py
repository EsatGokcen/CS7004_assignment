import unittest
from src.model.cell import Cell
from src.model.treasure import Treasure
from src.model.treasure_type import TreasureType
from src.model.hunter_skills import Skill
from src.model.treasure_hunter import TreasureHunter
from src.model.hideout import Hideout


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

    def test_rest_increases_stamina(self):
        cell = Cell(0, 1)
        Hideout(cell) # hunter can only rest in a hideout
        self.hunter.move_to(cell)  # drop stamina to 98
        self.hunter.rest()
        self.assertEqual(self.hunter.get_stamina(), 99.0)

    def test_stamina_never_exceeds_100(self):
        self.hunter.rest()  # already at 100
        self.assertEqual(self.hunter.get_stamina(), 100.0)

    def test_is_critical_and_collapsed(self):
        self.hunter._stamina = 6.0
        self.assertTrue(self.hunter.is_critical())
        self.hunter._stamina = 0.0
        self.assertTrue(self.hunter.is_collapsed())

    def test_survival_tick_decreases_counter(self):
        self.hunter._stamina = 0.0
        self.assertTrue(self.hunter.can_act())
        self.hunter.tick_survival()
        self.assertEqual(self.hunter._survival_steps_remaining, 2)

    def test_remember_and_share_memory(self):
        self.hunter.remember([self.treasure], [self.hideout_cell])
        self.assertIn(self.treasure, self.hunter.get_memory()["treasures"])
        self.assertIn(self.hideout_cell, self.hunter.get_memory()["hideouts"])

        other = TreasureHunter(self.cell, Skill.ENDURANCE)
        other.remember([], [self.hideout_cell])
        self.hunter.share_memory(other)
        self.assertIn(self.hideout_cell, self.hunter.get_memory()["hideouts"])

if __name__ == '__main__':
    unittest.main()