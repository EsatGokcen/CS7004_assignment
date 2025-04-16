from src.controller.config import *
from src.controller.simulation import Simulation
from src.model.eldoria_map import EldoriaMap

def main():
    the_map = EldoriaMap(MAP_WIDTH, MAP_HEIGHT)
    sim = Simulation(the_map)
    sim.run()
    # HUNTERS DONT MOVE AS SMOOTHLY AS I WOULD PREFER - i think they get tired, make sure they try to get rest for stamina

if __name__ == '__main__':
    main()