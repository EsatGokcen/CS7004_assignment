from src.controller.config import *
from src.controller.simulation import Simulation
from src.model.eldoria_map import EldoriaMap

def main():
    the_map = EldoriaMap(MAP_WIDTH, MAP_HEIGHT)
    sim = Simulation(the_map)
    sim.run()
    # HUNTERS die too easily and are bad at getting treasure

    # KNIGHTS disappear! Maybe they don't come out of the garrison after resting?
    # KNIGHTS don't challenge or detain hunters as much as they should

    # No use of sklearn or AI methods found, which would be needed for a top grade (70–100). !!!!!

if __name__ == '__main__':
    main()