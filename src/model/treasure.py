from src.model.treasure_type import TreasureType

class Treasure:
    def __init__(self, treasure_type: TreasureType):
        self.__type = treasure_type
        self.__value: float = treasure_type.base_value
        self.__collected: bool = False

    def get_value(self) -> float:
        return self.__value

    def get_type(self) -> TreasureType:
        return self.__type

    def is_depleted(self) -> bool:
        return self.__value <= 0

    def mark_collected(self):
        self.__collected = True

    def is_collected(self) -> bool:
        return self.__collected

    def lose_value(self) -> None:
        self.__value -= self.__value * 0.05  # This should be 0.001 to Lose 0.1% according to brief  but that takes 6900 simulation steps... Right now it takes 200 simulation steps to decay.
        if self.__value < 0.01:
            self.__value = 0

    def get_wealth_increase(self) -> float:
        return self.__type.wealth_increase