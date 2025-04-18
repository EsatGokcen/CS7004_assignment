from src.controller.config import *
from src.controller.simulation import Simulation
from src.model.eldoria_map import EldoriaMap

def main():
    the_map = EldoriaMap(MAP_WIDTH, MAP_HEIGHT)
    sim = Simulation(the_map)
    sim.run()
    # HUNTERS die too easily and are bad at getting treasure
    # HUNTERS need skills that actually do something
    # New treasure should be able to spawn
    # One cell has infinite amount of treasure by the looks of it
    # treasure is all in gold color, it should be bronze and silver too depending on type

     # ASK PRINS !!!!!! THE DEADLINE ON BRIEF IS 7TH BUT ON MOODLE IS 5TH !!!!!!!

if __name__ == '__main__':
    main()