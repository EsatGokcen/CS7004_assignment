from src.controller.config import *
from src.controller.simulation import Simulation
from src.model.eldoria_map import EldoriaMap

def main():
    the_map = EldoriaMap(MAP_WIDTH, MAP_HEIGHT)
    sim = Simulation(the_map)
    sim.run()

    # KNIGHTS get stuck still, also knight chase has gotten worse visually. I used to be able to
    # tell but now I can't tell when they are chasing or detaining or challenging.

if __name__ == '__main__':
    main()