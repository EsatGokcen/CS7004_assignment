import unittest
from src.model.garrison import Garrison
from src.model.knight import Knight
from src.model.cell import Cell

class TestGarrison(unittest.TestCase):

    def setUp(self):
        self.cell = Cell(0, 0)
        self.garrison = Garrison(self.cell)

    def test_garrison_initially_empty(self):
        self.assertEqual(len(self.garrison.get_knights()), 0)
        self.assertTrue(self.garrison.has_space())

    def test_add_knight(self):
        knight = Knight(self.cell)
        self.garrison.add_knight(knight)
        self.assertIn(knight, self.garrison.get_knights())
        self.assertIn(knight, self.cell.get_contents())

    def test_remove_knight(self):
        knight = Knight(self.cell)
        self.garrison.add_knight(knight)
        self.garrison.remove_knight(knight)
        self.assertNotIn(knight, self.garrison.get_knights())
        self.assertNotIn(knight, self.cell.get_contents())