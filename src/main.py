from src.controller.config import *
from src.controller.simulation import Simulation
from src.model.eldoria_map import EldoriaMap

def main():
    the_map = EldoriaMap(MAP_WIDTH, MAP_HEIGHT)
    sim = Simulation(the_map)
    sim.run()
    # HUNTERS die too easily and are bad at getting treasure
    # HUNTERS need skills that actually do something - covered initial endurance and navigation
    # New treasure should be able to spawn

    # add controllers for knight and garrison classes

    # Simulation needs to stop when there are no more treasure left to collect or no more hunter left to collect treasures

    # ASK PRINS !!!!!! THE DEADLINE ON BRIEF IS 7TH BUT ON MOODLE IS 5TH !!!!!!!

if __name__ == '__main__':
    main()