from src.controller.config import *
from src.controller.simulation import Simulation
from src.model.eldoria_map import EldoriaMap

def main():
    the_map = EldoriaMap(MAP_WIDTH, MAP_HEIGHT)
    sim = Simulation(the_map)
    sim.run()
    # HUNTERS die too easily and are bad at getting treasure
    # HUNTERS need skills that actually do something - covered initial endurance and navigation

    # KNIGHTS disappear! Maybe they don't come out of the garrison after resting?
    # KNIGHTS don't challenge or detain hunters as much as they should

    # ASK PRINS !!!!!! THE DEADLINE ON BRIEF IS 7TH BUT ON MOODLE IS 5TH !!!!!!!

if __name__ == '__main__':
    main()