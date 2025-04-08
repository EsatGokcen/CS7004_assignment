class Treasure:

    def __init__(self, treasure_type: str):
        self.__value: float = 100.00
        self.__type = treasure_type

    def get_value(self) -> float:
        return self.__value

    def get_type(self) -> str:
        return self.__type

    def lose_value(self) -> None:
        self.__value = self.__value * 0.09
