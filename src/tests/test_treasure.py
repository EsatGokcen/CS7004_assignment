import unittest
from src.model.treasure import Treasure, TreasureType

class TestTreasure(unittest.TestCase):

    def test_initial_value_and_type(self):
        treasure = Treasure(TreasureType.SILVER)
        self.assertEqual(treasure.get_type(), TreasureType.SILVER)
        self.assertEqual(treasure.get_value(), TreasureType.SILVER.base_value)

    def test_treasure_decay(self):
        treasure = Treasure(TreasureType.BRONZE)
        initial_value = treasure.get_value()
        treasure.lose_value()
        self.assertLess(treasure.get_value(), initial_value)

    def test_treasure_depletion(self):
        treasure = Treasure(TreasureType.BRONZE)
        for _ in range(88):
            treasure.lose_value()
        self.assertTrue(treasure.is_depleted())
        self.assertAlmostEqual(treasure.get_value(), 0.0, places=6)

if __name__ == '__main__':
    unittest.main()
