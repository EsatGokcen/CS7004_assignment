from src.controller.config import *
from src.controller.simulation import Simulation
from src.model.eldoria_map import EldoriaMap

def main():
    the_map = EldoriaMap(MAP_WIDTH, MAP_HEIGHT)
    sim = Simulation(the_map)
    sim.run()
    # HUNTERS DONT MOVE AS SMOOTHLY AS I WOULD PREFER
    # CONTROL PANEL CAN BE BETTER - TREASURE COLLECTED AND COLOR MATCHING

if __name__ == '__main__':
    main()