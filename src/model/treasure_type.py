from enum import Enum

class TreasureType(Enum):
    BRONZE = ('bronze', 3, 10.0)
    SILVER = ('silver', 7, 5.0)
    GOLD = ('gold', 13, 3.0)

    def __init__(self, label, wealth_increase_percent, base_value):
        self.label = label
        self.wealth_increase = wealth_increase_percent
        self.base_value = base_value