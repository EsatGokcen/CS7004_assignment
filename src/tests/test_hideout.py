import unittest
from src.model.cell import Cell
from src.model.hunter_skills import Skill
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


if __name__ == '__main__':
    unittest.main()