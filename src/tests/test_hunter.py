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

if __name__ == '__main__':
    unittest.main()