from src.controller.config import *
from src.controller.simulation import Simulation
from src.model.eldoria_map import EldoriaMap

def main():
    the_map = EldoriaMap(MAP_WIDTH, MAP_HEIGHT)
    sim = Simulation(the_map)
    sim.run()

    # KNIGHTS disappear! Maybe they don't come out of the garrison after resting?

if __name__ == '__main__':
    main()