from src.model.cell import Cell
from src.model.treasure_hunter import TreasureHunter

class Knight:

    def __init__(self, cell: Cell):
        self.__cell = cell
        self.__stamina: float = 100.0

    def get_cell(self) -> Cell:
        return self.__cell

    def get_stamina(self) -> float:
        return self.__stamina

    def patrol(self):
        # scan 3 cell radius in map for hunters
        # focus on hunter with most wealth
        pass

    def chase(self):
        # focus on a single hunter after patrol
        # limited range pn chase
        # lose 20% of energy after each chase
        pass

    def detain(self):
        # drains 5% of hunter stamina
        # forces hunter to drop any treasure they are carrying
        pass

    def challenge(self):
        # reduces 20% of hunter stamina
        # forces hunter to drop treasure
        pass

    def retreat(self):
        # if stamina is 20% or below retreat to garrison
        pass

    def rest(self):
        # rest until stamina fully restored
        # start patrolling again once stamina fully restored
        pass