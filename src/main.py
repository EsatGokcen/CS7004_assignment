from src.controller.config import *
from src.controller.simulation import Simulation
from src.model.eldoria_map import EldoriaMap

def main():
    the_map = EldoriaMap(MAP_WIDTH, MAP_HEIGHT)
    sim = Simulation(the_map)
    sim.run()
    # RESET BUTTON DOES NOT WORK PROPERLY - DOES NOT DELETE OLD TREASURE
    # HUNTERS DONT MOVE AS SMOOTHLY AS I WOULD PREFER
    # CONTROL PANEL CAN BE BETTER - TREASURE COLLECTED AND COLOR MATCHING
    # TREASURE COLLECTION MECHANIC MIGHT BE BROKEN

if __name__ == '__main__':
    main()