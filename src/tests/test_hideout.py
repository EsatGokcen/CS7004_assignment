import unittest
from src.model.cell import Cell
from src.model.hunter_skills import Skill
from src.model.treasure import Treasure
from src.model.treasure_type import TreasureType
from src.model.treasure_hunter import TreasureHunter
from src.model.hideout import Hideout


class TestHideout(unittest.TestCase):

    def setUp(self):
        self.cell = Cell(2, 2)
        self.hideout = Hideout(self.cell)

    def test_add_hunter_if_space(self):
        hunter = TreasureHunter(self.cell, Skill.ENDURANCE)
        self.hideout.add_hunter(hunter)
        self.assertIn(hunter, self.hideout.get_hunters())

    def test_does_not_add_hunter_if_full(self):
        for _ in range(5):
            self.hideout.add_hunter(TreasureHunter(self.cell, Skill.NAVIGATION))
        sixth = TreasureHunter(self.cell, Skill.STEALTH)
        self.hideout.add_hunter(sixth)
        self.assertNotIn(sixth, self.hideout.get_hunters())
        self.assertEqual(len(self.hideout.get_hunters()), 5)

    def test_remove_hunter(self):
        hunter = TreasureHunter(self.cell, Skill.STEALTH)
        self.hideout.add_hunter(hunter)
        self.hideout.remove_hunter(hunter)
        self.assertNotIn(hunter, self.hideout.get_hunters())

    def test_store_treasure_removes_from_hunter(self):
        hunter = TreasureHunter(self.cell, Skill.ENDURANCE)
        treasure = Treasure(TreasureType.BRONZE)
        hunter._carried_treasure = treasure  # Simulate carrying
        self.hideout.add_hunter(hunter)
        self.hideout.store_treasure(hunter)
        self.assertIn(treasure, self.hideout.get_stored_treasure())
        self.assertFalse(hunter.is_carrying_treasure())

    def test_share_knowledge_among_hunters(self):
        cell = self.cell
        t = Treasure(TreasureType.GOLD)
        h1 = TreasureHunter(cell, Skill.ENDURANCE)
        h2 = TreasureHunter(cell, Skill.NAVIGATION)
        h1.remember([t], [])
        self.hideout.add_hunter(h1)
        self.hideout.add_hunter(h2)
        self.hideout.share_knowledge()
        self.assertIn(t, h2.get_memory()["treasures"])

if __name__ == '__main__':
    unittest.main()