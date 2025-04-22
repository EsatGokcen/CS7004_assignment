import unittest
from src.model.garrison import Garrison
from src.model.cell import Cell

class TestGarrison(unittest.TestCase):

    def setUp(self):
        self.cell = Cell(0, 0)
        self.garrison = Garrison(self.cell)

    def test_garrison_initially_empty(self):
        self.assertEqual(len(self.garrison.get_knights()), 0)
        self.assertTrue(self.garrison.has_space())