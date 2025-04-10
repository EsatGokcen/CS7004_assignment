import unittest
from src.model.eldoria_map import EldoriaMap
from src.model.cell import Cell
from src.model.treasure import Treasure, TreasureType

class TestMapAndCell(unittest.TestCase):

    def test_map_wraparound(self):
        m = EldoriaMap(10, 10)
        cell1 = m.get_cell(0, 0)
        cell2 = m.get_cell(10, 10)
        self.assertIs(cell1, cell2)

    def test_cell_add_remove(self):
        cell = Cell(5, 5)
        treasure = Treasure(TreasureType.GOLD)

        self.assertTrue(cell.is_empty())
        cell.add_object(treasure)
        self.assertFalse(cell.is_empty())
        self.assertIn(treasure, cell.contents)

        cell.remove_object(treasure)
        self.assertTrue(cell.is_empty())

if __name__ == '__main__':
    unittest.main()
